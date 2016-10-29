import sys
import json
import cv2
import CutFaces as cf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName='../../../Destination/uploads/'+inputID
    inputJSONName='../../../Destination/json/'+inputID
    print('success')
    cutImage=cf.cutFace(inputImageName,inputJSONName)

    outFile=open('../../../Destination/results/'+inputID,'w')
    outFile.write(json.dumps(cutImage.flatten()))
    outFile.close()
    #cv2.imwrite('../../../Destination/results/'+inputID,cutImage)
else:
    li=[1,2,3]
    outFile=open('../../../Destination/results/123','w')
    outFile.write(json.dumps(li))
    outFile.close()
    #close(outFile)
    #cutImage=cf.cutFace('../../../Destination/uploads/kor.jpg','jsonDesc.txt')
    #cv2.imwrite('../../../Destination/results/'+'result.jpg',cutImage)