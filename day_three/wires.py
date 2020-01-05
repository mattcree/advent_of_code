up = 'U'
down = 'D'
left = 'L'
right = 'R'

def find_smallest_manhatten_distance(file_path):
    [wire_a, wire_b] = read_wires_input(file_path)
    wire_crossing_points = find_wire_crossing_points(wire_a, wire_b)
    manhatten_distances = set([abs(x) + abs(y) for x, y in wire_crossing_points])
    if 0 in manhatten_distances:
        manhatten_distances.remove(0)
    return min(manhatten_distances)

def find_wire_crossing_points(wire_a, wire_b):
    wire_a_occupied_vectors = generate_occupied_vectors(wire_a)
    wire_b_occupied_vectors = generate_occupied_vectors(wire_b)
    return wire_a_occupied_vectors.intersection(wire_b_occupied_vectors)

def generate_occupied_vectors(directions_line):
    last_x = 0
    last_y = 0
    occupied_vectors = set()
    for direction, distance in directions_line:
        if direction == up:
            occupied_vectors.update(up_occupied_vectors(last_x, last_y, distance))
            last_y += distance
        elif direction == right:
            occupied_vectors.update(right_occupied_vectors(last_x, last_y, distance))
            last_x += distance
        elif direction == down:
            occupied_vectors.update(down_occupied_vectors(last_x, last_y, distance))
            last_y -= distance
        elif direction == left:
            occupied_vectors.update(left_occupied_vectors(last_x, last_y, distance))
            last_x -= distance
    return occupied_vectors

def up_occupied_vectors(x, y, distance):
    vectors = set()
    for next_y in range(y, y + distance):
        vectors.add((x, next_y))
    return vectors

def right_occupied_vectors(x, y, distance):
    vectors = set()
    for next_x in range(x, x + distance):
        vectors.add((next_x, y))
    return vectors

def down_occupied_vectors(x, y, distance):
    vectors = set()
    next_y = y
    for _ in range(distance + 1):
        vectors.add((x, next_y))
        next_y -= 1
    return vectors

def left_occupied_vectors(x, y, distance):
    vectors = set()
    next_x = x
    for _ in range(distance + 1):
        vectors.add((next_x, y))
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

print(find_smallest_manhatten_distance('input.txt'))