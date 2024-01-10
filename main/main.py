import hyperpack
import time


# ======================================================================= FUNCTIONS
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract number of items and container dimensions
    num_items = int(lines[0].strip())
    container_dimensions = list(map(int, lines[1].split()))

    # Extract item dimensions
    item_dimensions = [list(map(int, line.split())) for line in lines[2:]]

    return num_items, container_dimensions, item_dimensions


def convert_to_format(num_items, container_dimensions, item_dimensions):
    # Create containers dictionary
    containers = {
        f"container-{i}-id": {"W": container_dimensions[0], "L": container_dimensions[1]}
        for i in range(1)
    }

    # Create items dictionary
    items = {
        f"item_{i}_id": {"w": dim[0], "l": dim[1]}
        for i, dim in enumerate(item_dimensions)
    }

    return containers, items


def write_solution_to_file(solution, output_file):
    with open(output_file, 'w') as file:
        for container_id, items in solution.items():
            file.write(f"{container_id}\n")
            for item_id, coordinates in items.items():
                file.write(f"{item_id},")
                file.write(",".join(map(str, coordinates)))
                file.write("\n")


def convert_solution_to_gcode(solution, gcode_file, scale_factor):
    gcode = ""

    # Add G-code setup commands
    gcode += "M03 S255 ; laser at MAX speed\n"
    gcode += "G90 ; Set to absolute positioning\n"
    gcode += "G21 ; Set units to millimeters\n"
    gcode += f"G1 F10000 ; Set feed rate\n"

    for container_id, items in solution.items():
        for item_id, coordinates in items.items():
            x, y, width, length = coordinates

            # Scale up the coordinates
            x_scaled = x * scale_factor
            y_scaled = y * scale_factor
            width_scaled = width * scale_factor
            length_scaled = length * scale_factor

            # Move to the starting point of the rectangle
            gcode += f"G1 X{x_scaled} Y{y_scaled} ; Move to starting point\n"

            # Dwell for 0.2 seconds
            gcode += "G4 P0.21 ; Dwell for 0.2 seconds\n"

            # Turn on the spindle with a speed of 90
            gcode += "M03 S90 ; laser at MIN speed\n"

            # Dwell for 0.2 seconds
            gcode += "G4 P0.21 ; Dwell for 0.21 seconds\n"

            # Draw the rectangle
            gcode += f"G1 X{x_scaled + width_scaled} Y{y_scaled} ; Draw top side\n"
            gcode += f"G1 X{x_scaled + width_scaled} Y{y_scaled + length_scaled} ; Draw right side\n"
            gcode += f"G1 X{x_scaled} Y{y_scaled + length_scaled} ; Draw bottom side\n"
            gcode += f"G1 X{x_scaled} Y{y_scaled} ; Draw left side\n"

            # Dwell for 0.2 seconds
            gcode += "G4 P0.21 ; Dwell for 0.21 seconds\n"

            # Turn off the spindle
            gcode += "M03 S255 ; laser at MAX speed\n"

            # Dwell for 0.2 seconds
            gcode += "G4 P0.21 ; Dwell for 0.21 seconds\n"

    # Return to the origin
    gcode += "G4 P0.21 ; Dwell for 0.21 seconds\n"
    gcode += "G1 X0 Y0 ; Return to origin\n"

    # Save G-code to a file
    with open(gcode_file, 'w') as file:
        file.write(gcode)




# ============================================================================= MAIN
def main():
    # Input and Output selection
    file_path = "data\\C1_1"
    delimiter = "_"
    output_file = delimiter.join([file_path, "result.csv"])

    # Read and pre-process input file
    num_items, container_dimensions, item_dimensions = read_input_file(file_path)
    my_containers, my_items = convert_to_format(num_items, container_dimensions, item_dimensions)

    # Problem definition
    problem = hyperpack.HyperPack(
        containers=my_containers,
        items=my_items,
    )

    # Show results
    print("Problem is being solved...")

    start_time = time.time()
    # problem.local_search()
    problem.hypersearch()
    end_time = time.time()
    elapsed_time = str(end_time - start_time)

    print("\n========== Problem solved ==========")
    print("\n========== Performance ==========", "\nExecution time: " + elapsed_time + " seconds\n", problem.log_solution())
    problem.create_figure(show=True)

    # Write solution to the output file in a .csv style
    write_solution_to_file(problem.solution, output_file)

    # Convert solution to G-code and write to file
    gcode_output_file = delimiter.join([file_path, "result.gcode"])
    convert_solution_to_gcode(solution=problem.solution, gcode_file=gcode_output_file, scale_factor=6)



if __name__ == "__main__":
    main()
