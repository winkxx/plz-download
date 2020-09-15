# plz-download
Github Action 离线下载到支持WebDAV的网盘

Using github action download resource then upload to netdisk.

![preview](https://raw.githubusercontent.com/ame-yu/plz-download/master/docs/preview.gif)

# 用途？
为代码、发行包做离线下载。

请勿滥用Github资源，谢谢🙏🏻
# 使用？
1. Fork这个项目, 点击项目workflow并启用（以下坚果云为例）
2. settings->Secrets 
    - nutstore_url: DAV目录 e.g.https://dav.jianguoyun.com/dav/download
    - nutstore_username 用户名
    - nutstore_password 密码
3. 新建wiki页面nutstore
4. 每次要下载时编辑Wiki的nutstore页面写上下载地址并保存页面(可多行)
5. 稍后前往网盘下载
> nutstore可以替换为box、yandex，如果是自建网盘或其他网盘请参照[添加指南](https://github.com/ame-yu/plz-download/tree/master/docs) <br>
> 添加后不同wiki页面填写会下载到不同的网盘<br>

### Tips 
本质上使用了wget,所以遇到不包含文件名的下载链接可以考虑重命名来避免错误
```bash
"https://xxxxxx.com/download?123*(#*&^!*&#" -O download/修改这里的文件名
```


