ball_diam=40
ballr = ball_diam/2
s= f"""
M3S110
G0X190
M3S140
G91 G2X-{ball_diam}R{ballr}F2000
G2X{ball_diam}R{ballr}
M3S110
G0Y{ball_diam}
M3S140
G2X-{ball_diam}R{ballr}F2000
G2X{ball_diam}R{ballr}
M3S110
G0X-{ball_diam}Y-{ball_diam}
M3S140
G0X-{ball_diam*3}
G2Y{ball_diam}R{ballr}
G0X{ball_diam*3}
M3S110
G0Y-{ballr}X-{ballr+3*ball_diam}
M3S140
G0X-10
M3S110
G0X-10
M3S140
G0X-10
M3S110
G0X-10
M3S140
G0X-10
"""
output_file = "big_penis.gcode"
with open(output_file, "w") as file:
    file.write(s)