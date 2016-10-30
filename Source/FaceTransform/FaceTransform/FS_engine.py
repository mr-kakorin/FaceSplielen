import sys
import json
import cv2
import os 
import numpy
import CutFaces as cf
import FaceTransform as tf
if len(sys.argv)>1:
    inputID=sys.argv[1]
    inputImageName=os.path.abspath(__file__+'/../../../../Destination/uploads/'+inputID)
    inputJSONName=os.path.abspath(__file__+'/../../../../Destination/json/'+inputID)
    print('success')
    cutImage, facecoord=cf.cutFace(inputImageName,inputJSONName)
    #cutImage = tf.GetTwoDimMatrix(cutImage);    

    #with open(inputID, 'wb') as outfile:
        #outjson = {}
        #outjson['img']=numpy.array_str(cutImage[0:80,0:80].flatten())
        #json.dump(outjson, outfile);
        #json.dump(list(cutImage.flatten()), outfile)
    FUCKED_FILE=open(os.path.abspath(__file__+'/../../../../Destination/results/'+inputID),'w')
    FUCKED_FILE.write(str(tf.GetTwoDimMatrix(cutImage)[0:10,0:10].flatten()))
    FUCKED_FILE.close();
    #cutImage, facecoord=cf.cutFace(inputImageName,inputJSONName)
    gmc=tf.GetMarksCoordinates(inputJSONName)
    gmc=tf.TransformMarkCoordinates(gmc,facecoord)
    k=0
    tf.TransformMarkCoordinates(gmc,facecoord)
    for key, value in gmc.items():
        if k == 0:
          tf.rotel(cutImage,value,30,k)
          tf.rotel(cutImage,value,30,k)
        else:
          tf.rotel(cutImage,value,30,k)
        k=k+1
    image = cv2.imread(inputImageName);
    h,w,c = cutImage.shape
    for i in range(facecoord[0],facecoord[0]+h):
        for j in range(facecoord[1],facecoord[1]+w):
            image[i,j]=cutImage[i-facecoord[0],j-facecoord[1]];    
    #outFile.close()
    cv2.imwrite(os.path.abspath(__file__+'../../../Destination/results/'+inputID+'_img'),image)
else:
    cutImage, facecoord=cf.cutFace('kor.jpg','jsonDesc.txt')
    #print(os.path.abspath(__file__+'/../../../../Destination/json/'))

    #outFile=open(os.path.abspath('FS_engine.py')+'/../../../../Destination/results/','w')
    #outFile.close()
    #print(os.path.abspath('FS_engine.py')+'/../../../Destination/uploads/')
    #close(outFile)
    #cutImage=cf.cutFace('../../../Destination/uploads/kor.jpg','jsonDesc.txt')
    #cv2.imwrite('../../../Destination/results/'+'result.jpg',cutImage)