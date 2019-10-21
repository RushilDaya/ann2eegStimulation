from psychopy import visual, core, logging
import matplotlib.pyplot as plt
from shared.setup import createWindow, createTarget, createMarker
from shared.vep import vepRoutine

IMAGE_SCALE = 0.25
UP_FRAME_PATH = './stimulationImages/tester1.jpg'
DOWN_FRAME_PATH = './stimulationImages/tester2.jpeg'
NUM_CYCLES = 2
CYCLE_LENGTH = 5 # in seconds
CYCLE_DUTY = 0.2 # normalised 




window, fps, shortSide = createWindow()
targetSize = shortSide*IMAGE_SCALE
targetUp, targetDown = createTarget(window, targetSize, UP_FRAME_PATH, DOWN_FRAME_PATH)

vepRoutine(window,targetUp,targetDown,fps, num_cycles=NUM_CYCLES, cycle_length=CYCLE_LENGTH,cycle_duty=CYCLE_DUTY)


core.wait(1)




# MONITOR_WIDTH = 1920
# MONITOR_HEIGHT = 1080
# FRAME_RATE = 60

# mainWindow = visual.Window([MONITOR_WIDTH, MONITOR_HEIGHT],units='pix',fullscr=True)
# mainSquare = visual.Rect(mainWindow, height=50,width=50,
#                          pos=(0,0))
# mainSquare.draw()
# mainWindow.flip()
# core.wait(1)

# screenProperties()



# # Setup stimulus
# win = visual.Window([400, 400])
# win.recordFrameIntervals = True
# win.refreshThreshold = 1/60 + 0.004
# gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5,
#     name='gabor', autoLog=False)
# fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size=0.02,
#     name='fixation', autoLog=False)

# # Let's draw a stimulus for 200 frames, drifting for frames 50:100
# for frameN in range(200):   # For exactly 200 frames
#     if 10 <= frameN < 150:  # Present fixation for a subset of frames
#         fixation.draw()
#     if 50 <= frameN < 100:  # Present stim for a different subset
#         gabor.phase += 0.1  # Increment by 10th of cycle
#         gabor.draw()
#     win.flip()

# logging.console.setLevel(logging.WARNING)
# print('Overall, %i frames were dropped.' % win.nDroppedFrames)


# plt.plot(win.frameIntervals)
# plt.show()