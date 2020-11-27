import pickle
import face_recognition
import os

known_encodings = []
known_names = []

known_faces_dir = "KNOWN_FACES"

print("De gezichten herkennen en opslaan...")


for name in os.listdir(known_faces_dir):

    for filename in os.listdir(f"{known_faces_dir}/{name}"):

        print(name)
        print(filename)

        
        try:
            image = face_recognition.load_image_file(f"{known_faces_dir}/{name}/{filename}")
        
            encoding = face_recognition.face_encodings(image)[0]

            known_encodings.append(encoding)
            known_names.append(name)
        except:
            print("Gezicht is niet herkend, doorgaan naar volgende foto...")
            break
        



pickle.dump(known_encodings, open("encodings.p", mode='wb'))
pickle.dump(known_names, open("names.p", mode='wb'))

print("Gezichten opgeslagen!")