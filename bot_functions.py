import pyautogui
import pydirectinput
from time import sleep
from random import randint
from psutil import process_iter


class ApexBot:
    def __init__(self, resolution):
        self.in_game = False
        self.resolution = resolution
        self.tries_to_find_fill_button = 0

    def xp_grinding(self):
        # 检查Apex是否正在运行
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # 通过跳跃防止玩家因挂机而被踢出游戏
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
        elif pyautogui.locateOnScreen(f"Game Assets/dianchi_HD.png", confidence=.8) is not None:
            self.in_game = True
            # 按下鼠标左键
            pydirectinput.mouseDown(button='left')
            # 暂停一段时间，例如1秒钟
            sleep(randint(0, 5))
            # 释放鼠标左键
            pydirectinput.mouseUp(button='left')
            pydirectinput.press("space")
        elif pyautogui.locateOnScreen(f"Game Assets/continue_{self.resolution}.png", confidence=.7) is not None:
            self.in_game = True
            # 按前进键键
            pydirectinput.press("space")
        elif pyautogui.locateOnScreen(f"Game Assets/space_{self.resolution}.png", confidence=.7) is not None:
            self.in_game = True
            pydirectinput.press("space")
        elif pyautogui.locateOnScreen(f"Game Assets/scoreboard_{self.resolution}.png", confidence=.7) is not None:
            self.in_game = True
            pydirectinput.press("escape")
        elif pyautogui.locateOnScreen(f"Game Assets/Esc_{self.resolution}.png", confidence=.7) is not None:
            self.in_game = True
            pydirectinput.press("escape")
        elif pyautogui.locateOnScreen(f"Game Assets/EscCloseLong_{self.resolution}.png", confidence=.7) is not None:
            self.in_game = True
            pydirectinput.press("escape")
        # 开始排队
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            self.queue_into_game()
            self.in_game = False
        # 从死亡画面返回主菜单
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            self.go_to_lobby()
            self.in_game = False
        # 单击在Apex首次启动时出现的“继续”按钮
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # 当弹出窗口出现在屏幕上时按下ESC键
        elif pyautogui.locateOnScreen(f"Game Assets/escape{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # 在发生错误时，例如断开连接时，使用户重新进入游戏
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    def kd_lowering(self, interact_key, tactical_key):
        # 检查Apex是否正在运行
        if "r5apex.exe" not in [p.name() for p in process_iter()]:
            pass
        # 通过跳跃并使用他们的战术技能使玩家更加显眼，防止他们因挂机而被踢出游戏
        elif pyautogui.locateOnScreen(f"Game Assets/in_game_constant{self.resolution}.png", confidence=.8) is not None:
            self.in_game = True
            pydirectinput.press("space")
            sleep(randint(0, 10))
            pydirectinput.press(tactical_key)
        # 开始排队
        elif pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8) is not None:
            self.queue_into_game()
            self.in_game = False
        # 尝试选择地平线，然后是直布罗陀
        elif pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.7) is not None:
            try:
                button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/horizon{self.resolution}.png", confidence=.8))
                pydirectinput.click(button_cords.x, button_cords.y)
            except:
                print("未找到 地平线 坐标")
                if pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.7) is not None:
                    try:
                        button_cords = pyautogui.center(pyautogui.locateOnScreen(f"Game Assets/gibraltar{self.resolution}.png", confidence=.8))
                        pydirectinput.click(button_cords.x, button_cords.y)
                    except:
                        print("未找到 直布罗陀 坐标")
        # 在通常有许多玩家的区域，从发射船上让用户降落
        elif pyautogui.locateOnScreen(f"Game Assets/launch{self.resolution}.png", confidence=.7) is not None:
            sleep(3)
            pydirectinput.press(interact_key)
            pydirectinput.moveTo(990, 985, 0.5)
            pydirectinput.keyDown("w")
            sleep(15)
            pydirectinput.keyUp("w")
        # 从死亡画面返回主菜单
        elif pyautogui.locateOnScreen(f"Game Assets/squad_eliminated_constant{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/leave_match_constant{self.resolution}.png", confidence=.8) is not None:
            self.go_to_lobby()
            self.in_game = False
        # 单击在Apex首次启动时出现的“继续”按钮
        elif pyautogui.locateOnScreen(f"Game Assets/continue_constant{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.click()
            self.in_game = False
        # 当弹出窗口出现在屏幕上时按下ESC键
        elif pyautogui.locateOnScreen(f"Game Assets/escape{self.resolution}.png", confidence=.8) is not None:
            pydirectinput.press("escape")
            self.in_game = False
        # 在出现错误时，例如断开连接时，使用户重新进入游戏
        elif pyautogui.locateOnScreen(f"Game Assets/continue_error{self.resolution}.png", confidence=.8) is not None or pyautogui.locateOnScreen(f"Game Assets/continue_error2_{self.resolution}.png", confidence=.8):
            pydirectinput.press("escape")
            self.in_game = False
        else:
            self.in_game = False

    # 从主菜单排队进行匹配
    def queue_into_game(self):
        try:
            print("正在尝试排队进入游戏")
            if pyautogui.locateOnScreen(f"Game Assets/fill_teammates{self.resolution}.png", confidence=.6) is not None:
                self.tries_to_find_fill_button = 0
                fill_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/fill_teammates{self.resolution}.png", confidence=.6))
                pydirectinput.click(fill_button_cords.x, fill_button_cords.y)
                sleep(1)
                ready_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
            else:
                self.tries_to_find_fill_button += 1
                sleep(1)

            if self.tries_to_find_fill_button >= 5:
                self.tries_to_find_fill_button = 0
                ready_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/ready_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(ready_button_cords.x, ready_button_cords.y)
        except:
            print("无法找到“填充”和/或“准备”按钮，并加载游戏时出现错误")

    # 按照正确的顺序输入点击和按键，从死亡画面返回到大厅
    def go_to_lobby(self):
        if self.resolution == "HD":
            pydirectinput.press("space")
            sleep(1)
            if pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            elif pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            sleep(7)
            pydirectinput.click(850, 716)
            pydirectinput.press("space")
            sleep(2)
            pydirectinput.press("space")
            sleep(1)
            pydirectinput.press("space")
            sleep(1)
            pydirectinput.press("space")
        else:
            pydirectinput.press("space")
            sleep(1)
            if pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            elif pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8) is not None:
                yes_button_cords = pyautogui.center(
                    pyautogui.locateOnScreen(f"Game Assets/yes_button2_{self.resolution}.png", confidence=.8))
                pydirectinput.click(yes_button_cords.x, yes_button_cords.y)
            sleep(7)
            pydirectinput.click(1231, 955)
            pydirectinput.press("space")
            sleep(2)
            pydirectinput.press("space")
            sleep(1)
            pydirectinput.press("space")
            sleep(1)
            pydirectinput.press("space")
            sleep(1)
            pydirectinput.press("space")
