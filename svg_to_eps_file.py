import subprocess

# Inkscapeをインストールした場所
Inkscape_PATH = 'C:\\Program Files\\Inkscape\\bin\\inkscapecom.com'

input_file_name = ''

# ---- ファイル名受け取り ---- #
print("enter filename(cancel:c) : ")
input_file_name = input()
# print('\n')
# print(input_file_name)

while True:
    try:
        input_file_name = input()
        break
    except ValueError:
        print("Try again...")

# ---- ファイル名処理（.svgの有無に対応） ---- #
file_ext = input_file_name[-4:]
if file_ext == '.svg':
    input_file_name = input_file_name[:-4]
else:
    input_file_name = input_file_name

print("convert to:" + input_file_name + "_converted.eps")

# ---- ファイル変換 ---- #
output_file_name = input_file_name + '_converted'
output_command = '--export-filename=' + output_file_name + '.eps'

result = subprocess.run([Inkscape_PATH, output_command, input_file_name + '.svg'])

if result.returncode == 0:
    print("Success!")
else :
    print("returncode:",result.returncode)
