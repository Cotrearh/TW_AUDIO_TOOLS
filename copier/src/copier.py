import os
import shutil

def parse(src_file, src_dir, out_dir, append = None):
    with open(src_file, "r") as file:
        try:
            os.mkdir(out_dir)
        except Exception as err:
            print(err)
        
        while line := file.readline():
            line = line.rstrip()
            file_id = line.split("\t")[0]
            file_name = f"{file_id}.wem"
            print(file_name)
            shutil.copyfile(f"{src_dir}/{file_name}", f"{out_dir}/{file_name}")

    print("COMPLETED!")
    input('Press ENTER to continue: ')
