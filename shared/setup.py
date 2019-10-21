from psychopy import visual

def createWindow():
    window = visual.Window(fullscr=True,
                           units='pix',
                           colorSpace='rgb255',
                           color=[0,0,0])
    fps = round(window.getActualFrameRate())
    shortSide = min(window.size) # used to size targets

    return window, fps, shortSide


def createTarget(window, sizeInPixels, upFramePath, downFramePath):

    sizeInPixels = int(sizeInPixels)
    targetUp = visual.ImageStim(window,image=upFramePath,size=[sizeInPixels,sizeInPixels])
    targetDown = visual.ImageStim(window,image=downFramePath,size=[sizeInPixels,sizeInPixels])

    return targetUp, targetDown

def createMarker():
    return True