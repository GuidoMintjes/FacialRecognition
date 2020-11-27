import face_recognition
from cv2 import cv2
import os
import numpy as np
import pickle


video_capture = cv2.VideoCapture(0)


print("Gezichten aan het inladen...")
known_encodings = pickle.load(open("encodings.p", mode='rb'))
known_names = pickle.load(open("names.p", mode='rb'))
print("Gezichten zijn ingeladen!")


fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
vidWidth = video_capture.get(3)
vidHeight = video_capture.get(4)
fps = video_capture.get(5)
print(vidWidth, vidHeight, fps)

out = cv2.VideoWriter("video_capture.avi",
                        fourcc, 
                        fps, 
                        (int(vidWidth), int(vidHeight)))


face_locations =[]
face_encodings = []
face_names = []
process_this_frame = True

tolerance = 0.5


while True:

    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    for(top, right, bottom, left), name in zip(face_locations, face_names):

        top *= 4
        bottom *= 4
        left *= 4
        right *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 200), 2)

        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 200), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    # out.write(cv2.resize(frame, (int(vidWidth), int(vidHeight))))

    if cv2.waitKey(1) & 0xFF == ord('Q'):
        print("Gestopt!")

        break

video_capture.release()
cv2.destroyAllWindows()

out.release()