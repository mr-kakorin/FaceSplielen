import sys
if len(sys.argv)>1:
    inputImage=sys.argv[1]
    inputJSON=sys.argv[0]
    print(inputImage)
else:
    print('что-то пошло не так')
