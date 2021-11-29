import face_recognition
from take_photo import take_photo


image = face_recognition.load_image_file("me.jpg")
face_locations = face_recognition.face_locations(image)

my_face_encoding = face_recognition.face_encodings(image)[0]

# my_face_encoding now contains a universal 'encoding' of my facial features that can be compared to any other picture of a face!

img = take_photo()
unknown_picture = face_recognition.load_image_file(img)
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

# Now we can see the two face encodings are of the same person with `compare_faces`!

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("It's a picture of me!")
else:
    print("It's not a picture of me!")
