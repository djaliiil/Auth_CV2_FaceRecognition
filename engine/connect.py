import time
import numpy as np
import cv2
import sys, os
import pymongo
from take_photo import take_photo
import face_recognition
import gridfs
import base64, re
from PIL import Image
from io import BytesIO

import json
my_data=["Reading and writing files in python",78546]
with open("./jsonfile.json","w") as f:
    json.dump(my_data,f)
f.close()

print("-----------------------------------------")

img = take_photo("test")
unknown_picture = face_recognition.load_image_file(img)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["securite"]
mycol = mydb["user"]

match = False

cursor = list(mycol.find({}))
for doc in cursor:
    byte_data = base64.b64decode(doc["image"])
    image_data = BytesIO(byte_data)
    img = Image.open(image_data)
    img.save('photo.png', "PNG")    
    
    image = face_recognition.load_image_file('photo.png')
    face_locations = face_recognition.face_locations(image)
    my_face_encoding = face_recognition.face_encodings(image)[0]

    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

    if results[0] == True:
        print("It's a picture of me!")
        match = True
        print("\n C'est : " + str(doc["nom"]).upper() + " " + doc["prenom"] + "  !!!")
        break
    else:
        print("It's not a picture of me!")


sys.stdout.flush()
