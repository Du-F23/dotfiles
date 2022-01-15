## Installation (UEFI)

1. Download the ISO file
   - [Download](https://archlinux.org/download/)
   - Make a bootable USB
   - Reboot

2. Set the keyboard layout (Optional)
```
loadkeys us
```

3. Verify the boot mode (Optional)
```
ls /sys/firmware/efi/efivars
```

4. Connect to the internet
   - Make sure the card is not blocked: `rfkill list`
     - If the card is not hard-blocked but soft-blocked: `rfkill unblock wifi`
   - Connect to the network: `iwctl`
     - List all Wi-Fi devices: `device list`
     - Scan networks: `station wlan0 scan`
     - List all available networks: `station wlan0 get-networks`
     - Connect to a network: `station wlan0 connect SSID`
   - Verify connection: `ping archlinux.org`

5. Partition the disks
   - List disks: `fdisk -l`
   - Create partitions: `cfdisk`

6. Format the partitions
   - Boot: `mkfs.vfat -F32 /dev/sda1`
   - Swap: `mkswap /dev/sda2`
     - Enable it: `swapon /dev/sda2`
   - Root: `mkfs.ext4 /dev/sda3`
   - Home: `mkfs.ext4 /dev/sda4`

7. Mount the file systems
   - Root: `mount /dev/sda3 /mnt`
   - Boot:
     - `mkdir -p /mnt/boot/efi`
     - `mount /dev/sda1 /mnt/boot/efi`
   - Home:
     - `mkdir /mnt/home`
     - `mount /dev/sda4 /mnt/home`

8. Install essential packages
```
pacstrap /mnt base base-devel efibootmgr os-prober grub networkmanager dhcp ntfs-3g gvfs nano linux linux-firmware
```

9. Install additional packages
- WIFI drivers
```
pacstrap /mnt netctl wpa_supplicant dialog
```

- Touchpad drivers
```
pacstrap /mnt xf86-input-synaptics
```

10. Generate fstab file
```
genfstab -U /mnt >> /mnt/etc/fstab
```

11. Change root into the new system:
```
arch-chroot /mnt
```

12. Configure the system
    - Hostname: `echo "archlinux" >> /etc/hostname`
    - Time zone: `ln -s /usr/share/zoneinfo/America/Mexico_City /etc/localtime`
    - Language: `nano /etc/locale.gen`
      - Uncomment the next lines:
      - *en_US.UTF-8 UTF-8*
      - *en_US ISO-8859-1*
    - Locale: `echo LANG=en_US.UTF-8 > /etc/locale.conf`
    - Generate the locale.gen file: `locale-gen`
    - Keyboard layout: `echo KEYMAP=us > /etc/vconsole.conf`

13. Install GRUB
```
grub-install --target=x86_64-efi --efi-directory=boot/efi --bootloader-id=ArchLinux
```

14. Update GRUB
```
grub-mkconfig -o /boot/grub/grub.cfg
```

15. User, group & password
    - Root password: `passwd`
    - Group: `groupadd GROUP_NAME`
    - User: `useradd -m -g GROUP_NAME -s /bin/bash USER_NAME`
    - User password: `passwd USER_NAME`

16. Umount the file systems & reboot
```
exit
umount -R /mnt
reboot
```

17. Initial setup
    - Login as root
    - Permissions
      - `nano /etc/sudoers`
      - Add `USER_NAME ALL=(ALL) ALL`
    - Network Manager
      - `systemctl start NetworkManager.service`
      - `systemctl enable NetworkManager.service`
      - `nmtui`
    - Login as user
      - `exit`
      - Log in
    - Update system
      - `sudo pacman -Syyu`

18. Install important packages
```
sudo pacman -S git xorg
```

19. Install AUR Helper
	- Paru (in Rust)
	  - `cd /opt`
      - `git clone https://aur.archlinux.org/paru.git`
      - `cd paru`
      - `makepkg -si`
	- Yay (in Go)
	  - `cd /opt`
      - `git clone https://aur.archlinux.org/yay.git`
      - `cd yay`
      - `makepkg -si`

20. Official installation guide
    - [archlinux.org](https://wiki.archlinux.org/title/Installation_guide)
