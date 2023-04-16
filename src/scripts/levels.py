import tkinter as tk
import tkinter.font as fnt

import config

app = tk.Tk()
app.geometry("500x100") # make this bigger as you add more presets
app.eval("tk::PlaceWindow . center")

def run_command(level):
    app.destroy()  # close dialog

    if config.os_is("Darwin"): # mac
        config.run_shell(
            "path/to/idasen-controller --move-to " + level + " > /dev/"
        )
    elif config.os_is("Windows"): # windows
        config.run_shell(
            r"path\to\idasen-controller.exe --move-to "
            + level
            + " > "
        )
    else:
        config.not_supported()

# levels: config/config.yaml
tk.Button(
        app, text="Cancel", font=fnt.Font(size=15), command=exit
    ).pack(side=tk.RIGHT, padx=20, pady=5)

levels = ["sit-", "sit+", "stand", "stand+"] # add here the presets names

for level in levels:
    tk.Button(
        app, text=level, font=fnt.Font(size=15), command=lambda m=level: run_command(m)
    ).pack(side=tk.LEFT, padx=10, pady=5)

app.mainloop()
