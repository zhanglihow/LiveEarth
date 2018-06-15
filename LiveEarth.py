import json
import os
import time
import urllib.request
import win32api
import win32con
import win32gui
from urllib import request

base_url = "http://himawari8-dl.nict.go.jp/himawari8/img/D531106/1d/550/"  # 官网图片地址前半部分

cwd = os.getcwd()  # 当前目录


def set_desktop(pic_path):
    k = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(k, "WallpaperStyle", 0, win32con.REG_SZ, "0.5")  # 2拉伸适应桌面,0桌面居中
    win32api.RegSetValueEx(k, "TileWallpaper", 0, win32con.REG_SZ, "0")
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic_path, 1 + 2)


# 获取当前图片url
# http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json?uid=时间戳 获取最新的图片时间
def getPic_url():
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    url='http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json?uid='+str(int(round(time.time() * 1000)))
    req = request.Request(url=url, headers=header_dict)
    res = request.urlopen(req)
    res_json = json.loads(res.read())
    date = res_json["date"]
    hour_url = time.strftime("%Y/%m/%d/%H%M%S", time.strptime(date, "%Y-%m-%d %H:%M:%S"))
    pic_url = base_url + "/" + hour_url + "_0_0.png"
    print(pic_url)
    return pic_url


# 下载图片
def down_pic(pic_url):
    conn = urllib.request.urlopen(pic_url)
    date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    hour = str(int(time.strftime('%H', time.localtime(time.time()))) - 1)
    pic_name = cwd + "\\downloads\\" + date + "-" + hour + ".png"
    conn = urllib.request.urlopen(pic_url)
    f = open(pic_name, 'wb')
    f.write(conn.read())
    f.close()
    print(pic_name + ' Saved!')
    return pic_name


def main():
    if not os.path.exists(cwd + "/downloads"):
        os.mkdir(cwd + "/downloads")
    while True:
        pic_url = getPic_url()
        pic_name = down_pic(pic_url)
        set_desktop(pic_name)
        time.sleep(60*5)
main()

