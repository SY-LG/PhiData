#coding=utf-8
from xml.etree import ElementTree as ET
from urllib import parse
per=ET.parse('com.PigeonGames.Phigros.v2.playerprefs.xml')
p=per.findall('.')
dict={}

for element in p:
	for child in list(element):
		if(child.tag=="int"):
			dict[parse.unquote(child.attrib["name"])]=parse.unquote(child.attrib["value"])
		else:
			dict[parse.unquote(child.attrib["name"])]=parse.unquote(child.text)


file_sort=open("sort.txt", "w")
file_simp=open("simp.txt", "w")
dict1_sorted_items1 = sorted(dict.items(),key = lambda x:x[0])
for key in dict1_sorted_items1:
	print(key[0],key[1],file=file_sort)
	if(key[1]!="s9mNN+yGZj/hdWZTAdLDsrNXnSiaO92FDmy930FgQa3/C4myxQiQ3blrJ7vZl8g0"):
		print(key[0],key[1],file=file_simp)