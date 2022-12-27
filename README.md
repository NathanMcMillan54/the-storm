# The Storm

A small 2D sandbox game that occasionally gets interrupted by a storm.

## Supported:

- Linux
 - x86_64
- Windows 10 - 11

## Install:

### Linux:

The Storm is only supported on x86_64 Linux devices.

To install The Storm for Linux clone this repositiory and run the install file:
```commandline
git clone https://github.com/NathanMcMillan54/the-storm.git
cd the-storm/
sh install.sh # sudo is required for this
```

After running ``install.sh`` there should be a file on your desktop named ``The_Storm.desktop``, right-click on it and select "Allow Launching".

If you're running a WSL and don't have a desktop you can run The Storm with this command:
```commandline
TheStorm.linux.x86_64
```

### Windows 10 - 11:

If you're running a Windows version that supports WSL (Windows Subsystem for Linux) you can run the Linux executable for The Storm in the WSL.
Open PowerShell or Windows Command Prompt as an administrator amd run these commands:

```commandline
wsl --install
```

After running this restart your device to apply the changes. After restarting, install the latest version of Ubuntu (22.04) on the Microsoft
Store. It can run as a command (``ubuntu``) or an app, after running it and setting up the user follow the install instructions for Linux.


