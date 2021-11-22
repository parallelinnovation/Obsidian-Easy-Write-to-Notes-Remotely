#-------------Obsidian: Easy Write To Notes Remotely------------#
# Author: Adrian Papineau
# Date created: November 12th, 2021

from datetime import date
import time
import glob, os

ObsidianVaultFolder = ""    # Example :"C:/Users/User/Documents/ObsidianVault/VaultName"
DailyNotesFolder = ""       # Example :"C:/Users/User/Documents/ObsidianVault/VaultName/DailyNotes"
today = date.today()
DateFormat = 1 

'''
DateFormat 1 = MMMM Do, YYYY (November 22,2021)
DateFormat 2 = YYYY-MM-DD (2021-11-22)
'''

#return current daily note file path
def RoamFormatDate(): 
    dateExtractMonth = today.strftime('%B')
    dateExtractDay = today.strftime('%d')
    dateExtractYear = today.strftime('%Y')
    # Get rid of the beginning 0 in day of the month. 
    if dateExtractDay[0] == "0":
        dateExtractDay = dateExtractDay[-1]
    # Add the "th" or similar
    if ((int(dateExtractDay) >= 10) and (int(dateExtractDay) <20)) or (dateExtractDay[-1] == "0") or ((int(dateExtractDay[-1]) >=4) and (int(dateExtractDay[-1]) <10)):       
        dateExtractNUM = str(dateExtractDay + "th")
    elif dateExtractDay[-1] == "1":       
        dateExtractNUM = str(dateExtractDay + "st")
    elif dateExtractDay[-1] == "2":       
        dateExtractNUM = str(dateExtractDay + "nd")
    elif dateExtractDay[-1] == "3":       
        dateExtractNUM = str(dateExtractDay + "rd")
    RoamFormat = str(dateExtractMonth + " " + dateExtractNUM + ", " + dateExtractYear)
    return RoamFormat
#print("Roam format date is: " + RoamFormatDate())
def SecondFormatDate():
    dateFormat = str(date.today())
    return dateFormat
#print("Second format date is: " + SecondFormatDate())

def CurrentDate():
    if DateFormat == 1:
        return RoamFormatDate()
    if DateFormat == 2:
        return SecondFormatDate()
    else:
        print("Invalid number selection for DateFormat")

def CurrentDailyNote():
    DailyNoteName = (CurrentDate() + ".md")
    DailyNotePath = DailyNotesFolder + "/" + DailyNoteName
    return DailyNotePath
print("Currently monitoring the daily note: " + "\n" + CurrentDailyNote())

# search the daily note
def FindLinkContent():
    try:
        searchfile = open(CurrentDailyNote(), "r", encoding="utf8")
        EntireFile = searchfile.read() 
        searchfile.close() 
        if ">[[" in EntireFile:
            indexStart = (EntireFile.index(">[["))
            #print(indexStart)
            everythingAfter = EntireFile[indexStart:]
            #print(everythingAfter)
            if "]]" in everythingAfter:
                RelIndexClosing = everythingAfter.index("]]")
                indexClosing = indexStart +RelIndexClosing
                LinkContent = EntireFile[(indexStart+3):indexClosing]   
                if "[[" in LinkContent:
                    print("There is another wikilink after your open [[")
                else:
                    return(LinkContent)
            
    except ValueError:
        print('ERROR FindLinkContent()')

def RemoveAlias():
    RawLinkName = str(FindLinkContent())
    if "|" in RawLinkName:
        BaseName = RawLinkName.split('|')[0]
        return(BaseName)
    else:
        return(RawLinkName)

def RemoveSymbol():
    try:
        searchfile = open(CurrentDailyNote(), "r", encoding="utf8")
        EntireFile = searchfile.read()
        searchfile.close()
        if ">[[" in EntireFile:
            searchfile = open(CurrentDailyNote(), encoding="utf8")
            SearchContent = searchfile.read()
            searchfile.seek(0)
            searchfile = open(CurrentDailyNote(), "w", encoding="utf8")   
            FixedFile = EntireFile.replace(">[[","[[")
            print("Sucessfully removed '>' symbol")
            searchfile.write(FixedFile)
            searchfile.seek(0)
            searchfile.close()
    except ValueError:
        print('ERROR RemoveSymbol()')

# Return the path of the note that is linked
def NotePath():
    LinkName = (RemoveAlias() + ".md")
    LinkNotePath = ObsidianVaultFolder + "/" + LinkName
    return(LinkNotePath)
 
def Block():
    searchfile = open(CurrentDailyNote(), "r", encoding="utf8")
    EntireFile = searchfile.read()
    indexStart = (EntireFile.index(">[["))
    everythingBefore = EntireFile[:indexStart]
    RelIndexBullet = everythingBefore[::-1].index("\n")
    #RelIndexBullet = everythingBefore[::-1].index("- ")
    indexBullet = indexStart - RelIndexBullet
    BlockContent = EntireFile[(indexBullet+1):indexStart]
    return(BlockContent)
    searchfile.close()
  
# Paste the block from daily notes into the linked note
def AppendToNote(desiredBlock):
    Notefile = open(NotePath(), encoding="utf8")
    NoteContent = Notefile.read()
    Notefile.seek(0)
    Notefile = open(NotePath(), "w", encoding="utf8")
    Notefile.write(NoteContent + "\n" + "-" + desiredBlock + "[[" + CurrentDate() + "]]")
    print("Sucessfully wrote to desired note")
    Notefile.seek(0)
    Notefile.close()

def StartMonitoring():
    while True:
        if FindLinkContent() != None:
            os.chdir(ObsidianVaultFolder)
            for file in glob.glob(RemoveAlias() + ".md"):
                print("Link found is: " + FindLinkContent())
                time.sleep(1)
                AppendToNote(Block())
                RemoveSymbol()
        time.sleep(1)

if __name__ == "__main__":
    StartMonitoring()

