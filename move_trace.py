'''csvファイルを読み込んで、動きをトレース'''
import pyautogui as gui
import time

filename='a.csv'

# ファイルの読み込みとパース
with open(filename, 'r', encoding='utf-8') as f:
    all_lst = [line.strip().split(',') for line in f]

start_time = time.time()

pre_x=0
pre_y=0

# イベント処理と実行時間の計測
for lst in all_lst:
    event, x, y = lst[0], int(lst[1]), int(lst[2])
    if event == 'move':
        duray = float(lst[3])
        # gui.moveTo(x, y, duration=duray)
        gui.moveTo(x, y)
    elif event[-5]=='click':
        # クリックイベントの場合、座標を保存
        pre_x=x
        pre_y=y
    elif event[-8]=='released':
        gui.drag()


    # elif event == 'left_click':
    #     gui.click(x, y)
    # elif event == 'right_click':
    #     gui.rightClick(x, y)
        
        
end_time = time.time()
actual_duration = end_time - start_time
print(f"Event: {event}, Expected Duration: {duray if event == 'move' else 'N/A'}, Actual Duration: {actual_duration}")    