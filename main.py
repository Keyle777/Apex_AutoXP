from tkinter import Tk, Label, PhotoImage, Button
from threading import Thread
from bot_functions import *
from other_functions import *
from psutil import process_iter

# 创建窗口对象
root = Tk()

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口大小
root.geometry(f"800x600+{screen_width//2-400}+{screen_height//2-300}")
root.maxsize(800, 600)
root.minsize(800, 600)

# 是否有其他窗口设置
root.title("Apex自动挂机机器人")
root.iconbitmap("ApexPredators_Logo.ico")
root.configure(background='white')

# 创建所有标签并将它们添加到窗口
title_label = Label(root, text="Apex自动挂机机器人", background="white", font=("Helvetica", 30, "bold"))
label1 = Label(root, text="您在Apex中的分辨率是多少?", background="white", font=("Helvetica", 15, "bold"))
label2 = Label(root, text="(默认使用您的显示器分辨率)", background="white", font=("Helvetica", 15, "bold"))
label3 = Label(root, text="您想以哪种模式自动挂机?", background="white", font=("Helvetica", 15, "bold"))
label4 = Label(root, text="", background="white", foreground="#ff4c4c", font=("Helvetica", 15, "bold"))
title_label.place(relx=.5, rely=.075, anchor="center")
label1.place(relx=.5, rely=.225, anchor="center")
label2.place(relx=.5, rely=.3, anchor="center")
label3.place(relx=.5, rely=.6, anchor="center")
label4.place(relx=.5, rely=.535, anchor="center")

# 获取按钮的所有图像
image1 = PhotoImage(file="GUI Assets/button1.png")
image2 = PhotoImage(file="GUI Assets/button2.png")
image3 = PhotoImage(file="GUI Assets/button3.png")
image4 = PhotoImage(file="GUI Assets/button4.png")
image5 = PhotoImage(file="GUI Assets/button5.png")
image5_2 = PhotoImage(file="GUI Assets/button5_2.png")
image1_pressed = PhotoImage(file="GUI Assets/button1_pressed.png")
image2_pressed = PhotoImage(file="GUI Assets/button2_pressed.png")
image3_pressed = PhotoImage(file="GUI Assets/button3_pressed.png")
image4_pressed = PhotoImage(file="GUI Assets/button4_pressed.png")
image5_pressed = PhotoImage(file="GUI Assets/button5_pressed.png")
image5_2_pressed = PhotoImage(file="GUI Assets/button5_2_pressed.png")

# 为按键绑定创建文本字段
entry1 = create_custom_entry(root=root, placeholder_text="输入您的交互按键（默认为 E）")
entry2 = create_custom_entry(root=root, placeholder_text="输入你的战术键（默认为 Q）")

res_button_pressed = ""
mode_button_pressed = 0
start_pressed = 0


# 定义确定按下按钮时会发生什么的函数
# 未按下按钮的十六进制代码是 #ff4c4c
# 按下按钮的十六进制代码是 #ff7e7e
def button1_pressed():
    button1.configure(image=image1_pressed)
    button2.configure(image=image2)
    global res_button_pressed
    res_button_pressed = "HD"
    print("分辨率设置为 1080p")


def button2_pressed():
    button2.configure(image=image2_pressed)
    button1.configure(image=image1)
    global res_button_pressed
    res_button_pressed = "2K"
    print("分辨率设置为 1440p")


def button3_pressed():
    button3.configure(image=image3_pressed)
    button4.configure(image=image4)
    global mode_button_pressed
    mode_button_pressed = 3
    print("模式设置为降低 KD ")
    entry1.place(relx=.5, rely=.75, anchor="center")
    entry2.place(relx=.5, rely=.8, anchor="center")
    label3.place(relx=.5, rely=.57, anchor="center")
    label4.place(relx=.5, rely=.515, anchor="center")
    button3.place(relx=.35, rely=.655, anchor="center")
    button4.place(relx=.65, rely=.655, anchor="center")


def button4_pressed():
    button4.configure(image=image4_pressed)
    button3.configure(image=image3)
    global mode_button_pressed
    mode_button_pressed = 4
    print("模式设置为获取 XP ")
    # 将 GUI 恢复为默认值 - 除非之前按下按钮 3，否则不会显示任何不同
    label1.place(relx=.5, rely=.225, anchor="center")
    label2.place(relx=.5, rely=.3, anchor="center")
    label3.place(relx=.5, rely=.6, anchor="center")
    label4.place(relx=.5, rely=.535, anchor="center")
    button1.place(relx=.35, rely=.425, anchor="center")
    button2.place(relx=.65, rely=.425, anchor="center")
    button3.place(relx=.35, rely=.725, anchor="center")
    button4.place(relx=.65, rely=.725, anchor="center")
    button5.place(relx=.5, rely=.9, anchor="center")
    entry1.place_forget()
    entry2.place_forget()


running = False
def button5_pressed():
    global running
    running = not running
    if res_button_pressed == "" or mode_button_pressed == 0:
        label4.configure(text="您必须选择模式和分辨率")
        running = False
    elif mode_button_pressed == 3 and (len(entry1.get()) > 1 and entry1.get() != entry1.placeholder) or (len(entry2.get()) > 1 and entry2.get() != entry2.placeholder):
        label4.configure(text="您只能输入一个字符")
        running = not running
    elif running:
        label4.configure(text="")
        button5.configure(image=image5_pressed)
        root.update()
        print("启动机器人")
        root.after(1000, button5.configure(image=image5_2))
        root.update()
        t1 = Thread(target=launch_bot)
        t1.start()
    else:
        button5.configure(image=image5_2_pressed)
        root.update()
        print("关闭机器人")
        root.after(1000, button5.configure(image=image5))
        root.update()


# 启动机器人
def launch_bot():
    apex_bot = ApexBot(res_button_pressed)
    while True:
        if not running:
            break
        if "r5apex.exe" in [p.name() for p in process_iter()]:
            if mode_button_pressed == 4:
                apex_bot.xp_grinding()
            else:
                interact = entry1.get()
                tactical = entry2.get()
                if entry1.get() == entry1.placeholder:
                    interact = "e"
                if entry2.get() == entry2.placeholder:
                    tactical = "q"
                apex_bot.kd_lowering(interact_key=interact.lower(), tactical_key=tactical.lower())


# 创建所有按钮并将它们添加到窗口
button1 = Button(root, image=image1, borderwidth=0, foreground="white", command=button1_pressed)
button2 = Button(root, image=image2, borderwidth=0, foreground="white", command=button2_pressed)
button3 = Button(root, image=image3, borderwidth=0, foreground="white", command=button3_pressed)
button4 = Button(root, image=image4, borderwidth=0, foreground="white", command=button4_pressed)
button5 = Button(root, image=image5, borderwidth=0, foreground="white", command=button5_pressed)
button1.place(relx=.35, rely=.425, anchor="center")
button2.place(relx=.65, rely=.425, anchor="center")
button3.place(relx=.35, rely=.725, anchor="center")
button4.place(relx=.65, rely=.725, anchor="center")
button5.place(relx=.5, rely=.9, anchor="center")


def close_window():
    global running
    running = False
    root.destroy()


root.protocol("WM_DELETE_WINDOW", close_window)

root.mainloop()
