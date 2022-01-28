#coding=utf-8
import io
import sys
import base64
from urllib import parse
from pyDes import des, CBC, PAD_PKCS5
from xml.etree import ElementTree as ET

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

key_base64 = 'UABHAFIAUwA='
KEY=base64.b64decode(key_base64)

def des_descrypt(s):
	secret_key=KEY
	iv=secret_key
	res=base64.b64decode(s)
	des_obj=des(secret_key,CBC,iv,pad=None,padmode=PAD_PKCS5)
	decrypt_str=des_obj.decrypt(res,padmode=PAD_PKCS5)
	return decrypt_str

per=ET.parse('com.PigeonGames.Phigros.v2.playerprefs.xml')
p=per.findall('.')
dict1={}
dict2={}

for element in p:
	for child in list(element):
		if child.tag=="int":
			dict1[parse.unquote(child.attrib["name"])]=child.attrib["value"]
		elif child.attrib["name"].find("unity")!=-1:
			dict1[child.attrib["name"]]=parse.unquote(child.text)
		else:
			str1=des_descrypt(parse.unquote(child.attrib["name"]));
			str2=des_descrypt(parse.unquote(child.text));
			# str1.decode("gbk",'ignore')
			# str2.decode("gbk",'ignore')
			# print(str1.decode("utf-8",'ignore'))
			# print(str2.decode("utf-8",'ignore'))
			dict2[str1]=str2


file_descrypt=open("descrypt.txt", "w",encoding='utf-8')
dict1_sorted_items = sorted(dict1.items(),key = lambda x:x[0])
dict2_sorted_items = sorted(dict2.items(),key = lambda x:x[0])
for key in dict1_sorted_items:
	print(key[0],key[1],file=file_descrypt)
for key in dict2_sorted_items:
	print(key[0].decode("utf-8","ignore"),key[1].decode("utf-8","ignore"),file=file_descrypt)