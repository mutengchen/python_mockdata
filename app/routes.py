import base64
import json
import os
import random
import sys
import uuid

import requests
from flask import (Blueprint, render_template, request, jsonify)
from werkzeug.routing import Rule


from core.helper import  save_buf_to_img, save_path_to_img

frontend = Blueprint("frontend", __name__,static_folder='static',
               template_folder='templates')
# 启动的时候初始化一次识别模型和数据集标签的设置
@frontend.route("/", methods=["GET", "POST"])
def index():
    return ""
    # 获取当前本地redis服务器的帧
    # redis_cam_frame = dict()
    # config = {"socre_thr": 0.35, "fps": 2, "cam_count": 8, "camera_pre": "cm:v1:", "output_url": ""}
    # # 读取redis配置
    # config_path = os.path.join(os.path.abspath('.'), 'cfg','params_config')
    # print(config_path)
    # file = open(config_path, 'r')
    # content = file.read()
    # params_config = json.loads(content)
    # print("params_config",params_config)
    # # 获取api/config配置项
    # try:
    #     res = requests.get(params_config['cam_config_url'])
    #     config = res.json()
    #     print(config)
    # except Exception as e:
    #     print("获取配置连接超时,程序退出",e.args)
    #     sys.exit(-1)
    # # 连接redis
    # print(params_config)
    # # pool = redis.ConnectionPool(host=params_config['redis_host'], port=params_config['redis_port'],
    # #                             db=params_config['redis_db'], password=params_config['redis_password'],
    # #                             socket_connect_timeout=30)
    # # r = redis.Redis(connection_pool=pool)
    # # 获取摄像头状态配置
    # try:
    #     cam_status = requests.get(params_config["cam_status_url"]).json()
    #     cam_status = cam_status["camerasstate"]
    # except Exception as e:
    #     print(e.args)
    # # 开始拿图片了
    # for i in range(1,config["cam_count"]+1):
    #     input_key = config["camera_pre"] + str(i)
    #     try:
    #         json_bytes = r.lindex(input_key, 0)
    #         if json_bytes == None:
    #             redis_cam_frame[i] = {}
    #             continue
    #
    #     except Exception as e:
    #         # 如果报错，去检查redis是否连接上
    #         print("redis error:", e.args)
    #         continue
    #         # 转换json
    #     json_str = str(json_bytes, "utf-8")
    #     res = json.loads(json_str)
    #     buf = base64.b64decode(res['frame'])
    #
    #     if buf==None or len(buf)<=0:
    #         continue
    #     redis_cam_frame[i] = {'cam_id': i, 'image_url': save_buf_to_img(buf, str(i) + "_1")}
    #     print(redis_cam_frame)
    # return render_template("index.html", capture_list=redis_cam_frame,
    #                        config_info=params_config, config_api_res=config, cam_status=cam_status
    #                        )



@frontend.route("/upload",methods=["POST"])
def upload():
    print("已经调用了upload接口，上传图片")
    file = request.files['file']
    file_path = uuid.uuid4().hex+".jpg"
    tmp_path = os.path.join("tmp",file_path)
    print(tmp_path)
    if file:
        file.save(tmp_path)
    return jsonify({'status': '0', 'msg':"上传成功",'filename':file_path })

@frontend.route("/rec_page")
def recPage():
    return render_template("rec_page.html")

@frontend.route("/recognize",methods=["POST"])
def commit_recognize():
    print("filelist = ",request.form['filelist'])
    res = json.loads(request.form['filelist'])
    print(len(res))

    result_img = []
    rs = []
    # for i in res:
    #     temp_save_path = os.path.join("tmp",str(i))
    #     img = cv2.imread(temp_save_path)
    #     rs = model.detect_img(img)
    #     # rs=[]
    #     for item in rs:
    #         cv2.rectangle(img,(item[0],item[1]),(item[2],item[3]),(0,0,255),4)
    #     aa = save_path_to_img(img,"res_"+str(i))
    #     os.remove(temp_save_path)
    #     result_img.append(aa)
    #     print("bboxes", rs)
    return render_template("recognize_result.html",info=result_img)



@frontend.route("/result")
def result():
    return render_template("recognize_result.html")