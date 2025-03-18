def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents


def num_words(file_content):
    words_list = file_content.split()
    nums = 0
    for i in words_list:
        nums += 1
    return nums


def words_with_count(file_content):
    word_dict = {}
    for i in file_content:
        j = i.lower()
        if j not in word_dict:
            word_dict[j] = 1
        else:
            word_dict[j] += 1
    return word_dict

