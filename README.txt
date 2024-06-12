一、概述
这是一个获取微博帖子评论的爬虫。

二、依赖
详见requirements.txt
终端安装:pip install -r requirements.txt

三、模块介绍
1、crawl模块主要存储爬取配置cookie以及headers信息
详细查看:help(Crawl)
2、extract模块主要存储数据解析函数
详细查看:help(Extract)
3、store模块主要存储数据保存函数，包含mysql存储
详细查看:help(Store)
4、main模块为项目主要流程模块，包含实际业务逻辑，可自行布置

四、说明
1、crawl中setting设置
打开F12工具，定位json数据或是文档数据，复制curl
打开网页https://curlconverter.com/，获取cookie及headers
2、store中修改mysql的密码
