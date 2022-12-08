class Letter:
    def __init__(self, notation: str, probability: float):
        self.notation = notation
        self.probability: float = probability
        self.code: [int] = []

    def get_code(self):
        return ''.join([str(code_letter) for code_letter in self.code])

    def __repr__(self):
        return f"({self.notation}) {self.probability}: {self.get_code()}"


FILENAME_INPUT = 'shannon_fano.conf'
TEST_LETTERS = [
    Letter('a', 0.05),
    Letter('b', 0.1),
    Letter('c', 0.05),
    Letter('d', 0.2),
    Letter('e', 0.03),
    Letter('f', 0.15),
    Letter('g', 0.01),
    Letter('h', 0.04),
]


def make_alphabet() -> [Letter]:
    with open(FILENAME_INPUT, 'r') as f:
        letters = f.readline().strip().split(' ')
        probabilities = [float(value) for value in f.readline().split(' ')]

    if len(letters) != len(probabilities):
        print('Error! Length are not equal!')
        return

    alphabet = []
    for i in range(len(letters)):
        alphabet.append(Letter(letters[i], probabilities[i]))

    return alphabet


def get_prob_sum(letters: [Letter]) -> float:
    sum_ = 0
    for letter_ in letters:
        sum_ += letter_.probability
    return sum_


def get_closer(left_num: float, average: float, right_num: float) -> float:
    if average - left_num < right_num - average:
        return left_num
    return right_num


def find_division_ind(letters: [Letter]) -> int:
    total_sum = get_prob_sum(letters)
    average = total_sum / 2
    running_sum = 0
    candidate_ind = 0

    for i in range(len(letters)):
        if running_sum > average:
            break
        running_sum += letters[i].probability
        candidate_ind = i

    if candidate_ind == 0:
        return candidate_ind
    if candidate_ind == len(letters) - 1:
        return candidate_ind - 1

    closer_num = get_closer(
        running_sum - letters[candidate_ind].probability,
        average,
        running_sum
    )

    if closer_num == running_sum:
        return candidate_ind
    return candidate_ind - 1


def add_code_symbol(letters: [Letter]):
    if len(letters) == 1:
        return

    division_ind = find_division_ind(letters)
    top_half = letters[: division_ind + 1]
    bottom_half = letters[division_ind + 1:]

    for letter_ in top_half:
        letter_.code.append(0)

    for letter_ in bottom_half:
        letter_.code.append(1)

    add_code_symbol(top_half)
    add_code_symbol(bottom_half)


def get_mapping(letters: [Letter]) -> dict:
    return {letter_.notation: letter_.get_code() for letter_ in letters}


def code_sense(sense: str, letters: [Letter]) -> str:
    result_code = []
    coding_system = get_mapping(letters)
    for bit in sense:
        result_code.append(coding_system.get(bit, "X"))
    return "".join(result_code)


if __name__ == '__main__':
    letters_ = make_alphabet()

    letters_sorted = list(sorted(letters_, reverse=True, key=lambda letter_: letter_.probability))
    add_code_symbol(letters_sorted)

    letters_in_alph_order = list(sorted(letters_sorted, key=lambda letter_: letter_.notation))
    for letter in letters_in_alph_order:
        print(letter)

    while True:
        print('Enter sequence you want to code:')
        seq_to_code = input()
        print('Result:')
        print(code_sense(seq_to_code, letters_in_alph_order))
