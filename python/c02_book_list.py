#-*- coding: utf-8 -*-
#filename : c02_book_list.py

#책을 관리하는데, 관리하는 항목
#제목, 출판년도, 출판사, 페이지수, 가격, 재고유무

books = list() #또는 books = []

books.append({"subject":"Python","year":2016,"made":"publisher_A","page":123,"price":1000, "stock":True})
books.append({"subject":"C","year":2015,"made":"publisher_A","page":222,"price":1222, "stock":True})
books.append({"subject":"C++","year":2016,"made":"publisher_B","page":333,"price":3333, "stock":False})
books.append({"subject":"PHP","year":2013,"made":"publisher_C","page":444,"stock":4444, "stock":True})
books.append({"subject":"JSP","year":2014,"made":"publisher_B","page":555,"stock":5555, "stock":False})

book_count = len(books)

for n in range(0, book_count):
    print(books[n])

print("="*70)

for book in books:
    print(book)

##특정한 조건의 데이터만 출력하기
#2015년 이후의 데이터만 출력하기

print("="*70)
for book in books:
    if book["year"] >= 2015:
        print(book)

print("출판사 A의 책을 찾아서, 제목, 가격만 출력")

for book in books:
    if book["made"] == "publisher_A":
        print(book["subject"], book["price"])

print("재고가 있는 책을 찾아서, 제목만 출력하기")

for book in books:
    if book["stock"] == True:
        print(book["subject"])
