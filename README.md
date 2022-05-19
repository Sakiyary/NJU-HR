# NJU-HR

![](https://img.shields.io/badge/language-python-brightgreen)

## 🌀 简介
NJU-HR 可以帮您自动进行每日健康打卡.

## ❗ 协议
使用 NJU-HR 即表明，您知情并同意：

- 本项目仅供学习交流使用. 代码通过模拟浏览器使用 Cookie 登录. 开发者对项目造成产生的后果不负任何责任, 也不保证本方案一直有效. 请使用者对自己负责.
- 使用前须将项目 Fork 至自己的仓库, 此时 `Secret` 只有自己才知道. 
- 用户的 Cookie 被储存于 Github 服务器, 只供本项目使用. 若 Github 服务器被攻破, 则您的 Cookie 有遭到泄露的风险. 除此之外, 开发者无权获取您的 Cookie; 即使是用户, 一旦创建完成Secrets, 也无法再次从中查看 Cookie.

## 📐 部署

1. 将本项目 Fork 到自己的仓库.
2. 进入 `Settings` 选项, 点击 `Secret`, 并选择 `New Repository Secret`. 依次添加以下变量:
   - `USERNAME`: 学号.
   - `LOCATION`: 你希望打卡的地理位置。比如南京大学仙林校区可以填 `中国江苏省南京市栖霞区九乡河东路`.
   - `COOKIE`: 使用电脑端 Chrome/Edge 打开[该网址](https://authserver.nju.edu.cn/authserver/login?service=https%3A%2F%2Fauthserver.nju.edu.cn%2Fauthserver%2Fmobile%2Fcallback%3FappId%3D301317066&login_type=mobileLogin), 成功登录后重新启动该网页, 按 `F12` 进入开发者模式, 选择 `网络`, 刷新页面, 点击抓取到的 `default.html`, 查看标头中 `Cookie:` 部分, 将 `CASTGC=` 之后的代码复制进该变量. 样例为 "TGT-xxxx-xxxx-xxxx-cas".
   - `USERAGENT`: 使用手机端 Chrome/Edge, 输入网址 about:version (注意为半角冒号), 查看`用户代理`/`User-Agent:` 部分, 在末尾加上 "cpdaily/9.0.15", 并复制进该变量. 样例为 "Mozilla/5.0 (Linux; Android xx; xxxx) AppleWebkit/xxxx(xxxx) Chrome/xxxx Mobile Safari/xxxx cpdaily/9.0.15".
3. 回到 `Action` 选项卡, 重新运行 Action，或者静待自动打卡.

## 🔍 结果

1. 设置`您的体温是否正常`为`正常`.
2. 设置`您的其他健康情况`为`正常`.
3. 设置`您今日苏康码显示颜色`为`绿色`.
4. 设置`您的共同居住人今日苏康码显示颜色`为`绿色`.
5. 设置`最近14天是否离宁`为`否`.
6. 设置`您的最近一次核酸检测时间`默认为常态化核酸检测时间.
7. 设置`填报地址`为 `LOCATION` 项.