import requests
from IPython.display import display, HTML

def search_books(user_description):
    url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        "q": user_description,
        "maxResults": 5  
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        books = response.json().get("items", [])
        recommended_books = []

        for book in books:
            title = book["volumeInfo"].get("title", "No title available")
            author = book["volumeInfo"].get("authors", ["Unknown author"])[0]
            description = book["volumeInfo"].get("description", "No description available")
            recommended_books.append((title, author, description))

        return recommended_books
    else:
        return []

def display_recommendations(user_description):
    recommendations = search_books(user_description)

    if recommendations:
        for title, author, description in recommendations:
            display(HTML(f"<h3>{title}</h3><p><strong>Author:</strong> {author}</p><p>{description}</p><hr>"))
    else:
        display(HTML("<p>No books found based on your description. Try a different one!</p>"))

user_description = input("Enter a description of the book you're looking for: ")
display_recommendations(user_description)
