## Web
### urlencode 作用
urllib.urlencode(values)   #适用urllib对数据进行格式化编码  参见https://www.cnblogs.com/oxspirt/p/6165821.html
### HTTP Error 415: Unsupported Media Type
urllib2.Request(url, data, {'Content-Type':'application/json'})  需要加上 header 指定正确的 Content-Type, 参见关键词 "Http Header里的Content-Type - 飞鸿影~ - 博客园"