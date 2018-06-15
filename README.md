# LiveEarth!

## Introduction
- Windows下实时动态更新地球壁纸！
- 地球照片抓自日本[himawari-8](http://himawari8.nict.go.jp/)气象卫星官网
- ~~默认每小时抓取一次~~（改为5分钟获取一次最新的图片，网站图片是10分钟更新一次）
- ~~不到50行的python代码~~ (不包括import)
- 感谢 [bitdust](https://github.com/bitdust) 提供的idea

## 2018/6/15更新
- 更换图片的url的拼接方式，改由请求最新的图片url

<pre><code>
url='http://himawari8-dl.nict.go.jp/himawari8/img/D531106/latest.json?uid='+str(int(round(time.time() * 1000)))
</pre></code>


## Screenshots
<img src='http://files.cnblogs.com/files/mrpod2g/earth1.gif' width='500' />
<img src='http://files.cnblogs.com/files/mrpod2g/earth2.gif' width='500' />
<img src='http://files.cnblogs.com/files/mrpod2g/earth3.gif' width='500' />

