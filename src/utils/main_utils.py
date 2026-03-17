import requests
import re 

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hTqGqoC-LrW6S79HjuJUkg/trimmed-02.wav"

def download_file(url=url):
    response = requests.get(url)
    audio_file_path = "sample-meeting.wav"

    if response.status_code == 200:
        with open(audio_file_path,"wb") as file:
            file.write(response.content)
            print("File downloaded successfully")
    else: 
        print("failed to donwload file")

def remove_fillers(text):
    fillers = ["um","uh","like","you know","basically","actually"]
    for word in fillers:
        text = text.replace(word,"")
    return text

def remove_non_ascii(text):
    return ''.join(char for char in text if ord(char) < 128)

def clean_transcript(text):
    text = remove_non_ascii(text)
    text = remove_fillers(text)
    text = re.sub(r'\s+',' ',text)
    return text.strip()

# if __name__ == "__main__":
#     download_file()