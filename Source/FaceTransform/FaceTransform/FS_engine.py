import sys
import json
import cv2
import os 
import CutFaces as cf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName=__file__+'/../../../Destination/uploads/'+inputID
    inputJSONName=__file__+'/../../../Destination/json/'+inputID
    print('success')
    cutImage=cf.cutFace(inputImageName,inputJSONName)

    outFile=open(__file__+'/../../../Destination/results/'+inputID,'w')
    outFile.write(json.dumps(cutImage.flatten()))
    outFile.close()
    #cv2.imwrite('../../../Destination/results/'+inputID,cutImage)
else:
    print(__file__)
    #outFile=open(os.path.abspath('FS_engine.py')+'/../../../../Destination/results/','w')
    #outFile.close()
    #print(os.path.abspath('FS_engine.py')+'/../../../Destination/uploads/')
    #close(outFile)
    #cutImage=cf.cutFace('../../../Destination/uploads/kor.jpg','jsonDesc.txt')
    #cv2.imwrite('../../../Destination/results/'+'result.jpg',cutImage)