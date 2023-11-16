from config import allowed_pattern, min_word_limit, max_word_limit, fname, lname
from datetime import datetime
from config import install
import re
import subprocess

install('pandas')
import pandas as pd

def is_valid(sentence, pattern=allowed_pattern):
    matches = re.findall(pattern, sentence)
    matches = ''.join(matches)
    if 'w' in matches or 'W' in matches:
        matches = ''
    return len(matches) == len(sentence)

file_name = input('file name (with extension): ')
df = pd.read_csv(f'./data/{file_name}')
print('[INFO] Upload: Successful')
text_column = input('sentence column: ')
sentences = list(df[text_column])
print('[INFO] Fetch: Successful')
print()
print('[INFO] Deleting invalid sentences...')
# delete invalid sentences
tmp = []
for sentence in sentences:
    if is_valid(sentence):
        tmp.append(sentence)
sentences = tmp

print('[INFO] Trimming and Splitting...')
tmp = set()
for sentence in sentences:
    sentence = sentence.strip().split('.')
    for s in sentence:
        if s:
            tmp.add(s[0].capitalize() + s[1:] +'.')
sentences = list(tmp)

print('[INFO] Applying word limitation...')
tmp = []
for sentence in sentences:
    current = sentence
    sentence = sentence.split(' ')
    if len(sentence) >= min_word_limit and len(sentence) <= max_word_limit:
        tmp.append(current)
sentences = tmp

current_time = datetime.now()
formatted_time = current_time.strftime("%S_%M_%H_%d_%m_%Y")

print('[INFO] Saving file...')
df = pd.DataFrame({"sentences": sentences})

file_name = f'dev_{fname}_{lname}_{formatted_time}.csv'
df.to_csv(f'./export/{file_name}')

print(f'[SUCCESS] File saved as {file_name}')
