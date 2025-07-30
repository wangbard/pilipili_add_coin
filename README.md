<p align="center">
  <img src="images/146-紫灵-08.png" width="800" alt="Centered image">
</p>

## warning 声明

1. 此脚本遵守 CC-BY-NC 4.0 协议，禁止一切商业使用，如需转载请注明作者 ID
2. **请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！请勿滥用，本项目仅用于学习和测试！**
3. 利用本项目造成不良影响及后果与本人无关
4. 本项目为开源项目，不接受任何形式的催单和索取行为，更不容许存在付费内容
5. **上传任何信息时请注意脱敏，删去账户密码、敏感 cookies 等可能泄漏个人信息的数据（例如 `SESSDATA`、`bili_jct` 之类的 cookies）**

## 使用方法
只需要修改`pilipili_add_coin.py`中`cookie`部分。可以通过浏览器开发者工具获取自己的cookie：

✅ 获取 cookie 的步骤如下：
1. 打开bilibili官网并登陆
2. 按`F12`打开开发者工具
3. 选择顶部菜单栏中的网络（Network）
4. 任意点开一个请求，向下翻动找到`cookie`
5. 在cookie中寻找对应的名称的字段，即 buvid3，bili_jct 和 SESSDATA，并填入对应位置

📌 注意：cookie 有时效性，如果提示失败，请重新获取。

## 鸣谢
感谢[bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect/tree/master)提供的api检索大全
