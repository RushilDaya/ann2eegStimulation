from psychopy import visual, core

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
            
                

            

