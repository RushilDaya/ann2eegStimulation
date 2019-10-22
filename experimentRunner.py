# runs the main experiment based on a configuration

# 1. read and parse the configuration information
import sys, json
from shared.validations import formatConfigFileName, configurationValidation


if len(sys.argv) != 2:
    raise Exception("Incorrect number of input arguments")
configFileNameRaw = sys.argv[1]

configFileName = formatConfigFileName(configFileNameRaw)

with open(configFileName) as config_file:
    configurations = json.load(config_file)

assert(configurationValidation(configurations))

# 2. generation the patterns which needs to be displayed
from shared.utils import generateFrequencyMasks
frequencyMasks = generateFrequencyMasks(configurations["frequencies"],configurations["frameRate"])

from psychopy import core,visual
from shared.psyHelpers import makeWindow, generateDisplaySequences

window = makeWindow()
displaySequences = generateDisplaySequences(window, configurations['frequencies'],
                                            configurations['angles'],frequencyMasks,
                                            configurations["frameRate"],
                                            configurations["targetSizePixels"])

# 3. display and save the patterns which will be displayed

# from shared.psyHelpers import showMessage, screenCaptureRoutine
# from shared.utils import saveObject

# showMessage(window, 'Displaying Calibration Routine' )
# screenShots = screenCaptureRoutine(window,displaySequences)
# storeObj = {
#     'screenShots':screenShots,
#     'frameRate':configurations['frameRate'],
#     'sequenceLength':configurations['sequenceLengthSeconds'],
#     'frequencies':configurations['frequencies'],
#     'angles':configurations['angles']
# }

# saveObject(storeObj,configurations['screenshotSavePath'])

# 4. run trial loops
from shared.markerHandler import markerHandler
from shared.utils import randomDuals
from shared.psyHelpers import pauseScreen, conductTrial

markerObj = markerHandler( configurations['markerFile'],
                           configurations['frequencies'],
                           configurations['angles'])

for trialNumber in range(configurations['numTrials']):
    randomOrder = randomDuals(configurations['frequencies'],configurations['angles'])
    pauseScreen(window)
    conductTrial(displaySequences,randomOrder,markerObj)

    