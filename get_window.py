from win32gui import GetWindowText, GetForegroundWindow

# アクティブなウィンドウを取得
def get_active_window_title():
    return GetWindowText(GetForegroundWindow())

print(get_active_window_title())