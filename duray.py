from pynput import mouse
import time

'''マウス移動の間隔、スピードを表示'''
class MouseMovementTracker:
    def __init__(self):
        self.previous_time = None
        self.listener = mouse.Listener(on_move=self.on_move)

    def on_move(self, x, y):
        current_time = time.time()
        if self.previous_time is not None:
            interval = current_time - self.previous_time
            print(f"Moved to ({x}, {y}) after {interval:.4f} seconds")
        self.previous_time = current_time

    def start(self):
        with self.listener:
            self.listener.join()

if __name__ == "__main__":
    tracker = MouseMovementTracker()
    tracker.start()
