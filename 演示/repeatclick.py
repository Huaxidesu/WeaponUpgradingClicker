import pyautogui
import time
import keyboard

clicking = False  # 点击状态
click_interval = 0.5  # 默认点击间隔


def get_click_interval():
    global click_interval
    while True:
        try:
            interval_input = input("请输入点击间隔（秒）：")
            click_interval = float(interval_input)
            break
        except ValueError:
            print("输入无效，请输入一个数字。")


def start_clicking():
    global clicking
    clicking = True
    print("开始点击")


def stop_clicking():
    global clicking
    clicking = False
    print("停止点击")


def end_program():
    global running
    running = False
    print("结束程序")


def prompt_for_interval():
    print("提示：重新输入间隔")
    get_click_interval()


# 注册键盘监听事件
keyboard.add_hotkey("left", start_clicking)  # 当按下←键时，开始点击
keyboard.add_hotkey("right", stop_clicking)  # 当按下→键时，停止点击
keyboard.add_hotkey("down", end_program)  # 当按下↓键时，结束程序
keyboard.add_hotkey("up", prompt_for_interval)  # 当按下↑键时，提示重新输入间隔

get_click_interval()  # 取点击间隔

running = True
try:
    while running:
        if clicking:
            pyautogui.click()
            time.sleep(click_interval)  # 使用用户输入的点击间隔
except KeyboardInterrupt:
    print("程序被用户中断")

print("程序结束")
