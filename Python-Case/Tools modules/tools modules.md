#包管理工具
## 安装 pip(python 版本要大于等于 2.7)
1. 打开 https://pip.pypa.io/en/latest/installing/ 把 "get-pip.py" 右键另存为下载下来
2. python get-pip.py (get-pip.py also installs setuptools and wheel if they are not already)
3. 添加 python 目录下的 Scripts 文件夹路径到环境变量

## distribute, setuptools, easy_install 与 pip 的发展历程
http://lib.csdn.net/article/python/1487 

# MySQL
1. pip install mysqlclient
2. 未装 pip, https://pypi.python.org/pypi/MySQL-python/1.2.5#downloads
同理可在 https://pypi.python.org/packages 搜索 mysql-connector 关键词

出现2019错误:Can't initialize character set utf-8: conn 的 charset 由 utf-8 改为 utf8. 似乎是 python 版本识别问题

DLL load failed: %1 is not a valid Win32 application: MySQL DB 用 32 位, 不用 64 位；或者使用 pymysql (通过 pip 安装)

Module 'MySQLdb' has no 'Error' member: https://stackoverflow.com/questions/43907094/how-do-i-get-pylint-to-recognize-mysqldb-members

# Lint
pylint guide: https://www.mantidproject.org/How_to_run_Pylint#Summary  https://pylint.readthedocs.io/en/latest/index.html

# 第三方
## Git
https://www.cnblogs.com/superjt/p/5977719.html
## Reg
http://www.jb51.net/tools/zhengze.html
