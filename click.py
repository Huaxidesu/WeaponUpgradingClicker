import pyautogui
import time
import keyboard


clicking = False  # 点击状态


def start_clicking():
    global clicking
    clicking = True


def stop_clicking():
    global clicking
    clicking = False


def end_program():
    global running
    running = False


# 注册键盘监听事件
keyboard.add_hotkey("left", start_clicking)  # 当按下←键时，开始点击
keyboard.add_hotkey("right", stop_clicking)  # 当按下→键时，停止点击
keyboard.add_hotkey("down", end_program)  # 当按下↓键时，结束程序

running = True
try:
    while running:
        if clicking:
            pyautogui.click()
            time.sleep(0.5)  # 等待点击间隔
except KeyboardInterrupt:
    print("程序被用户中断")

print("程序结束")
