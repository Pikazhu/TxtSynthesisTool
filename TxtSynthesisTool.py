# -*- coding:utf-8 -*-
#txt文件合成器。即：将文件夹下的所有txt文件合成一个大的TXT文件。

#需要传入两个参数。
#第一个参数为：文件夹的绝对路径
#第二个参数为：要存储的txt文件名。

import os

class TxtSynthesisTool:
    def __init__(self):
        self.__folderName=''
        self.__txtName=''

    @property
    def folderName(self):
        return self.__folderName
    @folderName.setter
    def folderName(self,value):
        self.__folderName=value

    @property
    def txtName(self):
        return self.__txtName
    @txtName.setter
    def txtName(self,value):
        self.__txtName=value

    def init(self):
        #判断文件夹路径是否正确。。不正确一直等到输入直到*正确。。
        while True:
            self.folderName = input('请输入文件夹的路径：')
            if self.judgeFolderPath():
                break;
        # 判断合成文件名是否正确。。不正确一直等到输入直到*正确。。
        while True:
            txt = input('请输入要存储的文件名称(不用带后缀)：')
            self.txtName = txt + '.txt'
            if self.judgeTxtName():
                break;


    def judgeFolderPath(self):
        if os.path.exists(self.folderName):
            return True
        else:
            print('你输入的文件夹不存在,请重新输入文件夹根目录（绝对路径）')
            return False

    def judgeTxtName(self):
        if os.path.exists(self.folderName+'/'+self.txtName):
            print('该文件夹下已经有{}了.请换个名称存储。'.format(self.txtName))
            return False
        else:
            return True

    #合成
    def systhesis(self):
        # 获得当前文件夹下的所有文档。找出所有的txt类型的
        allFiles = os.listdir(self.folderName)
        txtFiles = [file for file in allFiles if file.find('.txt') != -1]
        txt=open(self.folderName+'/'+self.txtName,'a')
        #读写过程。
        for file in sorted(txtFiles):
            txt.write(file.replace('.txt','')+'\n')
            smallTxt=open(self.folderName+'/'+file,'r')
            txtContent=smallTxt.read()
            txt.write(txtContent+'\n')
            smallTxt.close()

        txt.close()

    def run(self):
        self.init()
        self.systhesis()



if __name__ == '__main__':
    #/home/python/Desktop/xxSpider/myTool/TxtSynthesisTool/TxtFolder
    tool=TxtSynthesisTool()
    tool.run()
    print('合成完毕')



