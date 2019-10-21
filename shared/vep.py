from psychopy import core
# primary item here is the vep routine
# the vep routine distinction

def vepRoutine(window,targetUp,targetDown,fps, num_cycles=1, cycle_length=5,cycle_duty=0.2):
    # the vep routine cycles between the high and low targets
    # can approach the 
    
    targetDown.draw()
    window.flip()
    core.wait(2)
    
    for cycleIdx in range(num_cycles):
        



