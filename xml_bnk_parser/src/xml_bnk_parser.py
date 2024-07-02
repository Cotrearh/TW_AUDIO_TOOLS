def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit

from  xml.etree.cElementTree import iterparse
from dataclasses import dataclass


@dataclass
class CAkSound:
    sound_id: str
    src_wem_id: str
    direct_parent_id: str

    def __eq__(self, other):
        return self.sound_id==other.sound_id and self.src_wem_id==other.src_wem_id
    
    def __hash__(self):
        return hash(('sound_id', self.sound_id, 'src_wem_id', self.src_wem_id))

@dataclass
class CAkActionPlay:
    action_play_id: str
    ext_sound_id: str

@dataclass
class CAkEvent:
    readable_name: str
    ext_action_play_id: str

@dataclass
class CAkDialogueEvent:
    readable_name: str
    children: dict[str, list[CAkSound]]

    def get_children(self):
        children_list = []
        for k, v in self.children.items():
            for i, s in enumerate(v):
                children_list.append((s.src_wem_id, f"{self.readable_name}_{k}_{i + 1}"))
        
        return children_list

def parse(src_file, out_file, append = None):
    CAkSound_list = []
    CAkSound_dict = dict()
    CAkActionPlay_list = []
    CAkEvent_list = []
    CAkDialogueEvent_list = []

    for event, elem in iterparse(src_file, events=('start','end')):
        if event == "end":
            # parse CAkSound to get source wem file
            direct_parent_id = None
            if elem.tag == "obj" and elem.attrib.get("na") == "CAkSound":
                sound = CAkSound(None, None, None)
                fields = elem.findall("./fld")
                for field in fields:
                    # CAkSound ID
                    if field.attrib.get("na") == "ulID":
                        sound_id = field.attrib.get("va")
                        sound.sound_id = sound_id
                fields = elem.findall(".//fld")
                for field in fields:
                    # Source wem ID
                    if field.attrib.get("na") == "sourceID":
                        src_wem_id = field.attrib.get("va")
                        sound.src_wem_id = src_wem_id
                    # DirectParentID for dialogue events
                    if field.attrib.get("na") == "DirectParentID":
                        direct_parent_id = field.attrib.get("va")
                
                print(f"CAkSound: src_wem_id {sound.src_wem_id} ; sound_id {sound.sound_id}")
                CAkSound_list.append(sound)
                if direct_parent_id:
                    try:
                        CAkSound_dict[direct_parent_id].append(sound)
                    except:
                        CAkSound_dict[direct_parent_id] = []
                        CAkSound_dict[direct_parent_id].append(sound)
                elem.clear()

            
            # parse CAkDialogueEvent 
            if elem.tag == "obj" and elem.attrib.get("na") == "CAkDialogueEvent":
                dialogue_event = CAkDialogueEvent(None, dict())
                fields = elem.findall("./fld")
                for field in fields:
                    # Get CAkDialogueEvent readable name
                    if field.attrib.get("na") == "ulID":
                        dialogue_event_name = field.attrib.get("hn")
                        dialogue_event.readable_name = dialogue_event_name
                objs = elem.findall(".//obj")
                for obj in objs:
                    # Get connected sound node
                    if obj.attrib.get("na") == "Node":
                        node_readable_name, audio_node_id = None, None
                        for child in obj:
                            if child.tag == "fld" and child.attrib.get("na") == "key":
                                node_readable_name = child.attrib.get("hn")
                            if child.tag == "fld" and child.attrib.get("na") == "audioNodeId":
                                audio_node_id = child.attrib.get("va")
                        if node_readable_name:
                            sound_list = CAkSound_dict.get(audio_node_id, [])
                            
                            if sound_list:
                                dialogue_event.children[node_readable_name] = sound_list
                                
                print(f"CAkDialogueEvent: readable_name {dialogue_event.readable_name} ; children_num: {len(dialogue_event.children)}")
                CAkDialogueEvent_list.append(dialogue_event)
                elem.clear()
            
            # parse CAkActionPlay to get link to source wem file
            if elem.tag == "obj" and elem.attrib.get("na") == "CAkActionPlay":
                action = CAkActionPlay(None, None)
                for child in elem:
                    if event == "end":
                        if child.tag == "fld" and child.attrib.get("na") == "ulID":
                            # action play id
                            action_play_id = child.attrib.get("va")
                            action.action_play_id = action_play_id
                        if child.tag == "obj" and child.attrib.get("na") == "ActionInitialValues":
                            fields = child.findall("./fld")
                            for field in fields:
                                # link to source wem
                                if field.attrib.get("na") == "idExt":
                                    ext_sound_id = field.attrib.get("va")
                                    action.ext_sound_id = ext_sound_id
                
                print(f"CAkActionPlay: action_play_id {action.action_play_id} ; ext_sound_id {action.ext_sound_id}")
                CAkActionPlay_list.append(action)
                elem.clear()

            # parse CAkEvent for readable event names
            if elem.tag == "obj" and elem.attrib.get("na") == "CAkEvent":
                ca_event = CAkEvent(None, None)
                for child in elem:
                    if event == "end":
                        if child.tag == "fld" and child.attrib.get("na") == "ulID":
                            # readable name
                            readable_name = child.attrib.get("hn")
                            ca_event.readable_name = readable_name
                        if child.tag == "obj" and child.attrib.get("na") == "EventInitialValues":
                            list_elements = child.findall("./lst/obj/fld")
                            for list_element in list_elements:
                                # link to CAkActionPlay
                                ext_action_play_id = list_element.attrib.get("va")
                                ca_event.ext_action_play_id = ext_action_play_id
                
                print(f"CAkEvent: readable_name {ca_event.readable_name} ; ext_action_play_id {ca_event.ext_action_play_id}")
                CAkEvent_list.append(ca_event)
                elem.clear()



    with open(out_file, "w") as file:
        sound_list = list(set(CAkSound_list))
        for sound in sound_list:
            connected_actions = [action.action_play_id for action in CAkActionPlay_list if sound.sound_id == action.ext_sound_id]
            connected_events = [event.readable_name for event in CAkEvent_list if event.ext_action_play_id in connected_actions]
            if connected_events:
                print(f"{sound.src_wem_id} {' '.join(connected_events)}")
                file.write(f"{sound.src_wem_id}\t{'\t'.join(connected_events)}\n")
        
        for dialogue_event in CAkDialogueEvent_list:
            for c in dialogue_event.get_children():
                file.write(f"{c[0]}\t{c[1]}\n")

    print("COMPLETED!")
    input('Press ENTER to continue: ')
