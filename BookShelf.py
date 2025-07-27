import datetime

BookShelf = []

def menu():
    while True:
        print('\n-----BOOKSHELF-----')
        print('1 - Add Book')
        print('2 - View Books')
        print('3 - Edit Book')
        print('4 - Rank Books')
        print('5 - Delete Book')
        print('6 - Quit')

        menu_choice = input('\nType the number of your choice: ')
        if menu_choice == '1':
            add_book()
        elif menu_choice == '2':
            view_books()
        elif menu_choice == '3':
            edit_book()
        elif menu_choice == '4':
            ranking_books()
        elif menu_choice == '5':
            delete_book()
        elif menu_choice == '6':
            print('\nThanks for using Bookshelf! See you next time! (your data will be lost)')
            break
        else:
            print('\nThis is not a valid option. Please try again.')

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
            rating = input('Enter book rating: (1-5 stars): ')
            if rating.isdigit() and 6 > int(rating) > 0 :
                break
            else:
                print('This is not a valid number. Please try again.')

        review = input('Enter book review: ')
        while True:
            conclusionDate = input('Enter book conclusion date: (dd/mm/yyyy) ) ')
            try:
                datetime.datetime.strptime(conclusionDate, "%d/%m/%Y")
                break
            except ValueError:
                print('This is not a valid date. Please try again.')

        book['rating'] = rating
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
            current_page = input('Enter your current page: ')
            if current_page.isdigit():
                break
            else:
                print('This is not a valid number. Please try again.')

        progress = int((int(current_page)/int(pages))*100)
        book['progress'] = progress

    elif status == '3':
        motive = input('Enter the reason you dropped this book: ')
        book['motive'] = motive

    BookShelf.append(book)
    print('\nyour book has been added to the shelf.')


def view_books():
    if not BookShelf:
        print('\nThere are no books registered in the shelf.')
        return

    print('\nHow would you like to view your books? ')
    print('1. View all books')
    print('2. View by especific status')
    print('3. Search by name')
    print('4. View by especific rating')
    print('5. View by especific author')

    view_choice = input('\nEnter the number of your choice: ')

    view_filter = []

    if view_choice == '1':
        view_filter = BookShelf

    elif view_choice == '2':
        view_status = input ('\nWich status you want to view? (1. complete, 2. reading, 3. dropped, 4. want to read) ')
        if view_status.isdigit and 0 < int(view_status) < 5:
            view_filter = [book for book in BookShelf if book.get('status') == view_status]
        else:
            print('\nThis is not a valid number. Please try again.')
            return
        
    elif view_choice == '3':
            view_name = input ('\nWich title you want to search? ')
            view_filter = [book for book in BookShelf if book.get('title').replace(' ', '').lower() == view_name.replace(' ', '').lower()]

    elif view_choice == '4':
        view_rating = input ('\nWich rating you want to view? (1-5) ')
        if view_rating.isdigit and 0 < int(view_rating) < 6:
            view_filter = [book for book in BookShelf if book.get('rating') == view_rating]
        else:
            print('\nThis is not a valid number. Please try again.')
            return

    elif view_choice == '5':
        view_author = input ('\nWich author you want to view? ')
        view_filter = [book for book in BookShelf if book.get('author').replace(' ', '').lower() == view_author.replace(' ', '').lower()]
    
    else:
        print('\nThis is not a valid option. Please try again.')

    if view_filter == []:
        print('\nThere is no book in this option.')
    
    else:
        print('\n----- YOUR BOOKS -----')
        for i, book in enumerate(view_filter, 1):
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
                print(f"Rating: {book['rating']} stars")
                print(f"Review: {book['review']}")
                print(f"Conclusion Date: {book['conclusion_date']}")

            elif book['status'] == '2':
                print(f"Reading progress: {book['progress']}%")

            elif book['status'] == '3':
                print(f"Reason for dropping the book: {book['motive']}")

def edit_book():
    print('test')
def ranking_books():
    print('test')
def delete_book():
    print('test')

menu()
