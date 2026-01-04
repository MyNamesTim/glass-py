import os, sys, time, platform
from datetime import datetime
import tkinter
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

opsys = platform.system()

if opsys == "Windows":
    username = os.environ.get('USERNAME')
    init_path = os.path.expanduser("~/Pictures")
elif opsys == "Linux":
    import getpass
    username = getpass.getuser()
    init_path = os.path.expanduser("~/Documents")
elif opsys == "Darwin":
    username = os.getlogin()
    init_path = os.path.expanduser("~/Documents")
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

scale = float(input("What scale would you like the image to be? (0.00-1.00)"))
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

screen_w = t.winfo_screenwidth()
screen_h = t.winfo_screenheight()
t.geometry(f'{screen_w}x{screen_h}+0+0')
t.attributes("-alpha", 0.01)

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
    t.attributes("-alpha", 1.0)
    t.unbind("<Button-1>")
    print(f'Window positioned at {x}, {y}')

t.bind("<Button-1>", setpos)
t.mainloop()
