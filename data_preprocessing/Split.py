import os
import shutil
import random

src_path1 = 'new/train/images'
src_path2 = 'new/train/labels'

dst_path1 = 'new/val/images'
dst_path2 = 'new/val/labels'

files = os.listdir(src_path1)
random_files = random.sample(files, 1539)

for file in random_files:
    source_path1 = os.path.join(src_path1, file)
    destination_path1 = os.path.join(dst_path1, file)
    shutil.move(source_path1, destination_path1)


for file in random_files:
    source_path2 = os.path.join(src_path2, os.path.splitext(file)[0]) + ".txt"
    destination_path2 = os.path.join(dst_path2, os.path.splitext(file)[0]) + ".txt"
    shutil.move(source_path2, destination_path2)