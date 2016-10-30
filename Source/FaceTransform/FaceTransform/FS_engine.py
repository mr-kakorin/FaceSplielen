import sys
import json
import cv2
import os 
import numpy
import CutFaces as cf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName=os.path.abspath(__file__+'/../../../../Destination/uploads/'+inputID)
    inputJSONName=os.path.abspath(__file__+'/../../../../Destination/json/'+inputID)
    print('success')
    cutImage, tmp=cf.cutFace(inputImageName,inputJSONName)
    cutImage = cf.GetGrayScaleImg(cutImage);
    cutmage = cv2.resize(cutImage,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_CUBIC)

    with open(inputID, 'wb') as outfile:
        outjson = {}
        outjson['img']=numpy.array_str(cutImage)
        json.dump(outjson, outfile);
        #json.dump(list(cutImage.flatten()), outfile)
    FUCKED_FILE=open(os.path.abspath(__file__+'/../../../../Destination/results/'+inputID),'w')
    FUCKED_FILE.write(str(list(cutImage.flatten())))
    FUCKED_FILE.close();
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