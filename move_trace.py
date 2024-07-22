'''csvファイルを読み込んで、動きをトレース'''
import pyautogui as gui

filename='a.csv'

with open(filename,'r',encoding='utf-8') as f:
    for line in f:
        lst=line.split(',')
        event,x,y=lst[0],int(lst[1]),int(lst[2])
        if event=='move':
            gui.moveTo(x,y)
        elif event=='left_click':
            gui.click(x,y)
        elif event=='right_click':
            gui.rightClick(x,y)
        
        
        