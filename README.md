📚 AI-Based Book Recommendation System (NLP + Transformers)

This project implements an AI-powered book recommendation system using Natural Language Processing (NLP) and Transformer models. Users can describe their reading preferences (e.g., “I like mystery thrillers with complex characters”), and the system recommends similar books from the dataset. It also generates AI-based summaries for recommended books.

🚀 Features

✅ Recommends books based on semantic similarity
✅ Uses Sentence Transformers for text embeddings
✅ Uses Cosine Similarity to match user preferences with book descriptions
✅ AI-powered book summary generation using BART Transformer
✅ Interactive command-line interface
✅ Works with Goodreads sample dataset
✅ Filters English books
✅ Lightweight demo setup (100 books)

🛠️ Tech Stack

Python 3

Pandas, NumPy

Scikit-learn

Sentence-Transformers (MiniLM)

Hugging Face Transformers (BART Summarizer)

Goodreads Dataset (sample)

📦 Installation

pip install transformers sentence-transformers pandas numpy scikit-learn

python book_recommendation.py

🎯 How It Works

Loads a dataset of books from Goodreads

Adds sample descriptions to books

Converts descriptions into vector embeddings using Sentence Transformers

Takes user preferences as input

Computes cosine similarity between user input and book descriptions

Recommends the top-N most similar books

Uses BART summarization model to generate short summaries

🧠 Example

Input:

I enjoy thrilling mystery novels with complex characters

Output:

Recommended Books:
- Book Title 1 by Author (Rating: 4.2)
- Book Title 2 by Author (Rating: 4.0)
- Book Title 3 by Author (Rating: 3.9)

Summary:
A mystery thriller following a detective solving a series of murders...

⚙️ Requirements

Python 3.8+

Internet connection (to download dataset & models)

4GB+ RAM recommended (for transformer models)

🔮 Future Improvements

Use real book descriptions instead of sample text

Add user profile & history

Build a web app using Flask / Streamlit

Add genre filtering

Add collaborative filtering

Deploy as an API

🎓 Use Cases

Personalized book recommendations

Library systems

E-learning platforms

Online bookstores

AI-based reading assistants

👨‍💻 Author

Developed by: Raghini H
Project Type: Machine Learning / NLP / Recommendation System
