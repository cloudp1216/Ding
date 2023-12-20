

#### 一、利用钉钉接口实现告警消息推送，结构如下
```shell

    [ding 1]       |                                             | [用户1] 
    [ding-robot]   |    ->  [ding-proxy]  ->  [钉钉API]  ->      | [钉钉机器人]
    [ding 2]       |                                             | [用户1|用户2]
     ...                                                            ...
```


#### 二、ding-proxy应用部署

##### 1、部署ding-proxy
```shell
cd /usr/local
git clone https://github.com/cloudp1216/Ding.git
```
 
##### 2、安装python3及依赖环境：flask、flask-restful、uwsgi、requests
```shell
cd /usr/local/Ding/ding-proxy
pip3 install -r requirements.txt
```

##### 3、添加钉钉后台应用，修改配置文件：/usr/local/Ding/ding-proxy/config.json

##### 4、启动服务：
```shell           
cd /usr/local/Ding/ding-proxy && uwsgi uwsgi.ini
```           


#### 三、接口信息
```shell
http://x.x.x.x:8008/
POST:
{
    "users_id":    // 用户id，对应钉钉后台实际用户UserID，多用户使用"|"分割，在配置文件/usr/local/Ding/ding-proxy/config.json中定义
    "messages":    // 推送给用户的报警消息
}
```
```shell
http://x.x.x.x:8008/robot
POST:
{
    "messages":    // 推送给钉钉机器人的报警消息，可以在群设置里添加机器人，在config.json设置webhook
}
```


#### 四、客户端使用
##### 1、调整代理接口：
```shell
vi /usr/local/Ding/ding/config.py

# ding proxy 代理接口
DingProxy = "http://127.0.0.1:8008"

```

##### 2、ding：
```shell
ln -sv /usr/local/Ding/ding/ding.py /usr/bin/ding
ding <用户id> <第一行消息> <第二行消息> ...
```

##### 3、ding-robot
```shell
ln -sv /usr/local/Ding/ding/ding-robot.py /usr/bin/ding-robot
ding-robot <第一行消息> <第二行消息> ...
```


