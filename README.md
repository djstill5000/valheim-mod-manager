# Valheim-Mod-Manager

Simple CLI-based Valheim mod manager made in response to the `Network Error Bug` that many Linux users seem to experience -- making it __impossible__ to download certain mods on Linux machines. This script is designed to be used with [r2modman](https://thunderstore.io/package/ebkr/r2modman/) as a GUI and launcher, and is currently compatible with **all** mods available on [thunderstore.io](https://thunderstore.io/c/valheim/).

## Who Should Use This?

Any Linux user who is encountering problems with being able to download mods may find this useful, specifically the `Network Error Bug` that I have experienced on multiple Arch-based machines.

*Note:* If you not are using Linux, or are not experiencing this specific bug, I'd recommend you use [Thunderstore Mod Manager](https://www.overwolf.com/app/thunderstore-thunderstore_mod_manager) instead - as setup and maintenance of mods will be much smoother.

## Requirements

1. Python version > 3.0.0 must be installed
2. Install [conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) package manager
3. Install [r2modman](https://thunderstore.io/package/ebkr/r2modman/)
4. Resolve dependencies by executing the following in the project directory
   ```
   conda env create -f environment.yml
   ```

## Setup + Configuration
1. Open **r2modman** and create a profile
2. Download `BepInExPack_Valheim` under the **online** tab (It should be pinned as the first mod by default)
3. In r2modman select _Settings -> Browse profile folder_ and copy this directory (It should look something like "~/.config/r2modmanPlus-local/Valheim/profiles/YOUR_PROFILE_NAME")
4. Open `config.ini` in the project directory and change `mods_dir` to be your copied directory from above, so that your config.ini file looks like
   ```
   [PARAMETERS]
   mods_dir = YOUR_DIRECTORY_HERE
   mods_csv = mods.csv
   ```

## Usage

### Adding Mods

Adding mods is as easy as copying the URL for the modpage on the Thunderstore website and pasting it into the `mods.csv` file in the project directory, for example to add [Jotunn](https://thunderstore.io/c/valheim/p/ValheimModding/Jotunn/), [CreatureLevelAndLootControl](https://thunderstore.io/c/valheim/p/Smoothbrain/CreatureLevelAndLootControl/), and [PlantEverything](https://thunderstore.io/c/valheim/p/Smoothbrain/CreatureLevelAndLootControl/) your mods.csv will look like
   ```
   https://thunderstore.io/c/valheim/p/ValheimModding/Jotunn/
   https://thunderstore.io/c/valheim/p/Smoothbrain/CreatureLevelAndLootControl/
   https://thunderstore.io/c/valheim/p/Advize/PlantEverything/
   ```
_Note: Make sure you also add the other mod dependencies for the mods that you add!_

### Removing Mods

To remove mods just delete the corresponding webpage URL in `mods.csv`, in the above example we can remove [CreatureLevelAndLootControl](https://thunderstore.io/c/valheim/p/Smoothbrain/CreatureLevelAndLootControl/) by simply removing it's URL
   ```
   https://thunderstore.io/c/valheim/p/ValheimModding/Jotunn/
   https://thunderstore.io/c/valheim/p/Advize/PlantEverything/
   ```

### Downloading Mods

Once you've modified your `mods.csv` file to your liking, you can run the script to actually install them. First ensure that you are in the conda environment
 ```
conda activate vmm
 ```
Then in the project directory run
```
sudo python getmods.py
```
_Note: This may take a while depending on how many mods you've installed and your internet download speed!_


### Updating Mods

To update mods to their latest version, all you need to do is run the script again
```
sudo python getmods.py
```
_Note: Remember to execute this command in the conda env_ `vmm`

## Launching the Game

After you've run the script to install the mods you're ready to play! In r2modman just go to your profile that you've installed the mods for and click `start modded`.
