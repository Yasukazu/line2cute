function rblink (真偽値: boolean) {
	
}
let tracking = 0
let out = 0
cuteBot.singleheadlights(cuteBot.RGBLights.RGB_R, 255, 0, 0)
basic.forever(function () {
    if (out == 0) {
        if (tracking < 0) {
            cuteBot.motors(50, 30)
        } else {
            if (tracking > 0) {
                cuteBot.motors(30, 50)
            } else {
                cuteBot.motors(50, 50)
            }
        }
    } else {
        if (tracking > 0) {
            cuteBot.motors(50, 30)
        } else {
            if (tracking < 0) {
                cuteBot.motors(30, 50)
            } else {
                cuteBot.motors(50, 50)
            }
        }
    }
})
loops.everyInterval(200, function () {
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        tracking = 0
        out = 0
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        tracking = -1
        out = 0
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        tracking = 1
        out = 0
    }
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_unline)) {
        out = 1
    }
})
