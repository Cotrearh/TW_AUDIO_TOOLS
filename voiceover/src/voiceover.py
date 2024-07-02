def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

import sys
sys.excepthook = show_exception_and_exit

import base64
import csv
import os

import httpx

class VoData:
    def __init__(self, name, text, need_update):
        self.name = name.replace(".wem.wav", "")
        self.text = text
        self.need_update = need_update

    def get_file_name(self, prefix, postfix):
        return prefix + self.name + postfix


out_format = "wav"


def parse(voice_id, src_file, wav_folder, api_token):
    get_vo_url = f"https://public.api.voice.steos.io/api/v1/synthesize-controller/synthesis-by-text?authToken={api_token}"
    get_balance_url = f"https://public.api.voice.steos.io/api/v1/platform-controller/balance/{api_token}"
    
    vo_list = []

    # tmp_file = f"D:/MOD/audio/{bank_name}_TMP.tsv"

    with open(src_file, newline='', encoding = 'utf-8') as csvfile: #, open(tmp_file, "w", encoding = 'utf-8') as outFile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
        # writer = csv.writer(outFile, delimiter='\t')
        for row in reader:
            vo_data = VoData(
                name=row[0],
                text=row[2],
                need_update=1
            )

            # col_values = []
            # for col in row:
            #     col_values.append(col)
            # if len(row) <= 3:
            #     col_values.append(0)
            # col_values[-1] = 0

            # writer.writerow(col_values)

            if int(vo_data.need_update) == 1:
                vo_list.append(vo_data)

        # os.rename(tmp_file, src_file)

    response = httpx.get(get_balance_url)
    tokens_amount = response.json()["tokensAmount"]
    print(f"Balance: {tokens_amount}")
    
    counter = 0
    counter_2 = 1
    length = len(vo_list)
    if tokens_amount > 5:
        for vo_data in vo_list:
            print(vo_data.text)

            body = {
                "voiceId": voice_id,
                "text": vo_data.text,
                "format": out_format
            }

            response = httpx.post(get_vo_url, json=body, timeout=20)
            print(response.status_code)
            answer = response.json()
            file_contents = answer["fileContents"]
            if file_contents == '':
                print("Empty response")
                for i in range(1, 6):
                    print(f"retry {i}")
                    response = httpx.post(get_vo_url, json=body, timeout=20)
                    answer = response.json()
                    file_contents = answer["fileContents"]
                    if file_contents != '':
                        print("retry success!")
                        break

            decoded_bytes = base64.b64decode(answer["fileContents"])

            file_name = vo_data.get_file_name("", f".{out_format}")

            with open(f"{wav_folder}/{file_name}", "wb") as fout:
                fout.write(decoded_bytes)

            counter += 1
            print(f"{counter_2}/{length} ready")
            counter_2 += 1

            if counter >= 10:
                counter = 0
                response = httpx.get(get_balance_url)
                tokens_amount = response.json()["tokensAmount"]
                print(f"Balance: {tokens_amount}")

                if tokens_amount <= 10:
                    print(f"Balance is too low!")
                    break

