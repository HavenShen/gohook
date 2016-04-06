gohook
===

> Python 使用 Tornado 框架实现 WebHook 自动部署 Git 项目

为了方便开发测试或项目部署至服务器不那么繁琐，搞一个自动部署的小轮子也是必要的。

小轮子需要涉及到 Coding 项目托管平台(也可以用 Github 平台)，Linux服务器的Nginx、Python( Tornado框架 )。

同时配置项目托管平台的个人私钥或项目公钥，保证 `git pull` 能直接拉取。

## 安装

1.下载或克隆此项目

```shell
git clone git@github.com:HavenShen/gohook.git
```

2.部署代码的服务器必须安装 Python 的 Tornado框架

```shell
pip install tornado
#或
easy_instal tornado
```

## 修改配置

1.修改 `main.py` 中 `file_path` 变量路径

```python
#希望自动部署项目路径
file_path = '/home/wwwroot/xxx'
```

2.配置 `Nginx` 的conf文件

```shell
# http 节点下增加
upstream frontends{
		server 127.0.0.1:8765;
	}
	
#增加 server 配置
server {
    listen 80;

    server_name xxx.xxx.com; #你的域名

    location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://frontends;
    }
}
```
在此可以重启下 Nginx


## 启动

1.运行tornado框架开启后台进程运行

```shell
#下面路径修改成你自己gohook存放目录文件夹用户组必须跟nginx一致
setsid python /home/wwwroot/gohook/main.py &
```

## 配置 Coding 项目 WebHook 

1.`url` 填你的域名 `http://xxx.xxx.com/gohook`

2.`token` 填 `gohook`

## 测试

1.本地于服务器自动部署的git项目中使用 git 提交更新一下代码

```shell
touch test.md
git add .
git commit -m "test gohook"
git push -u origin master 
```

2.查看服务器上自动部署的git项目中是否存在 `test.md`

done.
