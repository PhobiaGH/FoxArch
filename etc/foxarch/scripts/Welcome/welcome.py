from tkinter import *
from PIL import ImageTk, Image
import matplotlib
matplotlib.use('Agg')

splash_root = Tk()
splash_root.grid_rowconfigure(8, weight=1)
splash_root.grid_columnconfigure((0, 1, 2), weight=1)
splash_root.resizable(width=True, height=True)
splash_root.title('Welcome')

# Add image file 
bg = PhotoImage(file = "/etc/foxarch/scripts/Welcome/resources/images/background.png") 
  
# Show image using label 
bgl = Label( splash_root, image = bg) 
bgl.place(x = 0, y = 0)

splash_label_welcome = Label(splash_root, text="Welcome to FoxArch!", font=("Helvetica", 24), fg = "#ffffff", bg = "#333333")

img_icon = Image.open("resources/images/fox0.png")
img_icon = img_icon.resize((150, 150))
img_icon = ImageTk.PhotoImage(img_icon)
panel = Label(splash_root, image=img_icon, bg = "black")
panel.image = img_icon
panel.grid(row=0, column=1)

splash_label_about = Label(text="About:", fg = "#ffffff", bg = "#333333")

splash_label_workflow = Label(text="""FoxArch is designed around the idea of fluent workflow. Never taking your hands off of the keyboard, and zooming around your projects 
like never before. Harness the power of flow with Hyprland, and an extensive set of pentesting tools built off of a bare bones Arch base. FoxArch has more flow than All-State!""", font=("Helvetica", 14), fg = "#ffffff", bg = "#333333")

img_kb = Image.open("resources/images/keyboard-icon.png")
img_kb = img_kb.resize((140, 140))
img_kb = ImageTk.PhotoImage(img_kb)
headline = Label(splash_root, image=img_kb, fg = "#ffffff", bg = "#333333")
headline.image = img_kb

splash_label_layout = Label(text="Keyboard Layout", font=("Helvetica", 18), fg = "#ffffff", bg = "#333333")

splash_label_bindings = Label(text="Bindings:", font=("Helvetica", 14), fg = "#ffffff", bg = "#333333")

splash_label_bind = Label(text="""
    SUPER+Q
    SUPER+E
    SUPER+R
    SUPER+T
    SUPER+O
    SUPER+P
    SUPER+S
    SUPER+F
    SUPER+J
    SUPER+L
    SUPER+C
    SUPER+V
    SUPER+B
    SUPER+Tab
    SUPER+SHIFT+M
    SUPER+SHIFT+W
""", fg = "#ffffff", bg = "#333333")

splash_label_actions = Label(text="Actions:", font=("Helvetica", 14), fg = "#ffffff", bg = "#333333")

splash_label_action = Label(text="""
    Logout Menu
    VSCode
    Run (Apps List)
    Terminal
    Tor Browser
    Change Window Size
    Dim Screen
    File Explorer
    Orientate Windows
    Lock Screen
    Close Current Window
    Float/Dynamic Window
    Brave Browser
    Notifications
    Logout Immediately
    Reset Waybar
""", fg = "#ffffff", bg = "#333333")

splash_label_welcome.grid(row=1, column=1, pady=10)
splash_label_about.grid(row=2, column=1)
splash_label_workflow.grid(row=3, column=1, padx=10, pady=30)
headline.grid(row=4, column=1, padx=10)
splash_label_layout.grid(row=5, column=1, padx=20, pady=10)
splash_label_bindings.grid(row=6, column=0, padx=20, pady=10)
splash_label_actions.grid(row=6, column=2, padx=20, pady=10)
splash_label_bind.grid(row=7, column=0, padx=20, pady=10)
splash_label_action.grid(row=7, column=2, padx=20, pady=10)

#def remove_autostart():
#    if (var1.get() == 1):
#        
#    else:

#var1 = tk.IntVar()
#cb = tk.Checkbutton(splash_root, text="To stop this from auto starting at login, check this box.", onvalue=1, offvalue=0, command=remove_autostart)
#cb.grid(row=8, column=1)




splash_root.mainloop()
