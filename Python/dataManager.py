from bookShelf_data import BookShelf
from output import filters, display 
import datetime

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

def edit_book():
    edit_filter = filters()
    if not edit_filter:
        return

    display(edit_filter)
    
    while True:
        choice_edit = input('\nWrite the number of the book you want to edit: ')
        found_book = False
        for i, book in enumerate(edit_filter, 1):
            if choice_edit.isdigit() and int(choice_edit) == i:
                found_book = True
                keep_going = 'yes'
                while keep_going.lower() in ['yes', 'y']:
                    what_edit = input('Write what item you want to edit (ex: title, author, status, etc): ').lower()

                    if what_edit in book:
                        if what_edit in ['author', 'title', 'motive', 'review']:
                            new_value = input(f"Enter the new value for {what_edit}: ")
                            book[what_edit] = new_value
                            print("Book updated successfully!")

                            keep_going = input('Want to edit something else? (y/n) ')

                        elif what_edit == 'rating':
                            while True:
                                new_value = input('Enter new value for rating (1 to 5): ')
                                if new_value.isdigit() and 1 <= int(new_value) <= 5:
                                    book['rating'] = int(new_value)
                                    print("Book updated successfully!")

                                    keep_going = input('Want to edit something else? (y/n) ')
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

                                    print("Book updated successfully!")
                                    keep_going = input('Want to edit something else? (y/n) ')
                                    break
                                else:
                                    print('This is not a valid status. Please try again.')
                                    
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
                            break

                    else:
                        print("Invalid selection. Try again.")
                        
                break
        
        if found_book:
            break
        else:
            print("This book doesn't exist. Try again.")
    
def delete_book():
    delete_filter = filters()
    if delete_filter is None:
        return

    display(delete_filter)
    if delete_filter == []:
            print('\nThere is no book in this option.')
    else:
        while True:
            choice_delete = {}
            choice_delete = input('\nWrite the number of the book you want to delete: ')
            Found_Book = False
            for i, book in enumerate(delete_filter, 1):
                    if choice_delete.isdigit() and int(choice_delete) == i:
                        Found_Book = True
                        sure = input(f'Are you sure you want to delete {book['title']}? (y/n) ')

                        if sure.lower() == 'y' or sure.lower() == 'yes':
                            BookShelf.remove(book)
                            print('Book deleted with sucess!')
                        
                        else:
                            print('Ok! The book wont be deleted.')
                        break
                    if Found_Book:
                        break
                    else:
                        print("This book doesn't exist. Try again.")
