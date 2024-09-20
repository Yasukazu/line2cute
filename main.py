"""

accel is a percentage of power to motor

"""
"""

steer is a ratio(0 to 1)

of motor powers

"""
def steer2(left: bool):
    if left:
        cuteBot.motors(accel, steer * accel)
        basic.pause(100)
    else:
        cuteBot.motors(steer * accel, accel)
        basic.pause(100)
tracking = 0
out = 0
steer = 0
accel = 0
cuteBot.singleheadlights(cuteBot.RGBLights.RGB_R, 255, 0, 0)
accel = 50
steer = 0.8

def on_forever():
    if out == 0:
        if tracking < 0:
            cuteBot.motors(50, 30)
        else:
            if tracking > 0:
                cuteBot.motors(30, 50)
            else:
                cuteBot.motors(50, 50)
    else:
        if tracking > 0:
            cuteBot.motors(50, 30)
        else:
            if tracking < 0:
                cuteBot.motors(30, 50)
            else:
                cuteBot.motors(50, 50)
basic.forever(on_forever)

def on_every_interval():
    global tracking, out
    if cuteBot.tracking(cuteBot.TrackingState.L_R_LINE):
        tracking = 0
        out = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_UNLINE_R_LINE):
        steer2(True)
        tracking = -1
        out = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        tracking = 1
        out = 0
    else: # cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        out = 1
loops.every_interval(200, on_every_interval)
