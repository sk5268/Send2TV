import requests
import glob
import time

url = 'http://192.168.1.36:8080/upload.html?path=/storage/48AC-1D06/Android/data/'

ts = time.time()

files = glob.glob('*.mkv')
files.sort()

for file_path in files:

    t1 = time.time()

    with open(file_path, 'rb') as video_file:
        files = {
            'file': (file_path, video_file, 'video/mkv')
        }

        
        response = requests.post(url, files=files)

        if response.status_code == 200:
            t2 = time.time()
            print(file_path, ' Uploaded')
            print('Time: ', (t2-t1)/60, ' minutes')
            print()

        else:
            print(f'Failed to upload, status code: {response.status_code}')

te = time.time()
print('Total Time: ', (te-ts)/60 , ' minutes')