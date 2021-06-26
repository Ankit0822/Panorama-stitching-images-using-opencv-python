import cv2
import os
import numpy as np

# Give the direction, path name of the main folder
mainFolder = 'C:\Python Programs\OpenCv\panorama\images' 
# Get the list of folders that within main folder
myFloders = os.listdir(mainFolder)
print(myFloders)

# We will iterate through each folder
# We will retrieve their images

for folder in myFloders:
    # path of the images
    path = mainFolder+'/'+folder
    images =[] # list that contain all images
    myList = os.listdir(path) # retrieving all tha images name
    print(f'Total number of images detected {len(myList)}')
    # loop through all images and store into images list
    for imgN in myList:
        curImg = cv2.imread(f'{path}/{imgN}')
        # Resizing our images
        curImg = cv2.resize(curImg,(0,0),None,0.2,0.2)
        
        images.append(curImg)
        
    # Now executing stitching function
    stitcher = cv2.Stitcher_create()
    (status,result) = stitcher.stitch(images)
    print(result)
    if (status == cv2.STITCHER_OK):
        print('Panorama Generated')
        cv2.imshow(folder,result)
        cv2.waitKey(1)
        cv2.destroyAllWindows()
    else: 
        print('Panorama Generation unsuccessful')

cv2.waitKey(0)

