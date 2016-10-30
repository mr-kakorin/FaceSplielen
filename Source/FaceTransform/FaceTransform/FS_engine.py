import sys
import json
import cv2
import os 
import CutFaces as cf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName=os.path.abspath(__file__+'/../../../../Destination/uploads/'+inputID)
    inputJSONName=os.path.abspath(__file__+'/../../../../Destination/json/'+inputID)
    print('success')
    cutImage=cf.cutFace(inputImageName,inputJSONName)

    outFile=open(os.path.abspath(__file__+'/../../../../Destination/results/'+inputID,'w'))
    with open(inputID, 'wb') as outfile:
        json.dump(cutImage.flatten(), outfile)
    #outFile.close()
    #cv2.imwrite('../../../Destination/results/'+inputID,cutImage)
else:
    print(os.path.abspath(__file__+'/../../../../Destination/json/'))
    #outFile=open(os.path.abspath('FS_engine.py')+'/../../../../Destination/results/','w')
    #outFile.close()
    #print(os.path.abspath('FS_engine.py')+'/../../../Destination/uploads/')
    #close(outFile)
    #cutImage=cf.cutFace('../../../Destination/uploads/kor.jpg','jsonDesc.txt')
    #cv2.imwrite('../../../Destination/results/'+'result.jpg',cutImage)