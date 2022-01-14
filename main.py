import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'problems.settings')

import django

django.setup()


from demo.models import Author, Book

# author = Author.objects.get(name='..').select_related('books')  #1
for book in Book.objects.all().select_related('author'):
    print(book.title, book.author.name)

"SELECT * FROM book"
"SELECT * FROM book INNER JOIN author ON book.author_id=author.id"
