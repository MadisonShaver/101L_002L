'''CS 101 Lab
Program 10
Madison Shaver
mlsy7z@umkc.edu

PROBLEM: Get a file input from the user and output the most frequently 
used words, number of words only used once, and number of unique words.

ALGORITHM:
    1. Start
    2. Get file from user
    3. Open file (use exception handling in case invalid file is given)
    4. Split lines from file into words
    5. Strip whitespace, !, ?, ., , from all words in list and make all words lowercase
    6. Iterate through list to get counts of each word and add to a dictionary
    7. Sort dictionary in reverse value order
    8. Output most frequently used words table
    9. Iterate through dictionary and output first ten words and counts in table
    10. Iterate through values of dictionary to count the number of words that only occur once
    11. Use the length of the dictionary as the number of unique words
'''

def open_file():
    while True:
        try:
            print()
            user_file = input('Enter the name of the file to open ')
            file = open(user_file)
            return file
        except FileNotFoundError:
            print('Could not open file {}'.format(user_file))
            print('Please try again')

def clean_words(file):
    words = []
    file_list = file.readlines()
    for line in file_list:
        line_words = line.split()
        words += [word.strip(" ,.!?").lower() for word in line_words if len(word) > 3]
    return words

def get_word_counts(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    sort_word_counts = {}
    for v in sorted(word_counts.values(), reverse=True):
        for k in word_counts:
            if v == word_counts[k]:
                sort_word_counts[k] = v
    return sort_word_counts

def output_top_ten(word_counts):
    i = 0
    print()
    print('Most frequently used words')
    print('{:>2}{:>15}{:>20}'.format('#', 'Word', 'Freq.'))
    print('{:=^37}'.format(''))
    for k,v in word_counts.items():
        print('{:>2}{:>15}{:>20}'.format((i + 1), k, v))
        i += 1
        if i >= 10:
            break

def output_uniques(word_counts):
    words_once = 0
    for v in word_counts.values():
        if v == 1:
            words_once += 1
    print()
    print('There are {} words that occur only once'.format(words_once))
    print('There are {} unique words in the document'.format(len(word_counts)))

if __name__ == '__main__':
    file = open_file()
    words = clean_words(file)
    word_counts = get_word_counts(words)
    output_top_ten(word_counts)
    output_uniques(word_counts)