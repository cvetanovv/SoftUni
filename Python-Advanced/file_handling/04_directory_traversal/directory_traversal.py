from os import walk

files_by_ext = {}
for _, _, files in walk("."):
    for file in files:
        extension = file.split(".")[-1]
        if extension not in files_by_ext:
            files_by_ext[extension] = []
        files_by_ext[extension].append(file)

with open('result.txt', 'w') as output:
    for extension, files in sorted(files_by_ext.items()):
        output.write(f".{extension}\n")
        for file in sorted(files):
            output.write(f"--- {file}\n")