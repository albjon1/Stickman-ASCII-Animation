import os
import time
os.system('cls')
fileNames = ["frame_1", "frame_2",
             "frame_3", "frame_4",
             "frame_5", "frame_6",
             "frame_7", "frame_8",
             "frame_9", "frame_10",
             "frame_11", "frame_12",
             "frame_13", "frame_14",
             "frame_15", "frame_16",
             "frame_17", "frame_18"]
framesList = []

for name in fileNames:
    with open(name, "r", encoding ="utf8") as f:
        framesList.append(f.readlines())
for i in range(10):
    for frame in framesList:
        print("".join(frame))
        time.sleep(0.2)
        os.system('cls')
