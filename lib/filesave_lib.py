#coding=utf-8 
import urllib,StringIO
import sys,datetime

sys.path.append("..")
import config

import Image

import os,sys

reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.
class SaveFile:
	def save_web_file(self, img_url):
		try:
			data = urllib.urlopen(img_url).read()
			im = Image.open(StringIO.StringIO(data))
		except Exception,e:
			print e
			return False
		return self.save_disk_file(StringIO.StringIO(data),data)
		return self.save_file(StringIO.StringIO(data))

	def save_disk_file(self,file_obj,data=''):
		im = Image.open(file_obj)
		(imwidth,imheight) = im.size
		if imwidth<2 and imheight<2:
			return "X"
		file_md5 = self.getfilemd5(file_obj)
		file_path = self.get_file_path(file_md5)
		if not os.path.isdir(file_path):
			os.mkdir(file_path)
		fp = open(file_path+file_md5,"w+")
		fp.write(data)
		fp.close()

		return {"img_width":imwidth,"img_height":imheight,"file_md5":str(file_md5)}

	def get_file_path(self, file_md5):
		file_path = config.file_save_path+"/"+file_md5[0:2]+"/"
		return file_path

	#size: (max_width,max_height)
	def get_img_file_thumbnail_value(self,file_md5,thumbnail_size=(192,1000)):
		import StringIO
		output = StringIO.StringIO()
		file_md5 = file_md5
		try:
			file_path = self.get_file_path(file_md5)
			file_path_name = file_path+"/"+file_md5
			print file_path_name
			im = Image.open(file_path_name)
			im = im.convert('RGB')
			im.thumbnail(thumbnail_size,Image.ANTIALIAS)
			im.save(output,"JPEG")
			return output.getvalue()
		except Exception,e:
			print e
			return HttpResponse(output.getvalue(),mimetype="image/gif")
			return False

	def get_file(self,file_md5):
		try:
			file_path = self.get_file_path(file_md5)
			file_path_name = file_path+"/"+file_md5
			return open(file_path_name).read()
		except Exception,e:
			print e
			return False

	def if_file_exists(self,file_obj):
		file_md5 = self.getfilemd5(file_obj)
		file_path = self.get_file_path(file_md5)
		file_path_name = file_path+"/"+file_md5
		return os.path.isfile(file_path_name)

	def getfilemd5(self,file_obj):
		import hashlib
		file_obj.seek(0)
		#需要设置成二进制文件格式，否则无法正常读取部分文件
		data = file_obj.read()
		myMd5 = hashlib.md5()
		myMd5.update(data)
		myMd5_Digest = myMd5.hexdigest()
		#返回文件起始点
		file_obj.seek(0)
		return myMd5_Digest
		

