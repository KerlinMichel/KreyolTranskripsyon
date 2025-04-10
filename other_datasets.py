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