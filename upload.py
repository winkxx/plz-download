# -*- coding:utf-8 -*-
import os
from webdav3.client import Client

driver_prefix = os.getenv("driver")

if driver_prefix==None or driver_prefix=="Home":
    print("请先新建Wiki页面，详情请参考项目Readme!")
    exit(-1)

driver_prefix = driver_prefix[:-3]

webdav_url = os.getenv(f"{driver_prefix}_url")
webdav_username = os.getenv(f"{driver_prefix}_username")
webdav_password = os.getenv(f"{driver_prefix}_password")

if webdav_username==None or webdav_username=="" or webdav_password==None or webdav_password=="":
    print(f"{driver_prefix}_username 或 {driver_prefix}_password 没有配置secret")
    exit(-1)

options = {
 'webdav_hostname': webdav_url,
 'webdav_login':    webdav_username,
 'webdav_password': webdav_password,
 'disable_check': True
}

client = Client(options)

os.chdir("download")

for it in os.listdir():
    if os.path.isfile(it):
        client.upload(remote_path=it,local_path=it)

print("✨ All file uploaded")