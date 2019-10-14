# 一、项目简介

该项目实现的是一个聊天室, 具备聊天室的基本功能, 
旨在实现多人交流与私人之间的交流, 满足基本的沟通需求

### 项目功能简介

- 注册与登录功能 (登录校验)
- 显示聊天室当前在线人数
- 公共聊天室 (群聊功能)
- 私聊 (一对一聊天功能)
- 发送语音与图片消息
- 聊天记录存储与聊天记录查询 (未实现)
- 语音消息 AI 对话功能
- 文字消息 AI 对话功能 (未实现)

### 项目使用方式简介

1. 启动后端服务器 (运行 app.py, ws_server.py)
2. 启动 MongoDB
3. 浏览器登入注册页面进行注册 (127.0.0.1:9527/reg) 注册成功后跳转到登录页面
4. 或者浏览器登入登录页面直接进行登录 (127.0.0.1:9527/login) 登录成功后跳转到聊天室页面
5. 聊天室页面大致分为语音操作板块, 文字操作板块, 图片操作板块, 消息展示板块
    1. 语音操作板块可以实现发送语音消息以及实现语音消息 AI 对话功能
    2. 文字操作板块分为群聊板块和私聊板块
        1. 群聊板块可以直接进行发送消息, 输入消息点击发送即可
        2. 私聊板块需要指定接收方, 之后输入消息点击发送即可 (需要确保接收方在线)
    3. 图片操作板块可以上传图片, 实现发送图片消息
    4. 消息展示板块也分为群聊板块和私聊板块, 分别展示群聊消息和私聊消息
    - 注： 无论文字消息， 图片消息还是语音消息都需要通过唯一的发送按钮进行发送