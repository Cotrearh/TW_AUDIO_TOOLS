def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit

import speech_recognition as sr
import csv

r = sr.Recognizer()

class VoData:
    def __init__(self, name, text, wem):
        self.name = name
        self.wem = wem
        self.text = text

def recognize_voice(src_audio, filename):
    with src_audio as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print(f"File: {filename} Text: {s}")
        return filename, s
    except Exception as e:
        print("Exception: "+str(e))
        return filename, "RECOGNIZE ERROR"
        

def parse(src_file, src_dir, out_file, append = None):
    counter = 1
    batch = []
    vo_list = []

    with open(src_file, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        for row in reader:
            vo_data = VoData(
                wem=row[0],
                text="",
                name=row[1]
            )

            vo_list.append(vo_data)

            
    for vo in vo_list:
        print(f"{counter}/{len(vo_list)}")
        filename = vo.wem + ".wem.wav"
        src_file_path = f"{src_dir}/{filename}"

        src_audio = sr.AudioFile(src_file_path)
        _, text = recognize_voice(src_audio, filename)
        vo.text = text
        batch.append(vo)
        
        if len(batch) >= 10:
            print("writing file")
            with open(out_file, "a") as o_file:
                for item in batch:
                    o_file.write(f"{item.wem}\t{item.text}\t{item.name}\n")
            
            batch = []
        
        counter += 1
        
    if len(batch) > 0:
        print("writing file")
        with open(out_file, "a") as o_file:
            for item in batch:
                o_file.write(f"{item.wem}\t{item.text}\t{item.name}\n")


    print("COMPLETED!")
    input('Press ENTER to continue: ')
