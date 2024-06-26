#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import re

out_file = f"D:/MOD/audio/wwnames.txt"


def parse(src_file, out_file, append = None):
    with open(src_file, mode='r') as file, open(out_file, mode='w') as outFile:
        fileContent = file.read()
        fileContent = fileContent.replace("\\", "#")
        line = re.sub(r"[^a-zA-Z_0-9]", "#", fileContent)
        
        lines = line.split("#")
        for line in lines:
            if len(line) >= 3:
                print(line)
                outFile.write(f"{line}\n")

    print("COMPLETED!")
