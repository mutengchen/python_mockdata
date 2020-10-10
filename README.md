###
上svn复制yolov4.weights到model文件夹中

#需要修改的配置
cfg/params_config.txt
{
    "host":"192.168.1.5",//redis_host,如果部署在本机，就是127.0.0.1
    "port":6379,
    "db":0,
    "password":"123456",
    "cam_status_url":"http://192.168.1.5:5004/api/state",//如果摄像头服务部署在本机的话，就是127.0.0.1
    "cam_config_url":"http://192.168.1.5:5004/api/config"//如果摄像头服务部署在本机的话，就是127.0.0.1
}

##安装依赖包
pip install -r requirements.txt

###下载yolov4.weights
svn://123.57.14.158/ai/big_files/yolov4.weights

###启动项目
python car_main.py

###后台运行
bash boot.sh

##初始化flask db



##启动调试页面
nohup python test_page.py &

###测试识别页面部署在5011端口,需要开启端口
http://xxx.xxx.xxx.xxx:5011/


