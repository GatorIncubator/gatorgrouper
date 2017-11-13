import os
import logging

os.system('touch $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"[Desktop Entry]\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"Name=GatorGrouper\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"Exec=gnome-terminal -e \"python3\\\ $HOME/gatorgrouper/gatorgrouperGUI.py\"\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"Terminal=true\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"Type=Application\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('echo  \"Icon=gg_icon.png\" >> $HOME/Desktop/gatorgrouper.desktop')
os.system('chmod +x $HOME/Desktop/gatorgrouper.desktop')
