# ai-writing

这是AI辅助项目的后端2018-7

## Getting start

首先确认您使用 Python3 并已经安装了 conda 或者 virtualenv

```bash
git clone https://github.com/MasterFishfish/ai-writing.git
cd ai-writing/mysite
virtualenv venv # 假设您使用 virtualenv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
#### api 文档

###### 登录

请求http://xxx.xxxx.xxx/login进入登录页面

发送登录请求:

+ POST 	 {"userId": "xxxxxxx", "userpassword":"xxxxxx"}
+ url :  http://xxx.xxxx.xxx/login/do_login

	erver返回json格式信息:	 

	 登录成功:	{"state": "1"}
+ 登录失败:      {"state": "0"}

##### 登出

发出登出请求: 

+ http://xxx.xxxx.xxx/login/do_login
	 POST 	 {"userId": "xxxxxxx"}

server返回的json格式信息:

+ 登出成功:	{"state": "1"}
+ 登出失败:      {"state": "0"}

##### 注册

发出注册的请求:

+ http://xxx.xxxx.xxx/login/regist/
+ POST     {"userId": "xxxx", "userpassword":"xxxx", "username": "xx"}

server返回的json格式信息：

+ 注册成功:	{"state": "1"}
+ 注册失败:      {"state": "0"}

##### 搜索:

登录的前提下发出搜索请求:

+ http://xxx.xxxx.xxx/user/search/
+ POST     {"str": "(一段字符串)xxxxxxxxxxxxxxxxxxx"}

server返回的json格式信息:

+ {"result": 

  ​	[ 

  ​		{"keyword": "xxx",   "url": "xxx", "str": "xxxxxxxx"},

  ​	 	{"keyword": "xxx",   "url": "xxx", "str": "xxxxxxxx"},

  ​		{"keyword": "xxx",   "url": "xxx", "str": "xxxxxxxx"},

  ​	 ]

  }