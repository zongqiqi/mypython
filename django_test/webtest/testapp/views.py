from django.shortcuts import render
import glob,os

#根据路径获取图名的文件名(加上静态文件路径，方面模板调用)
def get_pic_name(pic_path,static_path):
	pics=glob.iglob(pic_path)
	static_path='pic/small/'
	pwd=os.path.dirname(__file__)
	pics=glob.glob(pwd+pic_path)
	pics_list=[]
	for pic in pics:
		pic_text=os.path.split(pic)[1]#分离图片文件的路径和文件名
		pics_list.append(static_path+pic_text)
	return pics_list




def index(request):

	#插入缩略图图片
	pic_path=r'/static/pic/small/*.jpg'
	static_path='pic/small/'
	small_pics=get_pic_name(pic_path,static_path)
	context={'small_pics':small_pics}

	return render(request,'testapp/index.html',context)
