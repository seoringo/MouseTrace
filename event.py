from pynput.mouse import Listener, Button

def on_move(x, y):
    print(f"マウスが移動しました：({x}, {y})")

def on_click(x, y, button, pressed):
    button_name = None
    if button == Button.left:
        button_name = "左クリック"
    elif button == Button.right:
        button_name = "右クリック"
    elif button == Button.middle:
        button_name = "中央クリック"
    elif button == Button.x:
        button_name = f"ボタン{button.value}"
    elif button == Button.y:
        button_name = f"ボタン{button.value}"
    
    action = "クリック" if pressed else "リリース"
    print(f"{button_name} が {action} されました：({x}, {y})")

def on_scroll(x, y, dx, dy):
    print(f"マウスがスクロールしました：({x}, {y}) ({dx}, {dy})")

# マウスのイベントリスナーを作成
with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    listener.join()  # イベントリスナーが終了するまで待機