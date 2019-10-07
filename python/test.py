import re
s = 'http://www.rkpass.cn/image/54.gif'
pattern = 'http://www.rkpass.cn/image/([1-9]+).gif'
image = re.findall(pattern,s)
print(image[0])