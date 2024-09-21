"""

accel is a percentage of power to motor

"""
L_TURN = -1
R_TURN = 1
N_TURN = 0
accel = 50
steer = 0.8

# steer is a ratio(0 to 1)
# 
# of motor powers
def steer2(turn: int):
    if turn < 0:
        cuteBot.motors(accel / steer, steer * accel)
    elif turn > 0:
        cuteBot.motors(steer * accel, accel / steer)
    else:
        cuteBot.motors(accel, accel)
tracking = 0
out = 0
cuteBot.singleheadlights(cuteBot.RGBLights.RGB_R, 255, 0, 0)

def on_forever():
    if out == 0:
        if tracking < 0:
            cuteBot.motors(50, 30)
        elif tracking > 0:
            cuteBot.motors(30, 50)
        else:
            cuteBot.motors(50, 50)
    elif tracking > 0:
        cuteBot.motors(50, 30)
    elif tracking < 0:
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
        steer2(L_TURN)
        tracking = -1
        out = 0
    elif cuteBot.tracking(cuteBot.TrackingState.L_LINE_R_UNLINE):
        steer2(R_TURN)
        tracking = 1
        out = 0
    else:
        # cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        out = 1
loops.every_interval(200, on_every_interval)
