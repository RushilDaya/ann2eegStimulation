# code for stimulation
## requires
* Python 3.7 
* Install Anaconda
* Download pyschopy using Anaconda install at https://www.psychopy.org/download.html
* Run python experimentRunner.py `CONFIGURATION_NAME`

## Background
This experiment runs a stimulus for an SSVEP based data collection. Allows for the generation of data at different frequencies as well as for different angles of a grating spatial pattern.
The experiment also writes 1 second of data for each frequency phase combination to file which can be used later as input in an analysis.
The records being only 1 second require replication (post) if they are to be used in a subsequent analysis.

## configuration files
For a new experiment define it as a .json file in the configurations folder.
* frameRate: the framerate of the monitor on which the stimulus will be displayed
* frequencies: a list of the frequencies which will be tested. Frequencies must be whole numbers.
* angles: a list of angles, the spatial angle of the stimulation pattern between 0 and 90.
* targetSizePixels: size of the stimulus block
* sequenceLengthSeconds: must be a WHOLE number 
* screenshotSavePath: 
* markerFile:
* numTrials: One trial goes through the each combination of frequency and angle

NOTE: every frequency angle pair defined in the configuration needs to have a corresponding marker defined in the `markerList.json` file.



## TODO
Currently the `markerHandler` object is a stub and just prints the marker to console. 
To use marker based synchronisation theses markers need to transmitted to the computer recording the EEG signal
so that the recorded EEG signal can be properly segmented.

