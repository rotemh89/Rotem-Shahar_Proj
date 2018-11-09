from random import randint
import cv2
import sys
import os
import numpy as np

CASCADE = "haarcascade_frontalface_default.xml"
FACE_CASCADE = cv2.CascadeClassifier(CASCADE)


def detect_faces(image_path):
    image = cv2.imread(image_path)
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(image_grey, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25), flags=0)

    for x, y, w, h in faces:
        sub_img = image[y - 10:y + h + 10, x - 10:x + w + 10]
        #os.chdir("Extracted")
        sub_image_grey = cv2.cvtColor(sub_img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("extract_" + str(sys.argv[1]), sub_image_grey)
        print(np.mean(sub_image_grey))
        #os.chdir("../")
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Faces Found", image)
    if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
        cv2.destroyAllWindows()


if __name__ == "__main__":

    #if not "Extracted" in os.listdir("."):
        #os.mkdir("Extracted")

    if len(sys.argv) < 2:
        print("Usage: python Detect_face.py 'image path'")
        sys.exit()

    detect_faces(sys.argv[1])