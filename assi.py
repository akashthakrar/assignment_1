import os
import sys

os.popen('mkdir -p music documents others videos compressed_files')
process = os.popen('ls -l | grep \'^-\' | awk \'{print $NF}\'')
op = process.read()
opar = op.splitlines()
for x in opar:
	if x==sys.argv[0]:
		continue
	if x.endswith(".mp3") or x.endswith(".wav") or x.endswith(".m3u"):
		os.popen("mv ./"+x+" ./music")
	elif x.endswith(".tar") or x.endswith(".iso") or x.endswith(".gz") or x.endswith(".zip") or x.endswith(".rar") or x.endswith(".bz2") or x.endswith(".7z"):
		os.popen("mv ./"+x+" ./compressed_files")
	elif x.endswith(".docx") or x.endswith(".doc") or x.endswith(".pdf") or x.endswith(".xls") or x.endswith(".xlsx") or x.endswith(".rtf") or x.endswith(".txt") or x.endswith(".odt"):
		os.popen("mv ./"+x+" ./documents")
	elif x.endswith(".mp4") or x.endswith(".3gp") or x.endswith(".avi") or x.endswith(".mov"):
		os.popen("mv ./"+x+" ./videos")
	else:
		os.popen("mv ./"+x+" ./others")
process.close()
