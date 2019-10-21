from psychopy import visual, core, logging
import matplotlib.pyplot as plt
import numpy
import pickle

window = visual.Window(fullscr=True,
                       units='pix',
                       colorSpace='rgb255',
                       color=[0,0,0]) 
fps = round(window.getActualFrameRate())
shortSide = min(window.size)
targetSize = shortSide*0.25

imagePath = './stimulationImages/tester1.jpg'
image1 = visual.ImageStim(window,image=imagePath,size=[targetSize,targetSize])
imagePath = './stimulationImages/tester2.jpg'
image2 = visual.ImageStim(window,image=imagePath,size=[targetSize,targetSize])

scrShots = []
print(core.getTime())
for idx in range(60):
    if idx % 2 == 1:
        image1.draw()
    else:
        image2.draw()
    window.flip()
    scrShot = numpy.asarray(window.getMovieFrame())
    scrShots += [scrShot]
print(core.getTime())

file = open('temp.pickle','wb')
pickle.dump(scrShots,file)
    
    

