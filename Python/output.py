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
            print(f"Reason for dropping the book(motive): {book['motive']}")
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

def ranking_books():
    ranking1 = [book for book in BookShelf if book.get('rating') == '1']
    ranking2 = [book for book in BookShelf if book.get('rating') == '2']
    ranking3 = [book for book in BookShelf if book.get('rating') == '3']
    ranking4 = [book for book in BookShelf if book.get('rating') == '4']
    ranking5 = [book for book in BookShelf if book.get('rating') == '5']

    print('----- 1 STAR -----')
    if ranking5 == []:
        print('There`s no books with this rating!')
    else:
        for book in ranking1:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")

    print('\n----- 2 STAR -----')
    if ranking2 == []:
        print('There`s no books with this rating!')
    else:
        for book in ranking2:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")

    print('\n----- 3 STAR -----')
    if ranking3 == []:
        print('There`s no books with this rating!')
    else:
        for book in ranking3:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")

    print('\n----- 4 STAR -----')
    if ranking4 == []:
        print('There`s no books with this rating!')
    else:
        for book in ranking4:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")

    print('\n----- 5 STAR -----')
    if ranking5 == []:
        print('There`s no books with this rating!')
    else:
        for book in ranking5:
            print(f"\nTitle: {book['title']}")
            print(f"Author: {book['author']}")