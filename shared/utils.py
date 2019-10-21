import math

def generateFrequencyMasks(frequencyList, frameRate):
    # returns a dictionary with keys given by frequencies
    # the returned arrays are for exactly 1 second of stimulation at each frequency
    
    masks = {}
    for frequency in frequencyList:
        mask = []
        for frameIdx in range(frameRate):
            mask += [ 0.5*math.cos(2*math.pi*frequency*frameIdx/frameRate ) + 0.5]
        masks[frequency] = mask
    return masks

