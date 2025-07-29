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
            conclusion_date = input('Enter book conclusion date: (dd/mm/yyyy) ) ')
            try:
                datetime.datetime.strptime(conclusion_date, "%d/%m/%Y")
                break
            except ValueError:
                print('This is not a valid date. Please try again.')

        book['rating'] = rating
        book['review'] = review
        book['conclusion_date'] = conclusion_date

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

def filters():
    print('\nHow would you like to view your books? ')
    print('1. View all books')
    print('2. View by especific status')
    print('3. Search by name')
    print('4. View by especific rating')
    print('5. View by especific author')

    filter_choice = input('\nEnter the number of your choice: ')

    filter = []

    if filter_choice == '1':
        filter = BookShelf

    elif filter_choice == '2':
        filter_status = input ('\nWhich status you want to view? (1. complete, 2. reading, 3. dropped, 4. want to read) ')
        if filter_status.isdigit() and 0 < int(filter_status) < 5:
            filter = [book for book in BookShelf if book.get('status') == filter_status]
        else:
            print('\nThis is not a valid number. Please try again.')
            return
        
    elif filter_choice == '3':
            filter_name = input ('\nWhich title you want to search? ')
            filter = [book for book in BookShelf if book.get('title').replace(' ', '').lower() == filter_name.replace(' ', '').lower()]

    elif filter_choice == '4':
        filter_rating = input ('\nWhich rating you want to view? (1-5) ')
        if filter_rating.isdigit() and 0 < int(filter_rating) < 6:
            filter = [book for book in BookShelf if book.get('rating') == filter_rating]
        else:
            print('\nThis is not a valid number. Please try again.')
            return

    elif filter_choice == '5':
        filter_author = input ('\nWhich author you want to view? ')
        filter = [book for book in BookShelf if book.get('author').replace(' ', '').lower() == filter_author.replace(' ', '').lower()]
    
    else:
        print('\nThis is not a valid option. Please try again.')

    if filter == []:
        print('\nThere is no book in this option.')

    return filter

def display(view_filter):
    print('\n----- YOUR BOOKS -----')
    for i, book in enumerate(view_filter, 1):
        print(f"\n----- Book #{i} -----")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Publication: {book['publication']}")

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
            print(f"Conclusion_date: {book['conclusion_date']}")

        elif book['status'] == '2':
            print(f"Reading progress: {book['progress']}%")

        elif book['status'] == '3':
            print(f"Reason for dropping the book: {book['motive']}")
    return

def view_books():

    view_filter = filters()
    if view_filter is None:
        return

    if not BookShelf:
        print('\nThere are no books registered in the shelf.')
        return
    
    else:
        display(view_filter)

def edit_book():
    edit_filter = filters()
    if edit_filter is None:
        return

    display(edit_filter)
    choice_edit = input('Write the number of the book you want to edit: ')
    for i, book in enumerate(edit_filter, 1):
            if choice_edit.isdigit() and int(choice_edit) == i:
                keep_going = 'yes'
                while keep_going.lower() in ['yes', 'y']:
                    what_edit = input('Write what item you want to edit (ex: title, author, status, etc): ').lower()

                    if what_edit in book:
                        if what_edit in ['author', 'title', 'motive', 'review']:
                            new_value = input(f"Enter the new value for {what_edit}: ")
                            book[what_edit] = new_value
                            print("Book updated successfully!")

                            keep_going = input('Want to edit something else? (y/n)')

                        elif what_edit == 'rating':
                            while True:
                                new_value = input('Enter new value for rating (1 to 5): ')
                                if new_value.isdigit() and 1 <= int(new_value) <= 5:
                                    book['rating'] = int(new_value)
                                    print("Book updated successfully!")

                                    keep_going = input('Want to edit something else? (y/n)')
                                    break
                                else:
                                    print('This is not a valid number. Please try again.')

                        elif what_edit == 'status':
                            while True:
                                status = input('Enter book status: (1. complete, 2. reading, 3. dropped, 4. want to read): ')
                                if status in ['1', '2', '3', '4']:
                                    book['status'] = status
                                    if status == '1':

                                        while True:
                                            rating = input('Enter book rating: (1-5 stars): ')
                                            if rating.isdigit() and 6 > int(rating) > 0 :
                                                break
                                            else:
                                                print('This is not a valid number. Please try again.')

                                        review = input('Enter book review: ')
                                        while True:
                                            conclusion_date = input('Enter book conclusion date: (dd/mm/yyyy) ) ')
                                            try:
                                                datetime.datetime.strptime(conclusion_date, "%d/%m/%Y")
                                                break
                                            except ValueError:
                                                print('This is not a valid date. Please try again.')

                                        book['rating'] = rating
                                        book['review'] = review
                                        book['conclusion_date'] = conclusion_date

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
                                        motive = input('Enter the reason you dropped this book: ').strip()
                                        book['motive'] = motive

                                else:
                                    print('This is not a valid status. Please try again.')

                                print("Book updated successfully!")
                                keep_going = input('Want to edit something else? (y/n) ')


                        elif what_edit == 'conclusion_date':
                            while True:
                                conclusion_date = input('Enter book conclusion date (dd/mm/yyyy): ')
                                try:
                                    datetime.datetime.strptime(conclusion_date, "%d/%m/%Y")
                                    book['conclusion_date'] = conclusion_date
                                    print("Book updated successfully!")

                                    keep_going = input('Want to edit something else?  (y/n) ')
                                    break
                                except ValueError:
                                    print('This is not a valid date. Please try again.')

                        elif what_edit == 'publication':
                            while True:
                                publication = input('Enter book publication year: ')
                                if len(publication) == 4 and publication.isdigit():
                                    book['publication'] = publication
                                    print("Book updated successfully!")

                                    keep_going = input('Want to edit something else? (y/n) ')
                                    break
                                else:
                                    print('This is not a valid publication year. Please try again.')

                        elif what_edit == 'progress':
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

                            progress = int((int(current_page) / int(pages)) * 100)
                            book['progress'] = progress
                            print("Book updated successfully!")
                            
                            keep_going = input('Want to edit something else? (y/n) ')
                        
                else:
                    print("Invalid selection. Try again.")
            return

def ranking_books():
    print('test')
def delete_book():
    print('test')

menu()