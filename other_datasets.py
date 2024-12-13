import requests
import time

# CMU Speech Haitian Creole URLs
LICENSE_URL = "http://www.speech.cs.cmu.edu/haitian/COPYING"
WAV_TRANSCRIPTION = "http://www.speech.cs.cmu.edu/haitian/speech/data/cmu_haitian_speech/etc/txt.done.data"
WAV_FILE_TEMPLATE = "http://www.speech.cs.cmu.edu/haitian/speech/data/cmu_haitian_speech/wav/{wav_file}"

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

def download_cmu_speech_dataste():
    # download data license
    download_file(LICENSE_URL, "./other_datasets/cmu_speech_haitian_creole/LICENSE")

    transcriptions = get_file_from_url(WAV_TRANSCRIPTION).decode("utf-8").split('\n')

    for i, transcription in enumerate(transcriptions):
        line_parts = transcription.split('"')
        speaker_id = line_parts[0].replace("(", "").strip()
        transcription = line_parts[1].strip()
        download_file(WAV_FILE_TEMPLATE.format(wav_file=f"{speaker_id}.wav"), f"./other_datasets/cmu_speech_haitian_creole/{i}.wav")
        with open(f"./other_datasets/cmu_speech_haitian_creole/{i}.txt", "w") as f:
            f.write(transcription)
        with open(f"./other_datasets/cmu_speech_haitian_creole/{i}.metadata", "w") as f:
            f.write(f"speaker: {speaker_id}")