from bs4 import BeautifulSoup
import requests

categories = {
    "Mystery": "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "Religion": "https://books.toscrape.com/catalogue/category/books/religion_12/index.html",
    "Crime": "https://books.toscrape.com/catalogue/category/books/crime_51/index.html",
    "Non-Fiction": "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html",
    "Science Fiction": "https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html",
    "Sports and Games": "https://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html",
    "Paranormal": "https://books.toscrape.com/catalogue/category/books/paranormal_24/index.html",
    "Horror": "https://books.toscrape.com/catalogue/category/books/horror_31/index.html",
    "Business": "https://books.toscrape.com/catalogue/category/books/business_35/index.html"
}

print("Please select a category:")
for i, category in enumerate(categories.keys(), 1):
    print(f"{i}. {category}")

choice = int(input("Enter the number of your chosen category: "))
selected_category = list(categories.keys())[choice - 1]
url = categories[selected_category]

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, "lxml")

books = soup.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

rating_dict = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

print(f"{'Book Name':<60} {'Price':<10} {'Availability':<20} {'Rating':<10}")
print("-" * 100)

for book in books:
    name = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    availability = book.find('p', class_='instock availability').text.strip()
    rating_tag = book.find('p', class_='star-rating')
    rating_class = rating_tag['class'][1]
    rating = rating_dict.get(rating_class, "No rating found")
    
    print(f"{name:<60} {price:<10} {availability:<20} {rating} stars")
