from os import listdir
from os.path import isfile, join
import cv2
import time
def ls(ruta = ''): #No modificar esto
    arreglo= [arch for arch in listdir(ruta) if isfile(join(ruta,arch))]
    return arreglo



valor=(ls(r'Videos/')) #Ruta donde estan todos los videos, tampoco modificar
nuevoSet=[]



for v in valor :
    print('Tomando capturas del video: ' + v) #Para cada uno de los videos
    cap = cv2.VideoCapture('Videos/' +v)
    i = 1
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    while (cap.isOpened()):
        ret, frame = cap.read()

        if ret == False:
            break
        #if i % 180 == 0:
        if i % (1 * fps) == 0: #Cada cuantos fotogramas o frames va a tomar una captura 1 frame = 1 ms en este caso, 5 frames es 5 segundos

            cv2.imwrite(r'ImagenesFord/' + str(time.time_ns()) + '.jpg', frame)

        i += 1
    cap.release()
    cv2.destroyAllWindows()
