

#### 一、利用钉钉接口实现告警消息推送，结构如下
```shell

    [ding]       |                                             | [用户1] 
    [ding-robot] |    ->  [ding-proxy]  ->  [钉钉API]  ->      | [钉钉机器人]
    [ding]       |                                             | [用户1|用户2]
    ...                                                          ...
```


#### 二、ding-proxy应用部署

##### 1、需要安装python3及依赖环境：flask、flask-restful、uwsgi、requests
       
##### 2、部署ding-proxy
```shell
cd /usr/local
git clone https://github.com/cloudp1216/Ding.git
```
 
##### 3、根据钉钉后台及应用，修改配置文件：/usr/local/Ding/ding-proxy/config.conf

##### 4、启动服务：
```shell           
cd /usr/local/Ding/ding-proxy && uwsgi uwsgi.ini
```           


#### 三、接口信息
```shell
http://x.x.x.x:8008/
POST:
{
    "users_id":    // 用户id，在配置文件/usr/local/Ding/ding-proxy/config.conf中定义，多用户使用"|"分割
    "messages":    // 推送给用户的报警消息
}
```
```shell
http://x.x.x.x:8008/robot
POST:
{
    "messages":    // 推送给机器人的报警消息，可以在群设置里添加机器人，在config.json设置webhook
}
```


#### 四、客户端
##### 1、ding：
```shell
ding <用户id> <第一行消息> <第二行消息> ...
```


##### 2、ding-robot
```shell
ding-robot <第一行消息> <第二行消息> ...
```

