#!/usr/bin/env python3

import os
import stat
import sys
from pathlib import Path
from git import Repo


def create_folder_if_not_exists(folder_name):
    if not Path(folder_name).exists():
        Path(folder_name).mkdir(parents=True, exist_ok=True)
        os.chmod(folder_name, 0o755)
        print("... map {} gemaakt  [mode=755]".format(folder_name))
    else:
        print("... map {} bestaat al.".format(folder_name))


def create_file_if_not_exists(file_name, lines=None):
    if not Path(file_name).exists():
        Path(file_name).touch(0x755)
        os.chmod(file_name, 0o755)
        if not lines == None and isinstance(lines, list):
            with open(file_input, 'w') as f:
                for line in lines:
                    f.write(line + "\n")
        print("... bestand " + file_name + " gemaakt [mode=755].")
    else:
        print("... bestand {} bestaat al.".format(file_name))

    # i've excluded example and input files from git add
    if "input" not in os.path.basename(file_name) and "example" not in os.path.basename(file_name):
        repo.git.add(file_name)

current_folder = sys.path[0]
repo = Repo(current_folder)
print("Connecting to git repository in {}".format(current_folder))

propose = ''
for day in range(1, 26):
    if not Path(os.path.join(current_folder, 'day' + str(day).rjust(2,'0'))).exists():
        propose = str(day)
        break
if propose == '':
    print("Fout: alle mappen day01 t/m day25 bestaan al.")
    exit(0)

day = input("Mappen en bestanden maken voor welk dagnummer? (1 t/m 25, 0 om te stoppen) [" + propose + "]: ")
if day == '0':
    exit(0)
if propose == '' and not day.isnumeric():
    print("Fout: voer een getal in tussen 0 en 25")
    exit(0)
if propose == '' and not (0 <= int(day) <= 25):
    print("Fout: voer een getal in tussen 0 en 25")
    exit(0)
if day == '':
    day = propose

daynumber_formatted = day.rjust(2, '0')
folder_name = os.path.join(sys.path[0], "day" + daynumber_formatted)
create_folder_if_not_exists(folder_name)

file_input = os.path.join(folder_name, 'input{}.txt'.format(daynumber_formatted))
print(file_input)
create_file_if_not_exists(file_input)

file_input = os.path.join(folder_name, 'example{}.txt'.format(daynumber_formatted))
create_file_if_not_exists(file_input)

# file_input = os.path.join(folder_name, 'example{}a-outcome.txt'.format(daynumber_formatted))
# create_file_if_not_exists(file_input)

# file_input = os.path.join(folder_name, 'example{}b.txt'.format(daynumber_formatted))
# create_file_if_not_exists(file_input)

# file_input = os.path.join(folder_name, 'example{}b-outcome.txt'.format(daynumber_formatted))
# create_file_if_not_exists(file_input)


file_input = os.path.join(folder_name, 'day{}a.py'.format(daynumber_formatted))
lines = [
        r'#!/usr/bin/env python3'
        , r''
        , r'import os'
        , r'import sys'
        , r''
        , r'# read input file into "lines"'
        , r'input_file = os.path.join(sys.path[0], "example{}.txt")'.format(daynumber_formatted)
        , r'# input_file = os.path.join(sys.path[0], "input{}.txt")'.format(daynumber_formatted)
        , r'with open(input_file) as f:'
        , r'    lines = f.read().splitlines()'
        , r''
        , r'for line in lines:'
        , r'    print("Line: ", line)'
        , r'print("---------------")'
        , r'print("ANSWER: ")'
    ]
create_file_if_not_exists(file_input, lines)

file_input = os.path.join(folder_name, 'day{}b.py'.format(daynumber_formatted))
lines = [
        r'#!/usr/bin/env python3'
        , r''
        , r'import os'
        , r'import sys'
        , r''
        , r'# read input file into "lines"'
        , r'input_file = os.path.join(sys.path[0], "example{}.txt")'.format(daynumber_formatted)
        , r'# input_file = os.path.join(sys.path[0], "input{}.txt")'.format(daynumber_formatted)
        , r'with open(input_file) as f:'
        , r'    lines = f.read().splitlines()'
    ]
create_file_if_not_exists(file_input, lines)

# status = repo.git.status()
# print(status)
