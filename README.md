# Python Chatbot

The Python Chatbot is a chatbot that provides relevant code snippet based on the related Python question asked. It also provides top 3 codes along with their ranks in which they were predicted for the question. This chatbot acts like a small-scale retrieval-based system. The technology used to create this bot is Django, NLP, Machine Learning, and SQLite 3 serving as a database. K-Nearest Neighbors is used to find top 3 most relevant code snippets and metric used is Cosine Similarity to measure how similar two text vectors are.

## Setup Instructions

Follow these steps to set up the project:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 4. Load Dataset
Since `Python codes.csv` is included in the repository, download the dataset and place it in the project root.

### 5. Generate `.pkl` Files (Model and Vectorizer)
In `Chatbot.ipynb`, run all the cells to generate:
- `chatbot_model.pkl`
- `vectorizer.pkl`

### 6. Database Setup
Since `db.sqlite3` is excluded from the repository, run the following command to create the database and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser (Optional, for Admin Access)
```bash
python manage.py createsuperuser
```

### 8. Installing WhiteNoise

   ```
   pip install whitenoise
   ```
   
### 8. Run the Server
```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) to access the chatbot.

## Security Setup
To protect your project’s security:
- Move your `SECRET_KEY` to a `.env` file and add `.env` to your `.gitignore`.
- In `settings.py`, replace:
```python
SECRET_KEY = 'your-secret-key'
```
With:
```python
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
```

## Usage
1. Enter a question in the text field.
2. The chatbot will predict and display the most relevant code snippet along with top 3 codes chosen and their rank.
3. Use the "Clear Query History" button to reset the history (delete previous history content).
