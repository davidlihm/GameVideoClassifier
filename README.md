### 游戏视频标题分类器
基于 Naive Bayes theorem。
http://en.wikipedia.org/wiki/Naive_Bayes_classifier
目前只支持四款主流竞技游戏的标题分类
*************
Segment文件夹是某著名开源中文分词组件。
（ https://github.com/fxsjy/jieba ）
该文件夹中有自定义词典 gameDict.txt，可自行扩充。
使用此词典对游戏方面语句分词正确率会高一点。
*************
classifier.py 是主程序。
提供了三个 test case, 分别是三个不同游戏的视频标题。 
这三个视频都是5月18日晚上于优酷游戏首页上随机选取的。
实现了一个简单的 Naive Bayes Classifier ， 但代码结构很乱-_-||
*************
sqlite.py 是github上一个对 python-sqlite3 的 wrapper
( https://github.com/thegoleffect/sqlite3-python-wrapper )
*************
db.db 是一个 SQLite3 database。
内有一个表， 名为 word 
其中储存的是用几千个游戏视频标题训练出来的词频统计
可按表结构自行扩充




