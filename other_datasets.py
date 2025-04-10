import requests
import time

# CMU Speech Haitian Creole URLs
CMU_LICENSE_URL = "http://www.speech.cs.cmu.edu/haitian/COPYING"
CMU_WAV_TRANSCRIPTION = "http://www.speech.cs.cmu.edu/haitian/speech/data/cmu_haitian_speech/etc/txt.done.data"
CMU_WAV_FILE_TEMPLATE = "http://www.speech.cs.cmu.edu/haitian/speech/data/cmu_haitian_speech/wav/{wav_file}"
# CMU Speech Haitian Creole URLs
CMU2_LICENSE_URL = "http://www.speech.cs.cmu.edu/haitian/speech/data2/cmu_haitian_speech2/COPYING"
CMU2_WAV_TRANSCRIPTION = "http://www.speech.cs.cmu.edu/haitian/speech/data2/cmu_haitian_speech2/etc/txt.done.data"
CMU2_WAV_FILE_TEMPLATE = "http://www.speech.cs.cmu.edu/haitian/speech/data2/cmu_haitian_speech2/wav/{wav_file}"

def download_file(url, file_path):
    file_bytes = get_file_from_url(url)
    with open(file_path, "wb+") as f:
        f.write(file_bytes)

def get_file_from_url(url) -> bytes:
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    else:
        print(f"Error: {res}")
    time.sleep(0.25)

def download_cmu_speech_dataset():
    # download data license
    download_file(CMU_LICENSE_URL, "./other_datasets/cmu_speech_haitian_creole/LICENSE")

    transcriptions = get_file_from_url(CMU_WAV_TRANSCRIPTION).decode("utf-8").split('\n')

    for i, transcription in enumerate(transcriptions):
        line_parts = transcription.split('"')
        speaker_id = line_parts[0].replace("(", "").strip()
        transcription = line_parts[1].strip()
        download_file(CMU_WAV_FILE_TEMPLATE.format(wav_file=f"{speaker_id}.wav"), f"./other_datasets/cmu_speech_haitian_creole/{i}.wav")
        with open(f"./other_datasets/cmu_speech_haitian_creole/{i}.txt", "w") as f:
            f.write(transcription)
        with open(f"./other_datasets/cmu_speech_haitian_creole/{i}.metadata", "w") as f:
            f.write(f"speaker: {speaker_id}")

def download_cmu2_speech_dataset():
    # download data license
    download_file(CMU2_LICENSE_URL, "./other_datasets/cmu_speech_haitian_creole_2/LICENSE")

    transcriptions = get_file_from_url(CMU2_WAV_TRANSCRIPTION).decode("utf-8").split('\n')

    for i, transcription in enumerate(transcriptions):
        line_parts = transcription.split('"')
        speaker_id = line_parts[0].replace("(", "").strip()
        transcription = line_parts[1].strip()
        download_file(CMU2_WAV_FILE_TEMPLATE.format(wav_file=f"{speaker_id}.wav"), f"./other_datasets/cmu_speech_haitian_creole_2/{i}.wav")
        with open(f"./other_datasets/cmu_speech_haitian_creole_2/{i}.txt", "w") as f:
            f.write(transcription)
        with open(f"./other_datasets/cmu_speech_haitian_creole_2/{i}.metadata", "w") as f:
            f.write(f"speaker: {speaker_id}")



chars_to_ignore_regex = '[\,\?\.\!\;\:\"]'
import re

with open('/home/kur/Desktop/code_projects/KreyolNLP/cmu_speech_corupus.txt') as c_file:
    corpus = c_file.read()


new_words = set()
new_data_idxs = set()
i_to_nw = {}
for i in range(2062):
    with open(f"./other_datasets/cmu_speech_haitian_creole_2/{i}.txt", "r") as txt_file:
        for line in txt_file.readlines():
            for word in line.split():
                word = re.sub(chars_to_ignore_regex, '', word)
                if not word:
                    continue
                if word[0].isupper():
                    continue
                if not word in corpus and word.isalpha() and word not in new_words:
                    new_words.add(word)
                    new_data_idxs.add(i)
                    if not i in i_to_nw:
                        i_to_nw[i] = []
                    i_to_nw[i].append(word)
                    # print(i)
                    # print(line)
                    # print(word)
                    # print('-------------------')
# 1028, 1329, 1394, 1395, 1396, 1397, 1398, 1400, 1404, 1405, 1408, 1409, 1414, 1415, 1416, 1418
# 1436, 1451, 1975, 1986
import shutil
idx = [1028, 1329, 1394, 1395, 1396, 1397, 1398, 1400, 1404, 1405, 1408, 1409, 1414, 1415, 1416, 1418, 436, 1451, 1975, 1986]
for i in idx:
    shutil.copyfile(f"./other_datasets/cmu_speech_haitian_creole_2/{i}.txt", f"./train2/{i}.txt")
    shutil.copyfile(f"./other_datasets/cmu_speech_haitian_creole_2/{i}.wav", f"./train2/{i}.wav")

# new_data_idxs -= set([38, 321, 330, 334, 410, 414, 680, 705, 779])
# a = list(new_data_idxs)
# a.sort()
# print(a)
# print(i_to_nw)
