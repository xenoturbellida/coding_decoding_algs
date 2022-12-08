def find_orig_sequence(transformed_seq: [str], orig_position: int) -> [str]:
    buffer = [[letter] for letter in transformed_seq]

    while len(buffer[0]) != len(transformed_seq):
        buffer.sort()
        for i in range(len(buffer)):
            buffer[i].insert(0, transformed_seq[i])

    buffer.sort()
    return buffer[orig_position]
