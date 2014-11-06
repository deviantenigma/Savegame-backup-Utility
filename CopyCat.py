import shutil
import os
import time


class Cat:

    def __init__(self):
        self.starboundPlayerBoolean = False
        self.starboundPlanetBoolean = False
        self.vanillaMinecraftBoolean = False

        self.booleanSwitcher = (lambda booleanInput: False if booleanInput else True)

        self.dataDrive = 'C:/'
        self.saveDrive = './'

        self.timeString = time.strftime("%Y-%b-%d_%H-%M-%S")
        self.steamPath = os.path.join(self.dataDrive,'Program Files (x86)/Steam/SteamApps/common/')
        self.userFolders = os.path.join(self.dataDrive, 'Users/', os.path.expanduser('~'))

    #######################################################
    ################# File Path Functions #################
    #######################################################

    def setDataDriveToC(self):
        self.dataDrive = 'C:/'

    def setDataDriveToD(self):
        self.dataDrive = 'D:/'

    def setSavedriveToHdd(self):
        self.saveDrive = './'

    def setSaveDriveToDropBox(self):
        self.saveDrive = os.path.join(self.userFolders,'dropbox/apps')

    def setSaveDriveToGoogleDrive(self):
        self.saveDrive = os.path.join(self.userFolders,'Google Drive')

    def updateFilePaths(self):
        self.timeString = time.strftime("%Y-%b-%d_%H-%M-%S")
        self.steamPath = os.path.join(self.dataDrive, 'Program Files (x86)/Steam/SteamApps/common/')
        self.userFolders = os.path.join(self.dataDrive, 'Users/', os.path.expanduser('~'))

    #######################################################
    ################# Copy Boolean Functions ##############
    #######################################################

    def StarboundPlayerStatus(self):
        self.starboundPlayerBoolean = self.booleanSwitcher(self.starboundPlayerBoolean)

    def StarboundPlanetStatus(self):
        self.starboundPlanetBoolean = self.booleanSwitcher(self.starboundPlanetBoolean)

    def VanillaMinecraftStatus(self):
        self.vanillaMinecraftBoolean = self.booleanSwitcher(self.vanillaMinecraftBoolean)

    #######################################################
    ############ Obligatory long if function ##############
    #######################################################

    def determineGamesToCopy(self):

        self.updateFilePaths()

        steamSrcMaker = (lambda gameSpecifics: os.path.join(self.steamPath,gameSpecifics))
        MultiSaveFolderDstMaker = (lambda gameName, saveType:os.path.join(self.saveDrive, gameName,
                                                                          saveType, self.timeString, saveType))

        if self.starboundPlayerBoolean:
            #src = os.path.join(self.steamPath,'Starbound/player/')
            #dst = os.path.join(self.saveDrive, 'starbound/player', self.timeString, 'player')
            shutil.copytree(steamSrcMaker('Starbound/player/'), MultiSaveFolderDstMaker('starbound','player'))

        if self.starboundPlanetBoolean:
            #src = os.path.join(self.steamPath,'Starbound/universe/')
            #dst = os.path.join(self.saveDrive, 'starbound/universe', self.timeString,'universe')
            shutil.copytree(steamSrcMaker('Starbound/universe/'), MultiSaveFolderDstMaker('starbound','universe'))

        if self.vanillaMinecraftBoolean:
            src = os.path.join(self.userFolders,'AppData/Roaming/.minecraft/saves')
            dst = os.path.join(self.saveDrive,'minecraft',self.timeString)
            shutil.copytree(src, dst)

copierCat = Cat()