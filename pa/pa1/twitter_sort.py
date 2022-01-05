import sys
import re
import os

# PA 1: Tweets
# Version: 1.0
# Date: September 26, 2021
#
# This program merges and sorts two twitter feeds.


def main():
    '''
    interprets command line arguments for filename, calls functions, and outputs results to the console
    :return:
    '''
    if len(sys.argv) <= 1:
        print("Command line arguments not provided.")
    elif len(sys.argv) == 4:
        file1 = open(sys.argv[1], mode='r+', encoding='UTF8')
        file2 = open(sys.argv[2], mode='r+', encoding='UTF8')
        output = open(sys.argv[3], mode='w+', encoding='UTF8')
        filesize1 = os.path.getsize(sys.argv[1])
        filesize2 = os.path.getsize(sys.argv[2])
        if filesize1 == 0:
            print("%s is empty." % file1.name)
        elif filesize2 == 0:
            print("%s is empty." % file2.name)
        else:
            print("Reading files...")
            records_list1 = read_tweets(file1)
            records_list2 = read_tweets(file2)
            count1 = len(records_list1)
            count2 = len(records_list2)
            if count1 > count2:
                print(sys.argv[1] + " contained the most tweets with %s." % count1)
            elif count2 > count1:
                print(sys.argv[2] + " contained the most tweets with %s." % count2)
            else:
                print("Both files contain %s tweets." % count1)

            print("\nMerging files...")
            merged_list = merge_tweets(records_list1, records_list2)
            print("Files Merged.")

            print("\nWriting file...")
            write_tweets(merged_list, output)
            print("Files written.")

            print("\nDisplaying 5 newest tweeters and tweets.")
            i = 0
            while i < 5:
                temp = merged_list[i]
                print(temp['tweeter'] + " " + temp['tweet'])
                i += 1

            file1.close()
            file2.close()
            output.close()
    else:
        print("Command line arguments not valid.")


def read_tweets(file):
    '''
    reads a given file to create a list of records
    :param file: the file to read
    :return: the list of records
    '''
    records_list = []
    all_tags = []
    for s in file:
        dict = {}
        dict['tweeter'] = re.findall(r'^@\S+', s)[0]
        dict['tweet'] = re.search(r'\".+\"', s).group()
        date1 = re.findall(r'\d{4}\s\d{1,2}\s\d{1,2}', s)
        dict['year'] = re.search(r'\d{4}', date1[0]).group()
        date2 = re.findall(r'\s\d{1,2}\s\d{1,2}', date1[0])
        date3 = re.findall(r'\d{1,2}', date2[0])
        dict['month'] = date3[0]
        dict['day'] = date3[1]
        dict['time'] = re.search(r'\d\d\:\d\d\:\d\d', s).group()
        records_list.append(dict)
        tags = re.findall(r'\#\w+', s)
        i = 0
        while i < len(tags):
            all_tags.append(tags[i])
            i += 1

    # extra credit attempt:
    if len(all_tags) > 0:
        unique_tags = []
        hashtags = {}
        for item in all_tags:
            if item not in unique_tags:
                unique_tags.append(item)
                hashtags[item] = 1
            else:
                hashtags[item] += 1
        max_count = 0
        most_common = ''
        for tag, count in hashtags.items():
            if count > max_count:
                max_count = count
                most_common = tag
        print(most_common + " is the most common hashtag in %s." % file.name)
    else:
        print("There is no hashtag in %s." % file.name)

    return records_list


def merge_tweets(list1, list2):
    '''
    merges two lists of records in reverse chronological order
    :param list1: the first list of records
    :param list2: the second list of records
    :return: the merged list
    '''
    merged_list = []
    list1_index = 0
    list2_index = 0
    while list1_index < len(list1) and list2_index < len(list2):
        if time_calculator(list1[list1_index]) > time_calculator(list2[list2_index]):
            merged_list.append(list1[list1_index])
            list1_index += 1
        else:
            merged_list.append(list2[list2_index])
            list2_index += 1
    while list1_index < len(list1):
        merged_list.append(list1[list1_index])
        list1_index += 1
    while list2_index < len(list2):
        merged_list.append(list2[list2_index])
        list2_index += 1
    return merged_list


def time_calculator(dict):
    '''
    calculates time in seconds
    :param dict: the dictionary to refer to
    :return: time in seconds
    '''
    hour, minute, second = dict['time'].split(':')
    time = int(dict['year']) * 365 * 24 * 60 * 60 + int(dict['day']) * 24 * 60 * 60 + int(hour) * 60 * 60 + int(minute) * 60 + int(second)
    return time


def write_tweets(list, output):
    '''
    writes to the file output
    :param list: the list of records
    :param output: the output file
    :return:
    '''
    for item in list:
        for key, value in item.items():
            output.write(value + " ")
        output.write("\n")


if __name__ == '__main__':
    main()
