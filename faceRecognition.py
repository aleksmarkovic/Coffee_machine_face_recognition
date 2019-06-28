import cv2
import numpy as np
import os 
import yaml
import sys
import sqlite3
from sqlite3 import Error

users_dic = {}
user_counter = {}

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
 
    rows = cur.fetchall()
 
    for row in rows:
        users_dic.update({row[0]: row[1]})
        user_counter.update({row[0]: 0})
def main():
    database = "SQLite/database.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        # print("1. Query task by priority:")
        # select_task_by_priority(conn,1)
         select_all_tasks(conn) 
 
if __name__ == '__main__':
    main()



recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

recognized_user = ""

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

def faceReco():
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, -1) # Flip vertically
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
        faces = faceCascade.detectMultiScale( 
            gray,
            scaleFactor = 1.2,
            minNeighbors = 5,
            minSize = (int(minW), int(minH)),
        )

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            # Check if confidence is less them 100 ==> "0" is perfect match 
            if (confidence < 100):
                name = users_dic[id]
                if confidence <= 50:
                    user_counter[id] += 1
                if user_counter[id] >= 5:
                    #print("This is for sure ", users_dic[id])
                    return users_dic[id], id

                #print(id)
                confidence = "  {0}%".format(round(100 - confidence))
            else:
                name = "Unknown"
                confidence = "  {0}%".format(round(100 - confidence))
            
            cv2.putText(img, str(name), (x+5,y-5), font, 1, (255,255,255), 2)
            cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
        
        cv2.imshow('camera', img) 

        k = cv2.waitKey(10) & 0xff # Press 'ESC' to exit video
        if k == 27:
            break

recognized_user, ID = faceReco()

cam.release()
cv2.destroyAllWindows()

os.system("python3 coffeePicker.py " + str(ID) + " " + recognized_user)