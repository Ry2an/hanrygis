import wx
import os
import csv
import Image

class MainFrame(wx.Frame):
   
    def __init__(self):
        wx.Frame.__init__(self,None,1,'HanryGIS',size=(510,544))

        self.panel=wx.Panel(self,2)
        Inputbutton=wx.Button(self.panel,3,'Input Data',size=(80,24),pos=(320,8))
        
        Checkbutton=wx.Button(self.panel,4,'Check',size=(80,24),pos=(408,8))
        MapList=['China-Province','China-Country','Anhui',
                 'Beijing','Fujian','Gansu','Guangdong',
                 'Guangxi','Guizhou','Hainan','Hebei',
                 'Henan','Heilongjiang','Hubei','Hunan',
                 'Jilin','Jiangsu','Jianxi','Liaoning',
                 'Neimeng','Ningxia','Qinghai',
                 'Shandong','Shan(1)xi','Shan(3)xi',
                 'Shanghai','Sichuan','Taiwan','Tianjin',
                 'Xizang','Xianggang','Xinjiang','Yunnan',
                 'Zhejiang','Chongqing']
        self.Mapchoice=wx.Choice(self.panel,5,size=(148,24),choices=MapList,pos=(8,8))
        ModelList=['Points','Variables']
        self.Modelchoice=wx.Choice(self.panel,6,size=(148,24),
                                   choices=ModelList,pos=(164,8))
        Inputbutton.Bind(wx.EVT_BUTTON,self.inPut)
        Checkbutton.Bind(wx.EVT_BUTTON,self.chEck)
    def inPut(self,event):
        mapName=self.Mapchoice.GetStringSelection()
        modelName=self.Modelchoice.GetStringSelection()
        path="C:\\HanryGIS\\"+mapName
        os.startfile(path)
        messAge='Please copy your data in '+modelName+'.csv'
        wx.MessageBox(messAge,'Instruction')
    def chEck(self,event):
        mapName=self.Mapchoice.GetStringSelection()
        modelName=self.Modelchoice.GetStringSelection()
        path="C:\\HanryGIS\\"+mapName+"\\"+modelName+".csv"
        if(modelName=='Points'):
            reader=csv.reader(open(path,'rb'))
            i=0
            for row in reader:
                i=i+1
                #csvfile.close()
            if(i>=500):
                os.system('C:\\HanryGIS\\China-Province\\Points.bat')
                #time.sleep(5)
                bg=Image.open('C:\\HanryGIS\\'+mapName+'\\base.png')
                imp=Image.open('C:\\HanryGIS\\'+mapName+'\\points.png')
                out=imp.resize((480,446),Image.ANTIALIAS)
                out=out.convert("RGBA")
                r,g,b,a=out.split()
                bg.paste(out,(0,17),mask=a)
                bg.save('C:\\HanryGIS\\'+mapName+'\\result.png','png')
                resultplot=wx.Image('C:\\HanryGIS\\'+mapName+'\\result.png')
                resultshow=wx.StaticBitmap(self.panel,7,wx.BitmapFromImage(resultplot),
                                           size=(480,480),pos=(8,40))
            else:
                os.system('C:\\HanryGIS\\China-Province\\Dens.bat')
                #time.sleep(5)
                bg=Image.open('C:\\HanryGIS\\'+mapName+'\\density.jpeg')
                imp=Image.open('C:\\HanryGIS\\'+mapName+'\\base.png')
                out=imp.resize((480,480),Image.ANTIALIAS)
                out=out.convert("RGBA")
                r,g,b,a=out.split()
                bg.paste(out,(0,0),mask=a)
                bg.save('C:\\HanryGIS\\'+mapName+'\\result.png','png')
                resultplot=wx.Image('C:\\HanryGIS\\'+mapName+'\\result.png')
                resultshow=wx.StaticBitmap(self.panel,7,wx.BitmapFromImage(resultplot),
                                           size=(480,480),pos=(8,40))
            if(i>=500):
                wx.MessageBox('Plotting automatically(Point). Please wait...',
                              'HanryGIS')
            else:
                wx.MessageBox('Plotting automatically(Density). Please wait...',
                              'HanryGIS')
            
        else:
            if(modelName=='Variables'):
                os.system('C:\\HanryGIS\\China-Province\\Pie.bat')
                bg=Image.open('C:\\HanryGIS\\'+mapName+'\\base.png')
                imp=Image.open('C:\\HanryGIS\\'+mapName+'\\Muity\\mui1.png')
                out=imp.resize((64,64),Image.ANTIALIAS)
                out=out.convert("RGBA")
                r,g,b,a=out.split()
                bg.paste(out,(298,177),mask=a)
                bg.save('C:\\HanryGIS\\'+mapName+'\\result1.png','png')
                list1=[321,330,206,315,277,265,282,314,303,396,297,294,385,343,317,363,292,262,202,340,295,276,358,238,248,327,139,310,135,231,344]
                list2=[156,239,154,257,252,233,279,168,191,109,209,228,138,197,228,150,141,172,181,178,171,191,212,210,252,161,211,260,135,249,221]
                list3=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
                for i in list3:
                    #print i
                    bg=Image.open('C:\\HanryGIS\\'+mapName+'\\result1.png')
                    imp=Image.open('C:\\HanryGIS\\'+mapName+'\\Muity\\mui'+str(i+1)+'.png')
                    out=imp.resize((64,64),Image.ANTIALIAS)
                    out=out.convert("RGBA")
                    r,g,b,a=out.split()
                    bg.paste(out,(list1[i-1]-28,list2[i-1]-28),mask=a)
                    bg.save('C:\\HanryGIS\\'+mapName+'\\result1.png','png')
                bg=Image.open('C:\\HanryGIS\\'+mapName+'\\result1.png')
                imp=Image.open('C:\\HanryGIS\\'+mapName+'\\Muity\\mui33.png')
                out=imp.resize((64,64),Image.ANTIALIAS)
                out=out.convert("RGBA")
                r,g,b,a=out.split()
                bg.paste(out,(243,188),mask=a)
                bg.save('C:\\HanryGIS\\'+mapName+'\\result.png','png')
                resultplot=wx.Image('C:\\HanryGIS\\'+mapName+'\\result.png')
                resultshow=wx.StaticBitmap(self.panel,7,wx.BitmapFromImage(resultplot),
                                           size=(480,480),pos=(8,40))
                wx.MessageBox('Plotting automatically. Please wait...',
                              'HanryGIS')
            else:
                wx.MessageBox('WORNG! PELASE CHECK YOUR SELECTION','WRONG')

        
if __name__=='__main__':
    app=wx.App()
    frame=MainFrame()
    frame.Show()
    app.MainLoop()
