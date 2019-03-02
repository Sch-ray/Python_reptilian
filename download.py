import requests 
import urllib.request
import re
import linecache
import os

print("---------------碎片化ts视频自动批量下载脚本---------------\nby：Sch_ray\n将此脚本放到文件夹里，避免大量文件产生\n\n")


#下载模块
def download(url,filename):
	Durl=url+'out'+filename+".ts"
	r = requests.get(Durl) 
	with open(filename+".ts", "wb") as video:
		video.write(r.content)

def downloadm(url):
	url=url+'playlist.m3u8'
	r = requests.get(url) 
	with open('playlist.m3u8', "wb") as video:
		video.write(r.content)

def alldownload(url,num1,num2):
	for bianhao in range(num1,num2):
		if bianhao<10:
			shuchu='00'+str(bianhao)
		if 10<=bianhao<100:
			shuchu='0'+str(bianhao)
		if bianhao>=100:
			shuchu=str(bianhao)
		#根据路径和编号两个参数循环下载
		download(url,shuchu)
		print(Yurl+'out'+shuchu+".ts......OK!")

Yurl=input("文件路径(不要把playlist.m3u8粘进去)：")
dow = input('要重新下载新的m3u8文件吗？(Y/N)')
if dow == 'yes' or dow =='Yes' or dow =='Y' or dow == 'y':
	downloadm(Yurl)
	print('m3u8文件下载成功，正在分析...')
else:print('将会使用旧的m3u8文件')

#打开当前目录下的m3u8文件并进行后续分析
Traget_m3u8 = open("playlist.m3u8","r")
text = Traget_m3u8.readlines()
Traget_m3u8.close()
#获取长度
textlen = len(text)
#找到最后一行
text2 = linecache.getline('playlist.m3u8',textlen-1)
#正则表达式
Reg = 'out(.+)\.ts'
Reg_text = re.compile(Reg)
List_Len = Reg_text.findall(text2)
List_Len_int = int(List_Len[0])
print("m3u8文件分析成功，共有" + List_Len[0] + "个文件需要下载...\n")

dow = input('确认要全部下载吗？(Y/N)')
if dow == 'yes' or dow =='Yes' or dow =='Y' or dow == 'y':
	num1=3
	num2=List_Len_int+1
else:
	num1=input('起始:')
	num2=input('结束:')
	num1=int(num1)
	num2=int(num2)+1

alldownload(Yurl,num1,num2)

#视频拼接
print("下载成功\n开始合并...")

os.system('copy /b *.ts new.mp4')
print('合并完成...')
os.system('rm *.ts')