import subprocess
import os

# Inkscapeをインストールした場所
Inkscape_PATH = 'C:\\Program Files\\Inkscape\\bin\\inkscapecom.com'

input_file_name = ''

# ---- ファイル名のリスト取得 ---- #
current_PATH = os.getcwd()
filepath_list = os.listdir(current_PATH)
input_file_list = []
for filename in filepath_list:
    if filename[-4:] == '.svg':
        input_file_list.append(filename)

# print(input_file_list)

output_file_list = []
for svg in input_file_list:
    output_file_list.append(svg[:-4] + "_converted.eps")

print("convert to:", output_file_list)

# ---- ファイル変換 ---- #
for i in range(len(input_file_list)):
    output_command = '--export-filename=' + output_file_list[i]

    result = subprocess.run([Inkscape_PATH, output_command, input_file_list[i]])

    if result.returncode == 0:
        print("Success!")
    else :
        print("returncode:",result.returncode)
