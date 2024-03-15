import pyautogui
import time
import keyboard

clicking = False
interval = 0.5  # 默认点击间隔时间


def set_interval(short):
    global interval, clicking
    interval = short
    clicking = True


def stop_clicking():
    global clicking
    clicking = False
    print("停止点击")


def end_program():
    global running
    running = False
    print("结束程序")


keyboard.add_hotkey("left", set_interval, args=(0.5,))  # 自己改键
keyboard.add_hotkey("up", set_interval, args=(1.2,))    # 自己改键
keyboard.add_hotkey("[", set_interval, args=(1.5,))    # 自己改键
keyboard.add_hotkey("right", stop_clicking)            # 停止点击
keyboard.add_hotkey("down", end_program)               # 结束程序

running = True
try:
    while running:
        if clicking:
            pyautogui.click()
            time.sleep(interval)  # 等待点击间隔
except KeyboardInterrupt:
    print("程序被用户中断")

print("程序结束")
