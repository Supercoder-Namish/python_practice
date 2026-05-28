dict_1 = {
    'The Hobbit': 'J.R.R. Tolkien' ,
    'To Kill a Mockingbird': 'Harper Lee' ,
    'The Hunger Games': 'Suzanne Collins',
    'Percy Jackson': 'Rick Riordan'
}

def append():
    dict_1['Harry Potter']= 'J K Rowling'

def check_if_book_available(book_name):
    if book_name in dict_1:
        return True
    else:
        return False

def check_if_book_absent(book_name):
    if not book_name in dict_1:
        return True
    else:
        return False



if __name__ == '__main__':
    append()
    print(dict_1)

    print(check_if_book_available('The Hobbit'))
    print(check_if_book_available('Jungle Book'))
    print('-------------------------------')
    print(check_if_book_absent('The Hobbit'))
    print(check_if_book_absent('Jungle Book'))