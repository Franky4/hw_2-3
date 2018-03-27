import chardet
import os
import json


def whats_coding(file):
    detector = chardet.UniversalDetector()  # интересно получить обратную связь, правильно ли использую detector
    with open(file, 'rb') as fl:
        for ln in fl:
            detector.feed(ln)
            if detector.done:
                break
        detector.close()
    return detector.result


def top_ten_words(file):
    my_dict = {}
    with open(file, encoding=whats_coding(file)['encoding']) as f:
        data = json.load(f)
        a = data['rss']['channel']['items']
        for line in a:
            split_line = line['description'].strip().lower().split(' ')
            for item in split_line:
                if len(item) > 6:
                    my_dict[item] = my_dict.get(item, 0) + 1
    my_sort_dict = sorted(my_dict, key=my_dict.get, reverse=True)
    my_sort_value = sorted(my_dict.values(), reverse=True)
    print('TOP-10 слов для файла {}'.format(file))
    i = 1
    for item, value in zip(my_sort_dict[:10], my_sort_value[:10]):
        print('{}: {} - {}'.format(i, item, value))
        i += 1


def main():
    my_dir = "files/"
    my_format_file = '.json'
    for d, dirs, files in os.walk(my_dir):
        for f in files:
            if my_format_file in f:
                my_file = my_dir + f
                top_ten_words(my_file)
                # print(my_file)
                # print(whats_coding(my_file))


if __name__ == '__main__':
    main()



