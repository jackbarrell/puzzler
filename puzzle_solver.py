# with open('words_alpha.txt', 'r') as f:
#     dictionary = [x.rstrip().lower() for x in f.readlines()]
#
# with open('first_names.all.txt', 'r') as f:
#     first_names = [x.rstrip().lower() for x in f.readlines()]
#
# with open('last_names.all.txt', 'r') as f:
#     last_names = [x.rstrip().lower() for x in f.readlines()]

def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    with open('first_names.all.txt') as word_file:
        first_names = set(word_file.read().split())

    with open('last_names.all.txt') as word_file:
        last_names = set(word_file.read().split())



    return valid_words, first_names, last_names

def puzzle_b():
    puzzle = '*sled re*nt'
    puzzle = '*stro sou*er'
    puzzle = '*ion fri*'
    puzzle = 'pa*ma vi*nt'
    first_word, second_word = puzzle.split(' ')

    i = 0
    for name in last_names:
        i += 1
        if i % 1000 == 0:
            print(round(i/(len(last_names) +len(first_names)) * 100), '%')

        word = first_word.replace('*', name)
        # print(word)
        if word in english_words:
            print('found a fkn word!!: ', word)
            possible_first_names.append((name, word))


    print('MOVING ON TO SECOND WORD')
    for name in last_names:
        i += 1
        if i % 1000 == 0:
            print(round(i/(len(last_names) +len(first_names)) * 100), '%')

        word = second_word.replace('*', name)
        # print(word)
        if word in english_words:
            print('found a fkn word!!: ', word)
            possible_second_names.append((name, word))

    possible_first_names.sort()
    possible_second_names.sort()

    # print("possible first names:")
    # for name in possible_first_names:
    #     print(name)
    #
    # print("\npossible second names:")
    # for name in possible_second_names:
    #     print(name)

    for first in possible_first_names:
        for second in possible_second_names:
            print(first[0], second[0])


if __name__ == '__main__':
    english_words, first_names, last_names = load_words()
    # demo print

# first_names = ['jack', 'sanjay', 'leah', 'john', 'bob', 'james']
# second_names = ['smith', 'hitch', 'blah', 'dole', 'charles']


    possible_first_names = []
    possible_second_names = []

    puzzle_b()
