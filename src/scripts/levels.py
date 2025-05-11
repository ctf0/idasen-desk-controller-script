import config
import yaml
import tkinter as tk
import tkinter.font as fnt

app = tk.Tk()
app.geometry("600x100") # make this bigger as you add more presets
app.eval("tk::PlaceWindow . center")

# get levels
def read_config_file():
    if config.os_is("Darwin"):
        path = os.path.expanduser('~/Library/Application Support/linak-controller/config.yaml')
    elif config.os_is("Windows"):
        path = r'C:\Users\<user>\AppData\Local\linak-controller\linak-controller\config.yaml'
    else:
        config.not_supported()
        return None

    with open(path, 'r') as file:
        return yaml.safe_load(file)

data = read_config_file()
levels = list(data.get('favourites', {}).keys()) if data else []

# exec controller
def run_command(level):
    app.destroy()  # close dialog

    if config.os_is("Darwin"):  # mac
        config.run_shell(
            "path/to/linak-controller --move-to " + level + " > /dev/"
        )
    elif config.os_is("Windows"):
        config.run_shell(
            r"path\to\linak-controller.exe --move-to " + level + " > "
        )
    else:
        config.not_supported()

# add btns
tk.Button(app, text="Cancel", font=fnt.Font(size=15), command=exit).pack(side=tk.RIGHT, padx=20, pady=5)

for level in levels:
    tk.Button(app, text=level, font=fnt.Font(size=15), command=lambda m=level: run_command(m)).pack(side=tk.LEFT, padx=10, pady=5)

app.mainloop()
