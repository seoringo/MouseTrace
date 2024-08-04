'''動きを記録してcsvファイルに保存'''
import datetime
from pynput import mouse,keyboard
import os

# マウスイベントと座標のリスト
event_lst=[]
class RecordMouseMovement:
    def __init__(self):
        self.isClicked=False
        self.isDragging=False
        self.drag_start_pos=[]
        self.filename=''
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
                event_lst.append(['drag',str(x),str(y)])
                print(f'ドラッグで記録:{self.drag_start_pos}→[{button},{x},{y}]')
            else:
                event_lst.append(['click',str(x),str(y),str(button)])
                print(f'クリックで記録:[{button},{x},{y}]')

            self.isClicked=False
            self.isDragging=False
            

    def save_event(self,lst=[]):
        '''ファイルにイベントを保存'''

        DIR_NAME = "MouseRecords"
        try:
            if not os.path.exists(DIR_NAME):
                # ディレクトリが存在しない場合、ディレクトリを作成する
                os.makedirs(DIR_NAME)
        except Exception as e:
            print(e)

        if self.filename=='':
            # タイムスタンプ
            # すでにファイルが作成されていた時
            now = datetime.datetime.now()
            self.filename =now.strftime('%Y%m%d_%H%M%S') + '.csv'
            # self.filename='a.csv'
        
        # イベントを保存
        try:
            file_path=DIR_NAME+'/'+self.filename
            with open(file_path,'w',encoding='utf-8') as f:
                for row in lst:
                    f.write(','.join(row)+'\n')
        except Exception as e:
            print(e)

    def start(self,filename=''): 
            self.filename=filename
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
            self.save_event(event_lst)
            

# def btn_record():
#     '''記録ボタンを押された'''
#     record = RecordMouseMovement()
#     record.start()


if __name__ == "__main__":
    record = RecordMouseMovement()
    record.start()
