from dataManager import add_book, edit_book, delete_book
from output import view_books, ranking_books

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

menu()