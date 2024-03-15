import pyautogui
import time
import keyboard

clicking = False  # 点击状态
interval = 0.5  # 默认点击间隔时间


def set_interval(short):
    global interval
    interval = short
    print(f"设置点击间隔时间为 {interval} 秒")


def stop_clicking():
    global clicking
    clicking = False
    print("停止点击")


def end_program():
    global running
    running = False
    print("结束程序")


keyboard.add_hotkey("left", set_interval, args=(0.5,))  # 自己改键和时间
keyboard.add_hotkey("up", set_interval, args=(1.0,))  # 自己改键和时间
keyboard.add_hotkey("[", set_interval, args=(1.5,))  # 自己改键和时间
keyboard.add_hotkey("right", stop_clicking)  # 当按下→键时，停止点击
keyboard.add_hotkey("down", end_program)  # 当按下↓键时，结束程序

running = True
clicking = False
try:
    while running:
        if clicking:
            pyautogui.click()
            time.sleep(interval)  # 等待点击间隔
except KeyboardInterrupt:
    print("程序被用户中断")

print("程序结束")
