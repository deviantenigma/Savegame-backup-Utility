import shutil
import os
import time


class CopyCat:

    def __init__(self):
        self.starboundPlayerBoolean = False
        self.starboundPlanetBoolean = False
        self.vanillaMinecraftBoolean = False
        self.riskofRainBoolean = False

        self.booleanSwitcher = (lambda booleanInput: False if booleanInput else True)

        self.dataDrive = 'C:/'
        self.saveDrive = './'

        self.timeString = time.strftime("%Y-%b-%d_%H-%M-%S")
        self.steamPath = os.path.join(self.dataDrive,'Program Files (x86)/Steam/SteamApps/common/')
        self.userFolders = os.path.join(self.dataDrive, 'Users/', os.path.expanduser('~'))

    #######################################################
    ################# File Path Functions #################
    #######################################################

    def setDataDrive(self,drive):
        self.dataDrive = drive + r':/'
        print(self.dataDrive)

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

    def StarboundPlayerStatusToggle(self):
        self.starboundPlayerBoolean = self.booleanSwitcher(self.starboundPlayerBoolean)

    def StarboundPlanetStatusToggle(self):
        self.starboundPlanetBoolean = self.booleanSwitcher(self.starboundPlanetBoolean)

    def VanillaMinecraftStatusToggle(self):
        self.vanillaMinecraftBoolean = self.booleanSwitcher(self.vanillaMinecraftBoolean)

    def RiskOfRainStatusToggle(self):
        self.riskofRainBoolean = self.booleanSwitcher(self.riskofRainBoolean)

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
            src = os.path.join(self.userFolders, 'AppData/Roaming/.minecraft/saves')
            dst = os.path.join(self.saveDrive, 'minecraft', self.timeString)
            shutil.copytree(src, dst)

        if self.riskofRainBoolean:
            #still needs work
            src = os.path.join(steamSrcMaker('Risk of Rain/'), 'Save.ini')
            dst = os.path.join('riskofrain/', self.timeString)
            os.makedirs(dst)
            shutil.copy2(src, dst)



copierCat = CopyCat()