import datetime

BookShelf = []

def menu():
    while True:
        print('-----YOUR BOOKS-----')
        print('1 - Add Book')
        print('2 - View Books')
        print('3 - Edit Book')
        print('4 - Rank Books')
        print('5 - Delete Book')
        print('6 - Quit')

        choice = input('Type the number of your choice: ')
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            edit_book()
        elif choice == '4':
            ranking_books()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            print('Thanks for using book shelf! See you next time! (your data will be lost)')
            break
        else:
            print('This is not a valid option. Please try again.')
            menu()

def add_book():
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    while True:
        publication = input('Enter book publication year: ')
        if len(publication) == 4 and publication.isdigit():
            break
        else:
            print('This is not a valid publication year. Please try again.')

    while True:
        status = input('Enter book status: (1. complete, 2. reading, 3. dropped, 4. want to read) ')
        if status in ['1', '2', '3', '4']:
            break
        else:
            print('This is not a valid status. Please try again.')

    book = {
        'title' : title,
        'author' : author,
        'publication' : publication,
        'status' : status
    }

    if status == '1':

        while True:
            avaliation = input('Enter book avaliation: (1-5 stars): ')
            if avaliation.isdigit() and 6 > int(avaliation) > 0 :
                break
            else:
                print('This is not a valid avaliation. Please try again.')

        review = input('Enter book review: ')
        while True:
            conclusionDate = input('Enter book conclusion date: (dd/mm/yyyy) ) ')
            try:
                datetime.datetime.strptime(conclusionDate, "%d/%m/%Y")
                break
            except ValueError:
                print('This is not a valid date. Please try again.')

        book['avaliation'] = avaliation
        book['review'] = review
        book['conclusion_date'] = conclusionDate

    elif status == '2':
        while True:
            pages = input('Enter how many pages the book has: ')
            if pages.isdigit():
                break
            else:
                print('This is not a valid number. Please try again.')

        while True:
            current_page = input('Enter in what page you are: ')
            if current_page.isdigit():
                break
            else:
                print('This is not a valid number. Please try again.')

        progress = (int(current_page)/int(pages))*100
        book['progress'] = progress

    elif status == '3':
        motive = input('Enter why you dropped this book: ')
        book['motive'] = motive

    BookShelf.append(book)
    print('your book has been added to the shelf.')


def view_books():
    if not BookShelf:
        print('\nThere are no books registered in the shelf.')
        return

    print('\n----- ALL BOOKS -----')
    for i, book in enumerate(BookShelf, 1):
        print(f"\n----- Book #{i} -----")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication Year: {book['publication']}")

        status_text = "Unknown"
        if book['status'] == '1':
            status_text = "Complete"
        elif book['status'] == '2':
            status_text = "Reading"
        elif book['status'] == '3':
            status_text = "Dropped"
        elif book['status'] == '4':
            status_text = "Want to read"
        print(f"Status: {status_text}")

        if book['status'] == '1':
            print(f"Avaliation: {book['avaliation']} stars")
            print(f"Review: {book['review']}")
            print(f"Conclusion Date: {book['conclusion_date']}")

        elif book['status'] == '2':
            print(f"Reading progress: {book['progress']}%")

        elif book['status'] == '3':
            print(f"Motive of dropping the book: {book['motive']}")


def edit_book():
    
def ranking_books():

def delete_book():


menu()
