def find_orig_sequence(transformed_seq: [str], orig_position: int) -> [str]:
    buffer = [[letter] for letter in transformed_seq]

    while len(buffer[0]) != len(transformed_seq):
        buffer.sort()
        for i in range(len(buffer)):
            buffer[i].insert(0, transformed_seq[i])

    buffer.sort()
    return buffer[orig_position]


def check_if_pos_is_valid(sequence: str, position: str) -> bool:
    pos_is_valid = True
    try:
        ind = int(position)
        if ind >= len(sequence) or ind < 0:
            pos_is_valid = False
    except ValueError:
        pos_is_valid = False
    return pos_is_valid


def get_args_from_user():
    user_input = input().split(" ")
    return user_input[0], user_input[1]


if __name__ == '__main__':
    print('Enter transformed sequence, then position in BWT (zero based):')
    seq, pos = get_args_from_user()

    while not check_if_pos_is_valid(seq, pos):
        print("Position is not valid. Try again")
        seq, pos = get_args_from_user()

    print(''.join(find_orig_sequence(seq, int(pos))))

    # TEST:
    # print(''.join(find_orig_sequence('MLRATGOI', 0)))
    # print(''.join(find_orig_sequence('NNBAAA', 3)))
