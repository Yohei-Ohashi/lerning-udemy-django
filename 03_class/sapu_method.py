import json


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(
            f"タイトル: {self.title}\n"
            f"著者: {self.author}\n"
            f"価格: {self.price:,}円"
        )

    @staticmethod
    def sort_books_by_price(books):
        return sorted(books, key=lambda x: x.price)

    @classmethod
    def from_json(cls, book_json):
        book_dict = json.loads(book_json)
        return cls(book_dict["title"], book_dict["author"], book_dict["price"])


class Comic(Book):
    type = "漫画"


class Photo(Book):
    type = "写真集"


book_1 = Book("はらぺこあおむし", "エリック・カール", 1320)
book_2 = Book("老人と海", "ヘミングウェイ", 1650)
book_3 = Book("名探偵コナン(1巻)", "青山 剛昌", 499)

result = Book.sort_books_by_price([book_1, book_2, book_3])

for book in result:
    print(f"{book.title}: {book.price}円")

book_1 = Book.from_json(
    '{"title": "はらぺこあおむし", "author": "エリック・カール", "price": 1320}'
)
print(type(book_1))
book_1.display_info()

comic_1 = Comic.from_json(
    '{"title": "名探偵コナン(1巻)", "author": "青山 剛昌", "price": 499}'
)

photo_1 = Photo.from_json(
    '{"title": "世界の路地", "author": "PIE BOOKS", "price": 1980}'
)

print(f"{type(comic_1)}: {comic_1.title}")
print(f"{type(photo_1)}: {photo_1.title}")