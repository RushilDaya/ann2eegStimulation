from psychopy import visual, core
import numpy as np

def makeWindow():
    window = visual.Window(fullscr=True,
                           units='pix',
                           colorSpace='rgb255',
                           color=[0,0,0])
    return window

def generateDisplaySequences(window, frequencies, gratingAngles, frequencyMasks, frameRate, targetSize):
    # generate a unique image for each frequency/gratingAngle/frame combination
    # a multilevel dictionary is used to store the resulting images
    # note only producing 1 second of images

    allSequences = {}
    for frequency in frequencies:
        frequencySequences = {}
        for gratingAngle in gratingAngles:
            gratingList = []
            for frameIdx in range(frameRate):
                newGrating = visual.GratingStim(window,
                                                mask='circle',
                                                size=targetSize,
                                                texRes=200, 
                                                sf=0.05,
                                                ori=gratingAngle, 
                                                opacity= frequencyMasks[frequency][frameIdx] )
                gratingList += [newGrating]
            frequencySequences[gratingAngle]=gratingList
        allSequences[frequency]=frequencySequences

    return allSequences    
            
def showMessage(window, message, duration_frames=12):
    message = visual.TextStim(window,message)
    for i in range(duration_frames):
        message.draw()
        window.flip()
    return True

def screenCaptureRoutine(window, sequencesDict):
    # take multilevel dictionary and draws the images to the screen
    # this way is  flexible for future changes
    # the capturing is slow hence why it is not done in real time

    outerKeys = list(sequencesDict.keys())
    innerKeys = list(sequencesDict[outerKeys[0]].keys())
    
    screenShots = {}
    for outerKey in outerKeys:
        screenShots[outerKey]={}
        for innerKey in innerKeys:
            screenShots[outerKey][innerKey]=[]
            sequenceOfInterest = sequencesDict[outerKey][innerKey]
            for idx in range(len(sequenceOfInterest)):
                tempStimulus = sequenceOfInterest[idx]
                tempStimulus.draw()
                window.flip()
                screenShot = np.asarray(window.getMovieFrame())
                screenShots[outerKey][innerKey]+=[screenShot]

    return screenShots
            
