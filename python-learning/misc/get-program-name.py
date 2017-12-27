# -*- coding: utf-8 -*-

import sys
import os
val = str(sys.argv[0])
print(os.path.dirname(sys.argv[0]))

path = 'main.qml'   # 加载的QML文件
curdir = os.path.dirname(sys.argv[0])
qmlfile = os.path.join(curdir,path)

print(qmlfile)