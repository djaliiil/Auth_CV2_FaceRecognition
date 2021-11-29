import tensorflow
import sys, os
import pymongo
from take_photo import take_photo
import gridfs
import base64

nom = str(sys.argv[1])
prenom = str(sys.argv[2])
naissance = str(sys.argv[3])
email = str(sys.argv[4])
sexe = str(sys.argv[5])
path = str(os.getcwd()) + "\\images"

img = take_photo(prenom)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["securite"]
mycol = mydb["user"]

with open(img, "rb") as imageFile:
    str_img = base64.b64encode(imageFile.read())

mydict = { "nom": nom,
            "prenom": prenom,
            "naissance": naissance,
            "email": email,
            "sexe": sexe,
            "image": str_img }

x = mycol.insert_one(mydict)



print("------------",x,"-------------")
