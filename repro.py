import pyautogui as gui
import wx

filename='a.csv'

class ReproductionMouse:
    '''動きを再現'''   

    def __init__(self,filename='',repeat='1'):
        self.all_lst=[]
        self.repeat=repeat
        self.filename=filename

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        if filename=='':
            wx.MessageBox(u'ファイル名が指定されていません', u'エラー', wx.OK)
            return
        else:
            self.__filename=filename



    @property
    def repeat(self):
        return self.__repeat

    @repeat.setter
    def repeat(self, repeat):
        if repeat.isdecimal():
            self.__repeat = int(repeat)
        else:
            wx.MessageBox(u'数値で指定してください', u'エラー', wx.OK)
            return
        
        
    def get_content(self):
        '''ファイルの取得'''
        try:
            DIR_NAME = "MouseRecords"
            file_path=DIR_NAME+'/'+self.filename
            # ファイルの読み込みとパース
            with open(file_path, 'r', encoding='utf-8') as f:
                self.all_lst = [line.strip().split(',') for line in f]
                self.exe_event()
        except FileNotFoundError:
            wx.MessageBox(u'ファイルが存在しません', u'エラー', wx.OK)
            return


    # イベント実行
    def exe_event(self,duray=1.0):
        for i in range(self.repeat):
            for lst in self.all_lst:
                event, x, y = lst[0], int(lst[1]), int(lst[2])
                if event == 'move':
                    gui.moveTo(x, y, duration=duray)
                elif event=='click':
                    button=lst[3]
                    if button=='Button.left':
                        gui.click(x,y)
                    else:
                        gui.rightClick(x,y)
                elif event=='drag':
                    gui.dragTo(x,y,duration=duray)

# def btn_repro():
#     '''再現ボタンが押された'''
#     repro = ReproductionMouse()
#     repro.get_content()

if __name__ == "__main__":
    repro = ReproductionMouse()
    repro.get_content()