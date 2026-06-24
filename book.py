import requests
from dotenv import load_dotenv
import os

load_dotenv()

def search_books(userdes):
    url = "https://www.googleapis.com/books/v1/volumes"

    API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY") 

    params = {
        "q": userdes,
        "maxResults": 5,  
        "key": API_KEY  
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        books = response.json().get("items", [])
        recommended = []

        for book in books:
            title = book["volumeInfo"].get("title", "No title available")
            author = book["volumeInfo"].get("authors", ["Unknown author"])[0]
            description = book["volumeInfo"].get("description", "No description available")
            recommended.append((title, author, description))

        return recommended
    else:
        
        print(f"Error: API returned status code {response.status_code}")
        return []


def display(userdes):

    recommendations = search_books(userdes)

    if recommendations:
        for tit, a, des in recommendations:
            print(f"Title: {tit}")
            print(f"Author: {a}")
            print(f"Description: {des}")
            print("\n")
    else:
        print("No book recommendations found.")

userdes = input("Enter a description of the book you're looking for: ")
display(userdes)

