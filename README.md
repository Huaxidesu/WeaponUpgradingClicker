# WeaponUpgradingClicker #

给Minecraft的武器大师Weapon Master和Tetra武器锻造模组升级武器整的连点器。

## 快速开始 ##

### 如果你不熟悉也没下Python，建议下载`repeatclick.exe`双击使用，并以管理员权限运行 ###

所有文件下载地址 [**下载最新版本**](https://github.com/Huaxidesu/WeaponUpgradingClicker/releases/)

### `click.py` - 基础自动点击 ###

- **启动**: 按←键自动点击开始。
- **停止**: 按→键自动点击停止。
- **退出**: 按↓键结束程序。
- **自定义设置**: 若要调整点击间隔，可以修改`time.sleep(value)`中的`value`（间隔秒数，数值越小点击速度越快）。

### `repeatclick.py` - 带间隔设置的自动点击 ###

- **设置间隔**: 启动时输入点击间隔。
- **重新设置**: 按↑键时，提示重新输入间隔。
- **启动**: 按←键自动点击开始。
- **停止**: 按→键自动点击停止。
- **重设间隔**：按→键重新输入间隔时间。
- **退出**: 按↓键结束程序。

### `moreclick.py` - 可自定义热键和间隔的自动点击 ###

- **自定义键位和间隔时间**: 用户可以通过修改`keyboard.add_hotkey`中的键位和间隔时间来自定义操作。
- **停止与退出**: 按→键停止点击，按↓键结束程序。
- **自定义设置**: 通过代码直接修改键位和间隔时间，具体方法请查看脚本内的注释。

### `repeatclick.exe` - 打包版本 ###

- 功能与`repeatclick.py`相同，无需安装Python或其他库。
- 适合不熟悉Python环境的用户使用。

## 安装 - 仅限py文件 ##

1. 确保你的系统中已经安装了Python环境。

2. 安装所需库：按照以下步骤安装`pyautogui`和`keyboard`库：

   - `pip install pyautogui pyautogui`

   - `pip install pyautogui keyboard`

3. 运行脚本：在命令行中使用`python 名字.py`命令运行脚本。

## 演示图片 ##

![演示图片](https://github.com/Huaxidesu/WeaponUpgradingClicker/blob/%E4%B8%BB%E8%A6%81/%E6%BC%94%E7%A4%BA/gif.gif)

## 演示视频 ##

[演示视频](https://www.bilibili.com/video/BV1oz421f7zH/)

## 注意事项 ##

- 运行Python脚本可能需要管理员权限。
- 使用说明和参数调整请参考各文件内的注释。

## 题外话 ##

武器大师Weapon Master打的血越多升级越快所以稻草人越多越好，蓄力越满越好

Tetra只看击中次数，所以无所谓，打的越快越好

什么？你服务器没加稻草人，快去做刷怪塔！别摔残血，尽量满血！
