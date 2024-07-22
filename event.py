'''動きを記録してcsvファイルに保存'''
from pynput.mouse import Listener, Button

# マウスイベントと座標のリスト
mouse_event_lst=[]

def on_move(x, y):
    print(f"マウスが移動しました：({x}, {y})")
    mouse_event_lst.append(['move',str(x),str(y)])

def on_click(x, y, button, pressed):
    button_name = None
    if button == Button.left:
        button_name = "左クリック"
        mouse_event_lst.append(['left_click',str(x),str(y)])
    elif button == Button.right:
        button_name = "右クリック"
        mouse_event_lst.append(['right_click',str(x),str(y)])
        save_event(mouse_event_lst)
        listener.stop() # リスナー停止
    
    action = "クリック" if pressed else "リリース"
    print(f"{button_name} が {action} されました：({x}, {y})")

def on_scroll(x, y, dx, dy):
    print(f"マウスがスクロールしました：({x}, {y}) ({dx}, {dy})")


def save_event(lst=[],filename=''):
    '''excelにイベントや座標を保存'''

    if filename=='':
        # タイムスタンプ
        filename='a.csv'
    
    with open(filename,'w',encoding='utf-8') as f:
        for row in lst:
            f.write(','.join(row)+'\n')
            


# マウスのイベントリスナーを作成
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()  # イベントリスナーが終了するまで待機