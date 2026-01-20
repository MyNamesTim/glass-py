import os, sys, time, platform
from datetime import datetime
import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

opsys = platform.system()

if opsys == "Windows":
    username = os.environ.get('USERNAME')
    init_path = os.path.expanduser("~/Pictures")

    import ctypes
    user32 = ctypes.windll.user32
    SM_XVIRTUALSCREEN = 76
    SM_YVIRTUALSCREEN = 77
    SM_CXVIRTUALSCREEN = 78
    SM_CYVIRTUALSCREEN = 79
    vx = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
    vy = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
    vw = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
    vh = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
elif opsys == "Linux":
    import getpass
    username = getpass.getuser()
    init_path = os.path.expanduser("~/Documents")
elif opsys == "Darwin":
    username = os.getlogin()
    init_path = os.path.expanduser("~/")
else:
    print("Unsupported OS detected.")
    input("Press enter to exit...")
    sys.exit()

time = datetime.now().time()
if time.hour <= 12:
    if username:
        print(f'Good morning, {username}!')
    else:
        print("Good morning!")
elif time.hour > 12:
    if username:
        print(f'Good afternoon, {username}!')
    else:
        print("Good afternoon!")

while True:
    scale = float(input("What scale would you like the image to be? 1.00 is the original image scale.\n"))
    if scale < 0.0 or scale > 1.0:
        scale_confirm = input(
            "The scale that you have entered is abnormal and may lead to a loss of detail (artifacts, pixelation, and blurring) due to upscaling. Negative numbers can cause crashes.\n\n"
            "Are you sure that you would like this scale? (Y/N)\n"
        ).lower()
        if scale_confirm == "n":
            print("What is the new scale that you would like?")
            continue
        else:
            print("Confirmed.")
            break
    else:
        break

while True:
    alpha = float(input("What opacity would you like the image to be? (0.00 - 1.00)\n"))
    if alpha < 0.0 or alpha > 1.00:
        print("The opacity that you entered was invalid. Try again.\n")
        continue
    else:
        break

print("Please select an image.")
path = filedialog.askopenfilename(
        title="Select a file",
        initialdir=init_path,
        filetypes=[("All files", "*.*")]
    )

if not path:
    sys.exit()

og_img = Image.open(path)
w = int(og_img.width * scale)
h = int(og_img.height * scale) 
img = og_img.resize((w, h), Image.LANCZOS)

t = tkinter.Tk()
t.overrideredirect(True)
t.wm_attributes("-topmost", True)

if opsys == "Windows":
    import ctypes
    user32 = ctypes.windll.user32
    SM_XVIRTUALSCREEN = 76
    SM_YVIRTUALSCREEN = 77
    SM_CXVIRTUALSCREEN = 78
    SM_CYVIRTUALSCREEN = 79
    vx = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
    vy = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
    screen_w = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
    screen_h = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
else:
    vx = 0
    vy = 0
    screen_w = t.winfo_screenwidth()
    screen_h = t.winfo_screenheight()

t.geometry(f'{screen_w}x{screen_h}+{vx}+{vy}')
t.attributes("-alpha", 0.05)

canvas = tkinter.Canvas(t, width=w, height=h, highlightthickness=0)
canvas.pack()

photo = ImageTk.PhotoImage(img)
canvas.config(width=w, height=h)
canvas.create_image(0, 0, anchor="nw", image=photo)
canvas.image = photo

print("Please set window position using left click.")
def setpos(event):
    x, y = event.x_root, event.y_root
    t.geometry(f'{w}x{h}+{x}+{y}')
    t.attributes("-alpha", alpha)
    t.unbind("<Button-1>")
    print(f'Reference positioned at {x}, {y}')

t.bind("<Button-1>", setpos)
t.mainloop()

