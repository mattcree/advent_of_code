def find_steps_to_closest_intersection(file_path):
    [wire_a, wire_b] = read_wires_input(file_path)

    wire_a_vectors = generate_vectors(wire_a)
    wire_b_vectors = generate_vectors(wire_b)

    crossing_points = set(wire_a_vectors).intersection(set(wire_b_vectors))

    return min([get_steps(wire_a_vectors, wire_b_vectors, crossing_point) for crossing_point in crossing_points if crossing_point != (0, 0)])


def get_steps(wire_a_vectors, wire_b_vectors, crossing_point):
    wire_a_distance = wire_a_vectors.index(crossing_point)
    wire_b_distance = wire_b_vectors.index(crossing_point)
    return wire_a_distance + wire_b_distance


def generate_vectors(directions_line):
    current_x = 0
    current_y = 0
    occupied_vectors = [(current_x, current_y)]
    for direction, distance in directions_line:
        if direction == 'U':
            occupied_vectors.extend(up_occupied_vectors(current_x, current_y, distance))
            current_y += distance
        elif direction == 'R':
            occupied_vectors.extend(right_occupied_vectors(current_x, current_y, distance))
            current_x += distance
        elif direction == 'D':
            occupied_vectors.extend(down_occupied_vectors(current_x, current_y, distance))
            current_y -= distance
        elif direction == 'L':
            occupied_vectors.extend(left_occupied_vectors(current_x, current_y, distance))
            current_x -= distance
    return occupied_vectors


def up_occupied_vectors(x, y, distance):
    vectors = list()
    next_y = y + 1
    for _ in range(distance):
        vectors.append((x, next_y))
        next_y += 1
    return vectors


def right_occupied_vectors(x, y, distance):
    vectors = list()
    next_x = x + 1
    for _ in range(distance):
        vectors.append((next_x, y))
        next_x += 1
    return vectors


def down_occupied_vectors(x, y, distance):
    vectors = list()
    next_y = y - 1
    for _ in range(distance):
        vectors.append((x, next_y))
        next_y -= 1
    return vectors


def left_occupied_vectors(x, y, distance):
    vectors = list()
    next_x = x - 1
    for _ in range(distance):
        vectors.append((next_x, y))
        next_x -= 1
    return vectors


def read_wires_input(file_path):
    with open(file_path, 'r') as file:
        return [generate_directions(parse_directions_line(line)) for line in file]


def parse_directions_line(line):
    return line.replace('\n', '').split(',')


def generate_directions(directions_line):
    return [generate_direction(direction) for direction in directions_line]


def generate_direction(direction):
    return (direction[0], int(direction[1:]))


print(find_steps_to_closest_intersection('input.txt'))