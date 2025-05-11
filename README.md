# Idasen Desk Controller UI

this is a complementary cross-platform script for the excellent controller by [rhyst](https://github.com/rhyst)/[idasen-controller](https://github.com/rhyst/linak-controller)

sadly idasen doesnt have a native controller under any pc platform, only mobile.

also as i got tired of always having to either use the mobile app "which doesn't connect most of the time" or manually move the desk, so i decided to make this script to automate the movement as much as possible. (excuse my python, its a quick couple of hours work)

>atm the script supports `win & mac` but no linux as i dont have it installed however you can easily add it, please check `src/scripts/levels.py`.

## Setup

please check the [original controller repo](https://github.com/rhyst/linak-controller) first for the setup.

## Usage

1. configure the presets you want to select from, inside `config/config.yml`
2. copy `src/scripts` somewhere on your machine
    - update all the `path/to` inside `src/scripts/levels.py` with the correct path
    - next create a shortcut or some file that run the `levels.py` file

        ```shell
        python path\to\levels.py
        ```

3. if everything is done correctly, running the previous command above should show up a popup with the presets as buttons to chose from.

### Limitations

idasen desk controller doesn't support pairing with multiple devices/platforms at the same time, check [issue/54](https://github.com/rhyst/idasen-controller/issues/54)
