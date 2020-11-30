# Flask_test

该项目通过python的Flask框架接收用户上传的服装图像，并通过TensorFlow的数据模型识别服装图像的类别，将结果返还给用户。再此期间，用户所上传的图像会被保存在NoSQL的数据库中。数据库部分通过则MongoDB实现。最后用docker进行部署。

Tensorflow:
通过将Tensorflow导入进python文件，实现调用Tensorflow的数据模型进行大数据分析。
Flask:
通过将Flask导入进python文件，实现面向用户之间的传输

下面是网页的图像：

![image](https://github.com/Darkat-X/Flask_test/blob/main/Img/%E5%9B%BE%E7%89%87%201.png)

返还的结果：

![image](https://github.com/Darkat-X/Flask_test/blob/main/Img/%E5%9B%BE%E7%89%87%202.png)

终端运行指令：

export FLASK_APP=filename

export FLASK_ENV=development

flask run

通过浏览器搜索 http://127.0.0.1:5000/ 即可进入页面
MongoDB:
在服务器运行期间，用户所上传的照片将会以BinaryArray的形式保存在基于MongoDB的NoSQL数据库中。

![image](https://github.com/Darkat-X/Flask_test/blob/main/Img/%E5%9B%BE%E7%89%87%203.png)

Docker:
首先创建DockerFile，然后基于DockerFile生成镜像。运行镜像以实现部署。

终端运行指令

docker build -t ImageName

docker run -it --rm -p 80:80 ImageName
