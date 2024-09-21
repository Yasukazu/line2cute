// steer is a ratio(0 to 1)
// 
// of motor powers
function steer2 (turn: number) {
    if (turn < 0) {
        cuteBot.motors(accel / steer, steer * accel)
    } else if (turn > 0) {
        cuteBot.motors(steer * accel, accel / steer)
    } else {
        cuteBot.motors(accel, accel)
    }
}
let out = 0
let tracking = 0
let steer = 0
let accel = 0
let N_TURN = 0
// accel is a percentage of power to motor
let L_TURN = -1
let R_TURN = 1
accel = 50
steer = 0.8
cuteBot.singleheadlights(cuteBot.RGBLights.ALL, 0, 0, 0)
loops.everyInterval(200, function () {
    if (cuteBot.tracking(cuteBot.TrackingState.L_R_line)) {
        tracking = 0
        out = 0
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_unline_R_line)) {
        steer2(L_TURN)
        tracking = -1
        out = 0
    } else if (cuteBot.tracking(cuteBot.TrackingState.L_line_R_unline)) {
        steer2(R_TURN)
        tracking = 1
        out = 0
    } else {
        steer2(N_TURN)
        // cuteBot.tracking(cuteBot.TrackingState.L_R_UNLINE):
        out = 1
    }
})
