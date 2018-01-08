# put your code here.

import sys
from string import punctuation
from collections import Counter

def word_count(filename):
    """Open file, iterate over words, return word count for each word

    Upper & lower case are seen as separate values

    """

    poem = open(filename)

    word_counts = {}

    for line in poem:
        line = line.rstrip().split(" ")
        for word in line:
            word = word.lower()
            if word[-1] in punctuation:
                word = word[0:-1]
            if word[0] in punctuation:
                word = word[1:]
            # current_count_for_this_word = word_counts.get(word)
            # if current_count_for_this_word == None:
            #     word_counts[word] = 1
            # else:
            #     word_counts[word] = current_count_for_this_word + 1

            # Alternate solution
            # if word in word_counts:
                # word_counts[word] = word_counts.get(word) + 1
            # else:
            #     word_counts[word] = 1

            # Another
            word_counts[word] = word_counts.get(word, 0) + 1

# since .get doesn't set the key, why does this work?
    # poem.close()

    # for word in word_counts:
    #     count = word_counts[word]
    #     print word, count

    # words_with_counts = word_counts.iteritems()
    for k, v in word_counts.iteritems():
        print k, v

word_count(sys.argv[1])

