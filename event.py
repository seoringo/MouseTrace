'''動きを記録してcsvファイルに保存'''
from pynput.mouse import Listener, Button
import time

# マウスイベントと座標のリスト
mouse_event_lst=[]
class RecordMouseMovement:
    def __init__(self):
        self.previous_time = None
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

    def on_move(self, x, y):
        current_time = time.time()
        if self.previous_time is not None:
            interval = current_time - self.previous_time
            # print(f"Moved to ({x}, {y}) after {interval:.4f} seconds")
            print(f"マウスが移動しました：({x}, {y}, {interval:.4f} )")
            mouse_event_lst.append(['move',str(x),str(y),str(interval)])
        else:
            # 初回または、クリック後
            print(f"マウスが移動しました：({x}, {y}, 0 )")
            mouse_event_lst.append(['move',str(x),str(y),'0'])
        self.previous_time = current_time 

    # def on_move(x, y):
    #     print(f"マウスが移動しました：({x}, {y})")
    #     mouse_event_lst.append(['move',str(x),str(y)])

    def on_click(self,x, y, button, pressed):
        button_name = None
        if button == Button.left:
            button_name = "左クリック"
            mouse_event_lst.append(['left_click',str(x),str(y)])
            self.previous_time=None
        elif button == Button.right:
            button_name = "右クリック"
            mouse_event_lst.append(['right_click',str(x),str(y)])
            self.previous_time=None
            save_event(mouse_event_lst)
            self.listener.stop() # リスナー停止
        
        action = "クリック" if pressed else "リリース"
        print(f"{button_name} が {action} されました：({x}, {y})")

    def on_scroll(self,x, y, dx, dy):
        print(f"マウスがスクロールしました：({x}, {y}) ({dx}, {dy})")

    def start(self):
        with self.listener:
            self.listener.join()    


def save_event(lst=[],filename=''):
    '''excelにイベントや座標を保存'''

    if filename=='':
        # タイムスタンプ
        filename='a.csv'
    
    with open(filename,'w',encoding='utf-8') as f:
        for row in lst:
            f.write(','.join(row)+'\n')
            


# # マウスのイベントリスナーを作成
# with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()  # イベントリスナーが終了するまで待機

if __name__ == "__main__":
    record = RecordMouseMovement()
    record.start()
