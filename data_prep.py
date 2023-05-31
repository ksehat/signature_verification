import os
import re

images_path = 'C:\Project\signature_verification\data'
os.chdir(images_path)
name_pattern = re.compile(r'[A-Za-z]+')

labels = []
for i, f in enumerate(os.listdir(images_path)):
    match = name_pattern.search(f)
    if match:
        name = match.group()
        labels.append(name)
        os.rename(f, f'{i}.png')

list_str = '\n'.join(map(str, labels))

# Open the file in write mode
with open(f'{images_path}/labels.txt', 'w') as f:
    f.write(list_str)
