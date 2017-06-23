# 配置命令地址
PyCmd=python
PyRcc=C:\Users\vsG\AppData\Local\Programs\Python\Python36-32\Scripts\pyrcc5.exe
Pylupdate=C:\Python35\Lib\site-packages\PyQt5\pylupdate5.exe
Pylrelease=C:\Python35\Lib\site-packages\PyQt5\lrelease.exe

# 配置目录相关（当前假定pro文件和ts文件同名）
RootDir = $(MAKEDIR)
GenerateProPy=generate_pro.py
ProName=sanguosha_py
ProFileName=$(ProName).pro
QmFileName=$(ProName).qm
RsFileName=resource/res.qrc

all: $(QmFileName) $(RsFileName:.qrc=_rc.py)
	
	
# $@--目标文件，$^--所有的依赖文件，$<--第一个依赖文件。
# %.qm:%.ts nmake 不支持这种语法，且不支持$< ！！！


# qm文件
$(QmFileName):$(QmFileName:.qm=.ts)
	$(Pylrelease) $(QmFileName:.qm=.ts)

# ts文件
$(QmFileName:.qm=.ts):$(QmFileName:.qm=.pro)
	$(Pylupdate) $(QmFileName:.qm=.pro)
	
# pro 文件
$(ProFileName):
	$(PyCmd) $(GenerateProPy) $(ProName)
	
# rcc文件
$(RsFileName:.qrc=_rc.py):$(RsFileName)	
	$(PyRcc) $(RsFileName) -o $(RsFileName:.qrc=_rc.py)	
	
	
# 当前没有使用ui生成窗体，这里不清除该内容，如果有需要再添加
# del *.ts 不删除翻译文件，否则后面不会增量添加翻译文件
clean:
	del *.qm *.pro
	del /S *_rc.py
	
.PHONY: clean $(ProFileName)
	