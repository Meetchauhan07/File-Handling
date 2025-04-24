#specific subdirectory and copy one file from another subdirectory to newly created subdirectory.
import os
import shutil

source_dir = "source_folder"
target_dir = "target_folder"
file_name = "subdirectory.txt"

os.makedirs(target_dir, exist_ok=True)
shutil.copy(os.path.join(source_dir, file_name), target_dir)

#copy contents of one file to another
with open("source.txt", "r") as source, open("target.txt", "w") as target:
    for line in source:
        target.write(line.upper())

#merges lines alternatively from two files and writes the results to new file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])
            




