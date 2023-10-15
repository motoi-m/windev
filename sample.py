import tkinter
from tkinter import ttk


class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=420, height=320, borderwidth=4, relief="groove")
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widget()

    def create_widget(self):
        quit_btn = tkinter.Button(self)
        quit_btn["text"] = "閉じる"
        quit_btn["command"] = self.root
        quit_btn.pack(side="bottom")


root = tkinter.Tk()
root.title("サンプルアプリ")
root.geometry("400x300")
app = Application(root=root)
root.mainloop()

"""
# rootメインウィンドウの設定
root = tk.Tk()
root.title("application")
root.geometry("200x100")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(padx=20, pady=10)

# 各種ウィジェットの作成
button = tk.Button(frame, text="tkinter")
button_ttk = ttk.Button(frame, text="ttk")
# 各種ウィジェットの設置
button.grid(row=0, column=0, padx=5)
button_ttk.grid(row=0, column=1)

root.mainloop()
"""
