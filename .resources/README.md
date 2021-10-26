## Resources
*Scripts, software, commands, packages, etc...*

## After Install Arch Linux
- AMD Drivers
  - [xf86-video-amdgpu](https://archlinux.org/packages/extra/x86_64/xf86-video-amdgpu/)
  - [amd-ucode](https://archlinux.org/packages/core/any/amd-ucode/)
  - [xf86-video-ati](https://archlinux.org/packages/extra/x86_64/xf86-video-ati/)

- bspwm
  - [bspwm](https://archlinux.org/packages/community/x86_64/bspwm/)
  - [sxhkd](https://archlinux.org/packages/community/x86_64/sxhkd/)
    - [bspwm Setup](https://wiki.archlinux.org/title/Bspwm)

- Qtile
  - [qtile](https://archlinux.org/packages/community/x86_64/qtile/)
  - [python-setuptools](https://archlinux.org/packages/extra/any/python-setuptools/)
  - [python-psutil](https://archlinux.org/packages/community/x86_64/python-psutil/)
  - [python-iwlib](https://archlinux.org/packages/community/x86_64/python-iwlib/)

- Packages
  - [alacritty](https://archlinux.org/packages/community/x86_64/alacritty/)
  - [lightdm](https://archlinux.org/packages/extra/x86_64/lightdm/)
  - [lightdm-gtk-greeter](https://archlinux.org/packages/extra/x86_64/lightdm-gtk-greeter/)
    - [LightDM Setup](https://wiki.archlinux.org/title/LightDM#Greeter)
  - [neofetch](https://archlinux.org/packages/community/any/neofetch/)
  - [picom](https://archlinux.org/packages/community/x86_64/picom/)
  - [feh](https://archlinux.org/packages/extra/x86_64/feh/)
  - [rofi](https://archlinux.org/packages/community/x86_64/rofi/)
  - [papirus-icon-theme](https://archlinux.org/packages/community/any/papirus-icon-theme/)
  - [htop](https://archlinux.org/packages/extra/x86_64/htop/)
  - [zsh](https://archlinux.org/packages/extra/x86_64/zsh/)
  - [zsh-autosuggestions](https://archlinux.org/packages/community/any/zsh-autosuggestions/)
  - [zsh-syntax-highlighting](https://archlinux.org/packages/community/any/zsh-syntax-highlighting/)
    - [Zsh Setup](https://wiki.archlinux.org/title/Zsh#Making_Zsh_your_default_shell)

- Desktop
  - [firefox](https://archlinux.org/packages/extra/x86_64/firefox/)
  - [telegram-desktop](https://archlinux.org/packages/community/x86_64/telegram-desktop/)
  - [opera](https://archlinux.org/packages/community/x86_64/opera/)
  - [opera-ffmpeg-codecs](https://archlinux.org/packages/community/x86_64/opera-ffmpeg-codecs/)
  - [gnome-screenshot](https://archlinux.org/packages/extra/x86_64/gnome-screenshot/)
  - [lxappearance](https://archlinux.org/packages/community/x86_64/lxappearance/)
  - [libreoffice-fresh](https://archlinux.org/packages/extra/x86_64/libreoffice-fresh/)
  - [gpicview](https://archlinux.org/packages/community/x86_64/gpicview/)
  - [thunar](https://archlinux.org/packages/extra/x86_64/thunar/)
  - [thunar-volman](https://archlinux.org/packages/extra/x86_64/thunar-volman/)
  - [vlc](https://archlinux.org/packages/extra/x86_64/vlc/)

- Hardware
  - [ntp](https://archlinux.org/packages/extra/x86_64/ntp/)
  - [brightnessctl](https://archlinux.org/packages/community/x86_64/brightnessctl/)
  - [playerctl](https://archlinux.org/packages/community/x86_64/playerctl/)
  - [pulseaudio](https://archlinux.org/packages/extra/x86_64/pulseaudio/)
    - Enable it: `systemctl --user enable pulseaudio`
  - [yay -S pulseaudio-ctl](https://aur.archlinux.org/packages/pulseaudio-ctl/)

- Neovim
  - [neovim](https://archlinux.org/packages/community/x86_64/neovim/)
  - [yay -S neovim-plug-git](https://aur.archlinux.org/packages/neovim-plug-git)
  - [nodejs](https://archlinux.org/packages/community/x86_64/nodejs/)
  - [yarn](https://archlinux.org/packages/community/any/yarn/)
  - [python-pynvim](https://archlinux.org/packages/community/any/python-pynvim/)

- Fonts
  - [nerd-fonts-ubuntu-mono](https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono)
  - [nerd-fonts-mononoki](https://aur.archlinux.org/packages/nerd-fonts-mononoki)

- Yay
  - [visual-studio-code-bin](https://aur.archlinux.org/packages/visual-studio-code-bin)
  - [update-grub](https://aur.archlinux.org/packages/update-grub/)
  - [evince-no-gnome](https://aur.archlinux.org/packages/evince-no-gnome/)
  - [whatsapp-nativefier](https://aur.archlinux.org/packages/whatsapp-nativefier/)

- VirtualBox
  - [virtualbox](https://archlinux.org/packages/community/x86_64/virtualbox/)
  - [virtualbox-host-modules-arch](https://archlinux.org/packages/community/x86_64/virtualbox-host-modules-arch/)
  - [virtualbox-guest-iso](https://archlinux.org/packages/community/any/virtualbox-guest-iso/)
  - Setup:
```
sudo modprobe vboxdrv vboxnetadp vboxnetflt vboxpci
sudo nano /etc/modules-load.d/virtualbox.conf
sudo gpasswd -a $USER vboxusers
```
