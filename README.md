Selenium在请求过程中，会传递一些特有的属性，某些网站通过检测这些属性，鉴别出Selenium并实现反爬。

有反爬，自然有反反爬！

本文利用**Chrome DevTools**协议，它允许客户检查和调试Chrome浏览器，使Selenium接管手动打开的Chrome浏览器，实现反反爬。

操作环境：
 - Ubuntu 18.04LTS 
 - Python 3.6 .8
 - Selenium 3.141.0 
 - Chrome 76.0.3809

### 1 将google-chrome添加到环境变量PATH中
在~/.profile文件下添加该语句
```bash
export PATH="$PATH:/usr/bin/google-chrome"
```

在Terminal中执行
```bash
source ~/.profile
```

### 2 启动Chrome
在终端中执行以下命令，打开Chrome浏览器
```bash
google-chrome --remote-debugging-port=9222 --user-data-dir="/tmp/SeleniumData"
```
- --remote-debugging-port=9222：指定启动端口9222，也可以指定别的端口，在Selenium中会用到
- --user-data-dir="/tmp/SeleniumData/"：指定浏览器数据存储目录

### 参考
<https://blog.csdn.net/weixin_42960354/article/details/101321783>
