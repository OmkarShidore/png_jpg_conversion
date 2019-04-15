#Developed by OmkarShidore
#github: https://github.com/OmkarShidore

"""
    Setup:
        pip install opencv-python
"""

import cv2 as cv
import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
createFolder('./output_jpg/')
createFolder('./output_png/')
list1=os.listdir("source")
list2=[]
for name in list1:
    list2.append(''.join(name.split('.')[:-1]))
def img_to_jpg():
    i=0
    for name in list1:
        input_name=name
        img = cv.imread('source\\'+input_name,1)
        print(input_name)
        outpath_jpg='output_jpg\\'+list2[i]+'.jpg'
        cv.imwrite(outpath_jpg,img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        i+=1
def img_to_png():
    f=0
    for name in list1:
        input_name=name
        img = cv.imread('source\\'+input_name,1)
        print(input_name)
        outpath_png='output_png\\'+list2[f]+'.png'
        cv.imwrite(outpath_png,img)
        cv.waitKey(0)
        cv.destroyAllWindows()
        f+=1
print("------------------------------------------------")
print("Starting Conversion.")
print("-------------------------------------------------")
img_to_jpg()
img_to_png()
print("------------------------------------------------")
print("Image Conversion done, Check the Output folders.")
print("-------------------------------------------------")