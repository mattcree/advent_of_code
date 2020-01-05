def program_alarm(file_path):
    int_code_program = int_code_program_from_file(file_path)
    return process_int_code_program(int_code_program)

def brute_force_guess_noun_and_verb_for_given_target(file_path, target_number):
    int_code_program = int_code_program_from_file(file_path)
    origin_position = 0
    noun_position = 1
    verb_position = 2
    for noun_value in range(0, 99):
        for verb_value in range(0, 99):
            int_code_program_copy = int_code_program.copy()
            int_code_program_copy[noun_position] = noun_value
            int_code_program_copy[verb_position] = verb_value

            processed_program = process_int_code_program(int_code_program_copy)

            if (processed_program[origin_position] == target_number):
                return (noun_value, verb_value)

    return (-1, -1)

def process_int_code_program(int_code_program):
    position = 0
    while position <= len(int_code_program):
        if int_code_program[position] == 99:
            break
        if int_code_program[position] == 1:
            do_addition(int_code_program, position)
        if int_code_program[position] == 2:
            do_multiplication(int_code_program, position)
        position += 4
    return int_code_program


def do_addition(int_code_program, chunk_position):
    left, right, save = positions(int_code_program, chunk_position)
    int_code_program[save] = int_code_program[left] + int_code_program[right]


def do_multiplication(int_code_program, chunk_position):
    left, right, save = positions(int_code_program, chunk_position)
    int_code_program[save] = int_code_program[left] * int_code_program[right]


def positions(int_code_program, chunk_position):
    return (int_code_program[chunk_position + 1], int_code_program[chunk_position + 2], int_code_program[chunk_position + 3])


def int_code_program_from_file(file_path):
    int_codes = []
    with open(file_path, 'r') as file:
        for line in file:
            int_codes.extend(process_code_file_line(line))
    return int_codes


def process_code_file_line(code_file_line):
    return [int(code_string) for code_string in code_file_line.replace('\n', '').split(',')]


print(brute_force_guess_noun_and_verb_for_given_target('input.txt', 19690720))