import pyautogui as gui
import time

filename='a.csv'

class ReproductionMouse:
    '''動きを再現'''   

    def __init__(self):
        self.all_lst=[]

    def get_content(self,filename='a.csv'):
        try:
            # ファイルの読み込みとパース
            with open(filename, 'r', encoding='utf-8') as f:
                self.all_lst = [line.strip().split(',') for line in f]
        except Exception as e:
            print(e)


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


if __name__ == "__main__":
    repro = ReproductionMouse()
    repro.get_content()
    repro.exe_event()