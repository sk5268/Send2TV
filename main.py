import requests
import glob
import time
import os

url = 'http://192.168.1.33:8080/upload.html?path=/storage/48AC-1D06/Android/data/'

ts = time.time()

files = glob.glob('*.mp4')
files.sort()

for file_path in files:

    t1 = time.time()

    with open(file_path, 'rb') as video_file:
        files = {
            'file': (file_path, video_file, 'video/mkv')
        }

        size = os.path.getsize(file_path)
        size /= 1024
        size /= 1024
        
        response = requests.post(url, files=files)

        if response.status_code == 200:
            t2 = time.time()
            print(file_path, ' Uploaded')
            m = int((t2-t1)/60)
            print('Time: ', m, ' minutes ', t2-t1 - m*60, " seconds")
            print("Average Speed: ", size/(t2-t1), " MB/s")
            print()

        else:
            print(f'Failed to upload, status code: {response.status_code}')

te = time.time()
m = int(te-ts/60)
print('Time: ', m, ' minutes ', te-ts - m*60, " seconds")
print("Overall Average Speed: ", size/(te-ts), " MB/s")