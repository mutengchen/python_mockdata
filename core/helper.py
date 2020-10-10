import os

import cv2
from PIL.Image import Image
from flask import url_for
import numpy as np
from core.settings import Setting as ST
BASEDIR = 'tmp'

def save_buf_to_img(imgbuf,cameraname):
    img = cv2.imdecode(np.asarray(bytearray(imgbuf), dtype='uint8'), cv2.IMREAD_COLOR)
    imgname = f"{cameraname}.jpg"
    path = os.path.join(ST.SERVERSTATICROOT, BASEDIR, imgname)
    print("save_tem_img",path)
    cv2.imwrite(path, img,[cv2.IMWRITE_JPEG_QUALITY,60])
    return url_for('static', filename=f"{BASEDIR}/{imgname}")

def save_path_to_img(img,imagename):
    cv2.imwrite(os.path.join(ST.SERVERSTATICROOT,BASEDIR, imagename), img)
    return url_for('static', filename=f"{BASEDIR}/{imagename}")
