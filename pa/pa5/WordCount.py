# Hansol Lee, Anthony Chelf
# PA5: HashMap
# Version 1.0
# November 28, 2021
# A simple program which reads words from a file then stores the word and its count in a HashMap.

from HashMap import HashMap
import re


def main():
    map = HashMap(size=100)
    total_count = 0
    filename = input("Please enter a file name: ")
    try:
        r_file = open(filename, mode='r')
    except FileNotFoundError:
        print("File does not exist")
        return None

    for line in r_file:
        for word in line.split():
            # parse the word
            # make into lower case
            word = word.lower()
            # remove special characters except '
            new_word = re.sub(r"[^a-z']", "", word)
            # check if word exists in map
            if new_word not in map:
                # if does not exist: add word and count (1) to the map
                map.put(new_word, 1)
            else:
                # if exists: increment count (+= 1)
                count = map.get(new_word) + 1
                map.put(new_word, count)
            # update total_count
            total_count += 1
    # print total count of words in file
    print("total count: %s \n" % total_count)

    # prompt the user for a word
    word = ""
    while word != "Q" and word != "q":
        word = input("Try a word (enter 'Q' or 'q' to quit): ")
        # word exists: print count
        if word in map:
            count = map.get(word)
            print("Word '%s' has a count of %s \n" % (word, count))
        elif word == "Q" or word == "q":
            r_file.close()
        # word does not exists: let user know
        else:
            print("Word '%s' not found \n" % word)


if __name__ == '__main__':
    main()

