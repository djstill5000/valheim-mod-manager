# Valheim-Mod-Manager

CLI-based Valheim mod manager to be used in conjunction with [r2modman](https://thunderstore.io/package/ebkr/r2modman/) on Linux based systems.

## Who Should Use This?

 Linux users who have encountered problems trying to download mods from the Thunderstore webpage, or through the r2modman client -- Recieving the `Network Error Bug` message, or some other variation of it when trying to download a mod.

*Note:* If you not are using Linux, or are not experiencing this specific bug, I'd recommend you use [Thunderstore Mod Manager](https://www.overwolf.com/app/thunderstore-thunderstore_mod_manager) instead - as setup and maintenance of mods will be much smoother, however, in theory this script should work on any OS if you wish to use it.

### Preface

The installation procedure assumes the following:
  - You are using an Arch-based distro
  - You are using `paru` as your AUR helper
  - You use the given conda environment to resolve Python dependencies
  - You use `r2modman` to obtain `BepInEx` and format your file structure, as opposed to a manual install.
    
None of these are requirements, but I won't be explicitly demonstrating any alternative method of install.
## Requirements

Ensure your packages are up-to-date:
```
sudo pacman -Syu
paru -Syu
```

```
paru -S r2modman
```

```
conda env create -f environment.yml
```

## Setup + Configuration
1. Open r2modman and create a profile
2. Install BepInEx
3. Copy the directory to the plugins folder in r2modman and save it to `mods_dir` in `config.ini`.

## Usage
1. To add new mods, just copy the link to a mod on the Thunderstore website (ex. [Jotunn](https://thunderstore.io/c/valheim/p/ValheimModding/Jotunn/)) and paste it into `mods.csv`, which is located in the same directory that you downloaded this project.
2. Ensure that the mod links are placed vertically on top of one another, and not side by side or they will not be read correctly.
3. Once you have all of the mods that you would like to play with, activate the conda environment
```
conda activate vmm
```
4. Execute the script, and all of the mods will be downloaded and automatically placed into your r2modman plugins folder
```
sudo python getmods.py
```
5. To play, open r2modman and navigate to the profile you created and select `Start Modded`
