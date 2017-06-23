# ���������ַ
PyCmd=python
PyRcc=C:\Users\vsG\AppData\Local\Programs\Python\Python36-32\Scripts\pyrcc5.exe
Pylupdate=C:\Python35\Lib\site-packages\PyQt5\pylupdate5.exe
Pylrelease=C:\Python35\Lib\site-packages\PyQt5\lrelease.exe

# ����Ŀ¼��أ���ǰ�ٶ�pro�ļ���ts�ļ�ͬ����
RootDir = $(MAKEDIR)
GenerateProPy=generate_pro.py
ProName=sanguosha_py
ProFileName=$(ProName).pro
QmFileName=$(ProName).qm
RsFileName=resource/res.qrc

all: $(QmFileName) $(RsFileName:.qrc=_rc.py)
	
	
# $@--Ŀ���ļ���$^--���е������ļ���$<--��һ�������ļ���
# %.qm:%.ts nmake ��֧�������﷨���Ҳ�֧��$< ������


# qm�ļ�
$(QmFileName):$(QmFileName:.qm=.ts)
	$(Pylrelease) $(QmFileName:.qm=.ts)

# ts�ļ�
$(QmFileName:.qm=.ts):$(QmFileName:.qm=.pro)
	$(Pylupdate) $(QmFileName:.qm=.pro)
	
# pro �ļ�
$(ProFileName):
	$(PyCmd) $(GenerateProPy) $(ProName)
	
# rcc�ļ�
$(RsFileName:.qrc=_rc.py):$(RsFileName)	
	$(PyRcc) $(RsFileName) -o $(RsFileName:.qrc=_rc.py)	
	
	
# ��ǰû��ʹ��ui���ɴ��壬���ﲻ��������ݣ��������Ҫ�����
# del *.ts ��ɾ�������ļ���������治��������ӷ����ļ�
clean:
	del *.qm *.pro
	del /S *_rc.py
	
.PHONY: clean $(ProFileName)
	