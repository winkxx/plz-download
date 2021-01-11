# plz-download
aria2 下载 + rclone 上传 = Github 离线下载

![example](https://raw.githubusercontent.com/ame-yu/plz-download/main/docs/example.gif)
# Useage
1. Fork这个项目, 点击项目workflow并启用（以下坚果云为例）
2. settings->Secrets 设置 RCLONE_CONF
    ```
    [NutStore]
    type = webdav
    url = https://dav.jianguoyun.com/dav/文件夹的名称
    vendor = other
    user = 你的用户名
    pass = 应用授权码（账户信息->安全选项->第三方应用管理）
    ```
3. 新建wiki页面NutStore(页面名称要和配置文件节点名称保持一致)
4. 每次要下载时编辑Wiki的NutStore页面写上下载地址并保存页面(可多行)

>[进阶指南](https://github.com/ame-yu/plz-download/tree/main/docs)

# Licence
本项目基于 GLWTPL (Good Luck With That Public License) 许可证开源。

This project under the [Good Luck With That Public License](https://github.com/me-shaon/GLWTPL)



