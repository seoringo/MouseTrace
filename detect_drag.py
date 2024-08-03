'''動きを記録してcsvファイルに保存'''
# from pynput.mouse import Listener, Button
from pynput import mouse,keyboard
import time

# マウスイベントと座標のリスト
event_lst=[]
class RecordMouseMovement:
    def __init__(self):
        self.isClicked=False
        self.isDragging=False
        self.drag_start_pos=[]
        self.mouse_listener = mouse.Listener(on_click=self.on_click,on_move=self.on_move)
        self.key_listener = keyboard.Listener(on_press=self.end)

    
    def on_move(self,x,y):
        if self.isClicked==True:
            # clickしたあと
            print('ドラッグしている')
            self.isDragging=True


    def on_click(self,x, y, button, pressed):
        '''リリースしたときも反応する'''

        if pressed:
            # クリック
            self.isClicked=True
            self.drag_start_pos=[x,y]
            print(f'click:{self.drag_start_pos}')
        else:
            # リリース
            print('released')

            if self.isDragging==True and button == mouse.Button.left:
                event_lst.append(['move',str(self.drag_start_pos[0]),str(self.drag_start_pos[1])])
                event_lst.append(['drag',x,y])
                print(f'ドラッグで記録:{self.drag_start_pos}→[{button},{x},{y}]')
            else:
                event_lst.append(['click',str(x),str(y),str(button)])
                print(f'クリックで記録:[{button},{x},{y}]')

            self.isClicked=False
            self.isDragging=False
            

    def start(self): 
            self.mouse_listener.start()
            self.key_listener.start()       
            self.mouse_listener.join()
            self.key_listener.join()


    def end(self,key):
        print('enddddd')
        if key == keyboard.Key.esc:
            print('停止')
            # リスナー停止
            self.mouse_listener.stop() 
            self.key_listener.stop()



if __name__ == "__main__":
    record = RecordMouseMovement()
    record.start()
