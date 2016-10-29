import sys
import cv2
import CutFaces as cf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName='../../../Destination/uploads/'+inputID
    inputJSONName='../../../Destination/json/'+inputID
    print('success')
    cutImage=cf.cutFace(inputImageName,inputJSONName)
    cv2.imwrite('../../../Destination/results/'+inputID,cutImage)
else:
    cutImage=cf.cutFace('../../../Destination/uploads/kor.jpg','jsonDesc.txt')
    cv2.imwrite('../../../Destination/results/'+'result.jpg',cutImage)