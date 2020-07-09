import tkinter as tk
import mainApp as app

if(__name__ == "__main__"):
    root = tk.Tk()
    app.MainApplication(root).pack()
    root.mainloop()