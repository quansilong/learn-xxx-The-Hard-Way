from PIL import Image,ImageDraw,ImageFont

txt = "4"
im = Image.open("test.jpg")

#缩小图片
(x,y) = im.size  #获取图片原大小（958,958）
x1 = 300         #强制横向像素为310
y1 = int(x1*y/x) #保持横纵比不变，y1/x1=y/x
im = im.resize((x1,y1),Image.ANTIALIAS) #重新设置大小，ANTIALIAS消除锯齿
#写字
draw = ImageDraw.Draw(im)   #创建画布对象
ttf = ImageFont.truetype(r'C:\Users\LiuGaoyong\Downloads\SimHei.ttf', 50) #创建字体对象；Windows文件路径强制不转义
draw.text((250,0), txt, fill="red", font=ttf) # 把txt文本写入draw对象；Python3没有unicode
im.save("项目结果.jpg")