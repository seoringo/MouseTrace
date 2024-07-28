'''csvファイルを読み込んで、動きをトレース'''
import pyautogui as gui

filename='a.csv'

with open(filename,'r',encoding='utf-8') as f:
    # 読み込むだけ(読み込むのにそもそも時間かかるからduration)
    all_lst=[]
    for line in f:
        lst=line.strip().split(',')
        all_lst.append(lst)


    # 配列から
    for lst in all_lst:
        event,x,y=lst[0],int(lst[1]),int(lst[2])
        if event=='move':
            duray=float(lst[3])
            # gui.moveTo(x,y,duration=duray)
            print(x,y,duray)
            gui.moveTo(x,y)
        elif event=='left_click':
            gui.click(x,y)
        elif event=='right_click':
            gui.rightClick(x,y)
        
        
        