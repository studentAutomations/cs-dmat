import os


photo_path = 'https://github.com/studentAutomations/cs-dmat/blob/main/cs-mat-nova-obavestenja.png'  


if os.path.exists(photo_path):
    os.remove(photo_path)  
