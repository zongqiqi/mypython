import wx

#test
# app=wx.App()
# app.MainLoop()

# Fram
# app=wx.App()#初始化应用
# win=wx.Frame(None)##初始化窗口
# win.Show()#显示
# app.MainLoop()#主循环

# app=wx.App()
# win=wx.Frame(None)
# btn=wx.Button(win)#添加按钮
# win.Show()
# app.MainLoop()

# app=wx.App()
# win=wx.Frame(None,title='Simple Editor')#设置窗口标题
# loadButton=wx.Button(win,label="Open")#设置按钮名称
# saveButton=wx.Button(win,label="Save")
# win.Show()
# app.MainLoop()

# app=wx.App()
# win=wx.Frame(None,title='Simple Editor',size=(410,350))
# win.Show()
# loadButton=wx.Button(win,label="Open",size=(80,25),pos=(225,5))
# saveButton=wx.Button(win,label="Save",pos=(315,5),size=(80,25))
# filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))
# contents=wx.TextCtrl(win,pos=(5,35),size=(390,260),
#  			    	style=wx.TE_MULTILINE|wx.HSCROLL)
# app.MainLoop()


#使用尺寸器,定义buttom函数
def load(event):
	file=open(filename.GetValue())
	contents=SetValue(file.read())
	file.close()
def save(event):
	file=open(filename.GetValue())
	file.write(contents.GetValue())
	filename.close()

app=wx.App()
win=wx.Frame(None,title='Simlpe Editor',size=(410,335))
bkg=wx.Panel(win)#===========
loadButton=wx.Button(bkg,label="Open")
saveButton=wx.Button(bkg,label="Save")
filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)
hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND)
hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)
bkg.SetSizer(vbox)
win.Show()
app.MainLoop()