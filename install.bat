@echo off
winget install virtualbox
IF EXIST "%ProgramFiles%\Oracle\VirtualBox\VirtualBox.exe" echo [+] Success
set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"
#set /p "path_vm=Enter path for your virtual machine: "


VBoxManage createvm --name "Ubuntu" --ostype "Ubuntu_64" --register
VBoxManage createhd --filename D:\Ubuntu.vdi --size 10000
VBoxManage storagectl "Ubuntu" --name "IDE Controller" --add ide --controller PIIX4
VBoxManage storageattach "Ubuntu" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium D:\Ubuntu.vdi
VBoxManage storagectl "Ubuntu" --name "IDE Controller" --add ide
VBoxManage storageattach "Ubuntu" --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium D:\ubuntu-22.10-desktop-amd64.iso
VBoxManage modifyvm "Ubuntu" --ioapic on
VBoxManage modifyvm "Ubuntu" --memory 2048 --vram 256 --cpus 2
VBoxManage unattended install "Ubuntu" --iso=D:\ubuntu-22.10-desktop-amd64.iso --user=login --full-user-name=name --password password --install-additions --time-zone=CET --install-additions --post-install-command="firefox ya.ru"
VBoxManage startvm "Ubuntu"
pause