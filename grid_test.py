def generate_grid_gcode(start_x, start_y, end_x, end_y, spacing, pen_up_speed="M3S90", pen_down_speed="M3S140"):
    """
    Generates G-code for a grid of dots.

    Args:
        start_x (float): Starting X position.
        start_y (float): Starting Y position.
        end_x (float): Ending X position.
        end_y (float): Ending Y position.
        spacing (float): Spacing between dots.
        pen_up_speed (str): G-code command to lift the pen.
        pen_down_speed (str): G-code command to drop the pen.

    Returns:
        str: Generated G-code.
    """
    gcode = []
    gcode.append("G90")  # Absolute positioning
    gcode.append("G21")  # Millimeters
    
    # Calculate the number of dots
    num_x = int(abs(end_x - start_x) / spacing) + 1
    num_y = int(abs(end_y - start_y) / spacing) + 1

    # Generate the grid
    for i in range(num_y):
        y_pos = start_y + i * spacing
        for j in range(num_x):
            x_pos = start_x - j * spacing  # Adjusting for X direction moving left
            gcode.append(f"G0X{x_pos:.3f}Y{y_pos:.3f}")  # Move to position
            gcode.append(pen_down_speed)  # Drop pen
            gcode.append(pen_up_speed)    # Lift pen

    # gcode.append("M30")  # Program end
    return "\n".join(gcode)

# Parameters for the grid
start_x = 190
start_y = 0
end_x = 90
end_y = 100
spacing = 10

# Generate the G-code
gcode = generate_grid_gcode(start_x, start_y, end_x, end_y, spacing)

# Save to a file
output_file = "grid_of_dots.gcode"
with open(output_file, "w") as file:
    file.write(gcode)

print(f"G-code for grid of dots saved to {output_file}")
