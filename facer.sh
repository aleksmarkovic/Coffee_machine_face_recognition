#!/bin/bash

while true; do
  echo Hello, choose one of the following:
  echo 1 - Record and train a face dataset
  echo 2 - Run the face recognizer and coffee picker
  echo Press any key to quit.
  read choice

  if [ $choice == "1" ]
  then
    python3 faceDataset.py
    python3 faceTraining.py
  elif [ $choice == "2" ]
  then
    python3 faceRecognition.py
  else
    echo End of program.
    exit
  fi
done
