import os

import face_recognition as fr

KNOWN_IMAGE_PATH = '../Images/known_images'
UNKNOWN_IMAGE_PATH = '../Images/unknown_images'

class Person:
    def __init__(self, name):
        self.name = name
        self.unknown_image = None 
        self.unknown_encoding = None
        self.person_encoding = []
        self.face_encoding = []
        self.face_names = [name]

    def _load_images_locally(self):
        uiname = os.listdir(UNKNOWN_IMAGE_PATH)[0]
        uimage_path = os.path.abspath(os.path.join(UNKNOWN_IMAGE_PATH, uiname)) 
        
        self.unknown_image = fr.load_image_file(uimage_path)
        self.unknown_encoding = fr.face_encodings(self.unknown_image)[0]

        for image in os.listdir(KNOWN_IMAGE_PATH):
            known_image = os.path.abspath(os.path.join(KNOWN_IMAGE_PATH, image))
            person_image = fr.load_image_file(known_image)
            try:
                self.face_encoding.append(fr.face_encodings(person_image)[0])
            except IndexError:
                print('cant find face {}'.format(known_image))

    def face_detection(self):
        result = fr.compare_faces(self.face_encoding, self.unknown_encoding)
        return result

if __name__ == '__main__':
    person = Person('Mikhail Markov')
    person._load_images_locally()
    print(person.face_detection())
