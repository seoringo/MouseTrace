import pyautogui as gui
import wx

filename='a.csv'

class ReproductionMouse:
    '''動きを再現'''   

    def __init__(self):
        self.all_lst=[]

    def get_content(self,filename=''):
        '''ファイルの取得'''

        if filename=='':
            wx.MessageBox(u'ファイル名が指定されていません', u'エラー', wx.OK)
            return

        try:
            DIR_NAME = "MouseRecords"
            file_path=DIR_NAME+'/'+filename
            # ファイルの読み込みとパース
            with open(file_path, 'r', encoding='utf-8') as f:
                self.all_lst = [line.strip().split(',') for line in f]
                self.exe_event()
        except FileNotFoundError:
            wx.MessageBox(u'ファイルが存在しません', u'エラー', wx.OK)
            return


    # イベント実行
    def exe_event(self,duray=1.0):
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
    repro.get_content(filename='a.csv')