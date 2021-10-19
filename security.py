import cv2
import dropbox
import time
import random

start_time = time.time()

def take_pictures():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True 
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.time()
        result = False
    return image_name
    print("snapshot taken....")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_pictures(image_name):
    access_token = "gvfewq957r79eqy4grbtuoaegpifv7t8grDDDDipuwhe"
    file_from = image_name
    file_to = "/testFolder/"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded!!")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_pictures()
            upload_pictures(name)

main()

