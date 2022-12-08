from bwt_decoding import find_orig_sequence


FILENAME_INPUT = 'move_to_front.conf'
LETTERS = 'letters'
CODE_WORDS = 'code_words'
FROM_BINARY_MODE = 1
FROM_ORDERS_MODE = 2


def make_letter_code_mapping():
    with open(FILENAME_INPUT, 'r') as f:
        letters = f.readline().strip().split(' ')
        code_words = f.readline().strip().split(' ')
    return {LETTERS: letters, CODE_WORDS: code_words}


def make_alphabet():
    with open(FILENAME_INPUT, 'r') as f:
        letters = f.readline().strip().split(' ')
    return letters


def separate_code_words(code_line: str, accepted_words: [str]) -> [str]:
    current_word = ''
    separated_code = []
    for bit in code_line:
        current_word += bit
        if current_word in accepted_words:
            separated_code.append(current_word)
            current_word = ''

    return separated_code


def get_code_orders(code_words: [str]) -> {str: int}:
    code_order_mapping = {}
    for i in range(len(code_words)):
        code_order_mapping[code_words[i]] = i
    return code_order_mapping


def decode(coding_line: [str], coding_system: {str: [str]}) -> [str]:
    code_orders = get_code_orders(coding_system[CODE_WORDS])
    decoded_line = []
    letters_buffer = coding_system[LETTERS][:]
    for code_word in coding_line:
        ind_to_move = code_orders.get(code_word)
        letter = letters_buffer[ind_to_move]
        decoded_line.append(letter)
        del letters_buffer[ind_to_move]
        letters_buffer.insert(0, letter)

    return decoded_line


def decode_from_alphabet_only(coding_line: [str], alph: [str]) -> [str]:
    decoded_line = []
    letters_buffer = alph[:]
    for code_word in coding_line:
        ind_to_move = int(code_word)
        letter = letters_buffer[ind_to_move]
        decoded_line.append(letter)
        del letters_buffer[ind_to_move]
        letters_buffer.insert(0, letter)

    return decoded_line


if __name__ == '__main__':

    print("Choose mode: 1 - from binary sequence, 2 - from orders' sequence")
    mode = int(input())

    if mode == FROM_ORDERS_MODE:
        alphabet = make_alphabet()
        while True:
            print("Enter binary sequence you want to decode, then position in BWT:")
            sequence, pos = input().split(',')
            coding_line_ = sequence.split(' ')
            transformed_seq = decode_from_alphabet_only(coding_line_, alphabet)
            print('Result:')
            print("".join(find_orig_sequence(transformed_seq, int(pos))))

    elif mode == FROM_BINARY_MODE:
        coding_system_ = make_letter_code_mapping()
        while True:
            print('Enter decimal sequence you want to decode, then position in BWT:')
            sequence, pos = input().split(',')
            coding_line_ = separate_code_words(sequence, coding_system_[CODE_WORDS])
            transformed_seq = decode(coding_line_, coding_system_)
            print('Result:')
            print("".join(find_orig_sequence(transformed_seq, int(pos))))
