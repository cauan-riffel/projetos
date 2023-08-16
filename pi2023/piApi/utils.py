from json import dumps,loads
from datetime import datetime


def changeContent(newContent):
	oldContent=loads(rc())
	newContent=(newContent[1:-2]+',"created":"%s"}'%str(datetime.now())).replace('\\"','"')
	tempData=roc()
	print(newContent)
	print(type(newContent))
	f=goc('w')
	f.write(tempData[:-3]+',%s]}'%str(oldContent).replace("'",'"'))
	f.close()
	f=gc('w')
	f.write(newContent)
	f.close()




def goc(mode):
	return open('./temps/mainContent.json',mode)
def roc():
	f=goc('r')
	c=f.read()
	f.close()
	return c
def gc(mode):
	return open('./mainContent.json',mode)
def rc():
	f=gc('r')
	c=f.read()
	f.close()
	return c
