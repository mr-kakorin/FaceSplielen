import sys
import cv2
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImage=cv2.imread('../../../Destination/uploads/'+inputID)
    print('success')
else:
    inputImage=cv2.imread('../../../Destination/uploads/kor.jpg')
    

