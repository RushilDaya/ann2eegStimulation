import math, os, pickle, numpy, random

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

def saveObject(obj, savePath):
    with open(savePath,'wb') as fileHandler:
        pickle.dump(obj,fileHandler)
    return True

def randomDuals(A,B):
    # returns a list of AxB tuples
    # contains the cross of lists A and B in a random order
    listOfTuples = []
    for a in A:
        for b in B:
            listOfTuples += [(a,b)]
    random.shuffle(listOfTuples)
    print(listOfTuples)
    return listOfTuples

