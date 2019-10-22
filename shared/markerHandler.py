import json 

class markerHandler:
    def __init__(self,pathToMarkerFile, frequencies, angles):
        # how we deal with markers really depends on 
        # the setup we have available to us. 
        # as a temp measure we simply console log the markers
        with open(pathToMarkerFile,'rb') as file:
            tempStructure = json.load(file)
        self.trialStartMarker  = tempStructure["trialStart"]
        self.trialStopMarker   = tempStructure["trialStop"]
        self.sequenceEndMarker = tempStructure["endSeq"]

        sequenceStartMarkers = {}
        for frequency in frequencies:
            sequenceStartMarkers[frequency]={}
            for angle in angles:
                sequenceStartMarkers[frequency][angle]=tempStructure['startSeqs'][str(frequency)][str(angle)]
        self.sequenceStartMarkers = sequenceStartMarkers
    
    def _transmit_marker(self,marker):
        # this is probably the only function we need to modify once we know how markers work
        print(marker)
        return True

    def display_trialStart(self):
        self._transmit_marker(self.trialStartMarker)
        return True
    
    def display_trialEnd(self):
        self._transmit_marker(self.trialStopMarker)
        return True
    
    def display_seqEnd(self):
        self._transmit_marker(self.sequenceEndMarker)
        return True
    
    def display_seqStart(self,frequency,angle):
        self._transmit_marker(self.sequenceStartMarkers[frequency][angle])
        return True

