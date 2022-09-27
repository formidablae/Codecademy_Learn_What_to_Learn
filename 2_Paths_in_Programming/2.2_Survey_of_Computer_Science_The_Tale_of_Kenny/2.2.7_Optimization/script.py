# This binary search function will look for a book on a bookshelf by iteratively narrowing down the area where it might find the book, until it finds the book.
def binary_search(lst, search_val):
    if len(lst) == 0:
        print("Book is not on the shelf!")
        return
    print("Checking the bookshelf and finding: {0}".format(lst[0]))
    mid = len(lst) // 2
    if lst[mid] == search_val:
        print("\nFound the book: {0}\n\n\n\n\n\n".format(search_val))
        return
    elif lst[mid] > search_val:
        binary_search(lst[:mid], search_val)
    else:
        binary_search(lst[(mid + 1):], search_val)

# This linear search looks through a bookshelf book by book until it finds the book it is looking for.    
def linear_search(lst, search_val):
    count = 0
    while len(lst) != 0:
        print("Checking the bookshelf and finding: {0}".format(lst[0]))
        if lst[0] == search_val:
            print("\nFound the book: {0}\n\n\n\n\n\n".format(search_val))
            return
        lst = lst[1:]
        count += 1
with open("books.csv") as f:
    books = f.read()
    bookshelf = sorted(books.split(","))
  
# Copy-paste the search code below:
linear_search(bookshelf, "Do Androids Dream of Electric Sheep?")
binary_search(bookshelf, "Do Androids Dream of Electric Sheep?")
