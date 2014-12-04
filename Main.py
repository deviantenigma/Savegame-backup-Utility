"""
import os
import shutil
import glob
"""

import tkinter
import tkinter.messagebox
import CopyCat
import string
import os


class Main:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.wm_title("Sun's Backup Utility")

        self.copierCat = CopyCat.CopyCat()

        self.createWindow()

        tkinter.mainloop()

    #######################################################
    #################### Window Creation ##################
    #######################################################

    def createWindow(self):
        self.createFrames()
        self.fillFrames()
        self.packFrames()

    def createFrames(self):
        self.fullFrame = tkinter.Frame()
        self.menuframe = tkinter.Frame(self.fullFrame)
        self.buttonframe = tkinter.Frame(self.fullFrame)
        #self.textframe = tkinter.Frame(self.fullFrame)

    def fillFrames(self):
        self.fillMenuFrame()
        self.fillButtonFrame()
        #self.fillTextFrame()


    def fillMenuFrame(self):
        # Menu Frame
        menubar = tkinter.Menu(self.main_window)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        drivemenu = tkinter.Menu(menubar, tearoff=0)
        savetomenu = tkinter.Menu(menubar, tearoff=0)

        #FileMenu
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Exit", command=self.main_window.quit)

        #DriveMenu
        self.drive = 'C'
        menubar.add_cascade(label="Drive", menu=drivemenu)
        for letter in string.ascii_uppercase:
            if os.path.exists("%s:/" % letter):
                drivemenu.add_radiobutton(label=letter, command=lambda labelletter=letter:
                                          self.changeSaveDrive(labelletter))

        #SavetoMenu
        menubar.add_cascade(label="Save To", menu=savetomenu)
        savetomenu.add_radiobutton(label='Hard Drive: Program Folder',
                                   command=self.copierCat.setSavedriveToSameDirectory)
        savetomenu.add_radiobutton(label='Hard Drive: Documents',command=lambda: self.copierCat.setSaveDrive(
                                   'Documents/SunsBackupUtilitysaves'))
        savetomenu.add_radiobutton(label='DropBox Folder', command=lambda: self.copierCat.setSaveDrive
                                  ('dropbox/apps/SunsBackupUtilitysaves'))
        savetomenu.add_radiobutton(label='Google Drive Folder', command=lambda: self.copierCat.setSaveDrive
                                  ('Google Drive/SunsBackupUtilitysaves'))

        self.main_window.config(menu=menubar)

    def fillButtonFrame(self):
        # Button Frame

        #Checklist, needs its own frame eventually
        self.starboundPlayer = tkinter.Checkbutton(self.buttonframe, text="Starbound Player Files",
                                                   command=self.copierCat.StarboundPlayerStatusToggle)

        self.starboundPlanet = tkinter.Checkbutton(self.buttonframe, text="Starbound Planet Files",
                                                   command=self.copierCat.StarboundPlanetStatusToggle)

        self.MinecraftWorlds = tkinter.Checkbutton(self.buttonframe, text="Minecraft World Files",
                                                   command=self.copierCat.VanillaMinecraftStatusToggle)

        self.RiskOfRain = tkinter.Checkbutton(self.buttonframe, text="Risk of Rain",
                                              command=self.copierCat.RiskOfRainStatusToggle)

        #Copy Button
        self.onlybutton = tkinter.Button(self.buttonframe, text='Back Up Files', command=self.copytest) #self.copytest

        # Pack Widgets

        self.starboundPlayer.pack(side='top')
        self.starboundPlanet.pack(side='top')
        self.MinecraftWorlds.pack(side='top')
        self.RiskOfRain.pack(side='top')
        self.onlybutton.pack(side='top')

    '''
    def fillTextFrame(self):
        # add a vertical scroll bar to the text area
        self.scroll = tkinter.Scrollbar(self.textframe, jump=0)

        # Text Frame
        self.textbox = tkinter.Text(self.textframe, height=10, width=40, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.textbox.yview)

        #Pack Widgets
        self.scroll.pack(side='right', fill='y')
        self.textbox.pack(side='top')'''

    def packFrames(self):
        # Pack frames
        self.menuframe.pack()
        self.buttonframe.pack(padx=20, pady=40)
        #self.textframe.pack()
        self.fullFrame.pack(padx=20, pady=20)

    #######################################################
    ################# Command Functions ###################
    #######################################################

    def copytest(self):
        self.copierCat.determineGamesToCopy()
        tkinter.messagebox.showinfo("Files Copied", 'The files have been copied')

    '''def updatetextbox(self, name):
        self.textbox.insert(tkinter.INSERT, name)
        self.textbox.insert(tkinter.INSERT, '\n')'''

    def changeSaveDrive(self,drive):
        self.copierCat.setDataDrive(drive)

window = Main()

"""
src = os.path.abspath("C:/Users/Sun/Downloads/copyfrom/")
dst = os.path.abspath("C:/Users/Sun/Downloads/copyto/")
src = os.path.join(src)
dst = os.path.join(dst)

shutil.copyfile(src, dst)
src = r'C:/Program Files (x86)/Steam/SteamApps/common/Starbound/player/'
os.path.join('C:','Program Files(x86)','Steam','SteamApps','common','Starbound','player') #
dst = './tmp/'
shutil.copy(src, dst)

for name in glob.glob('C:\Program Files (x86)\Steam\SteamApps\common\Starbound\player\*'):
shutil.copy2(name, dst)
self.updatetextbox(name)
self.textbox.insert(tkinter.INSERT, name)
"""