
# Content-Based Book Recommender

![Alt Text](https://github.com/Uttam-Grade-McK/LLM-Large-Language-Models/blob/main/Gradio_Book_Recommendation/github_image.png)


This project implements a basic content-based book recommender system using Python. It takes a book title as input and recommends 5 similar books based on textual attributes such as summaries.

## Features
- **Preprocessing**: Cleans and processes book summaries to ensure meaningful feature extraction.
- **Feature Extraction**: Uses TF-IDF to vectorize summaries and generate feature matrices.
- **Similarity Computation**: Calculates pairwise cosine similarity between books.
- **Recommendation Generation**: Recommends top 5 books based on the input book's similarity scores.
- **Simple UI**: Deployed using Hugging Face Spaces, allowing users to input a book title and get recommendations.

## Requirements
- Python 3.7+
- Libraries:
  - `numpy`
  - `pandas`
  - `scikit-learn`
  - `streamlit` (for the UI)
  - `datasets` (for handling datasets)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Project Structure
```
.
├── app.py                # Streamlit app for user interface
├── recommender.py        # Core logic for the recommender system
├── preprocessing.py      # Functions for data cleaning and preprocessing
├── data/                 # Dataset files
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Usage
### Step 1: Data Preparation
1. Place the dataset in the `data/` folder. The dataset should contain the following columns:
   - `book_name`: Title of the book
   - `summaries`: Textual summaries of the books
2. Ensure the dataset is cleaned (e.g., remove duplicates, handle missing values).

### Step 2: Running the Recommender Locally
1. Preprocess the data and compute the similarity matrix:
   ```bash
   python recommender.py
   ```
2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the provided localhost link in your browser.

### Step 3: Using the Hugging Face Space
1. The app is deployed on Hugging Face Spaces for easy access.
2. Enter the book title in the input box and get 5 recommendations.

## How It Works
1. **Preprocessing**:
   - Cleans book summaries (removes punctuation, converts to lowercase, etc.).
   - Drops duplicate and missing values.
2. **Feature Extraction**:
   - Uses TF-IDF vectorization to create a feature matrix from the cleaned summaries.
3. **Similarity Calculation**:
   - Computes pairwise cosine similarity scores between all books.
4. **Recommendation**:
   - Sorts books by similarity scores (excluding the queried book itself) and returns the top 5.

## Error Handling
- Handles invalid book titles by providing appropriate error messages.
- Ensures robust preprocessing to avoid issues with null or missing data.

## Acknowledgements
- **TF-IDF**: Used for feature extraction (scikit-learn).
- **Cosine Similarity**: Pairwise similarity computation (scikit-learn).
- **Streamlit**: Lightweight UI for the app.
- **Hugging Face Spaces**: Hosting platform for the recommender app.

## Future Enhancements
- Use pre-trained embeddings (e.g., BERT or Sentence Transformers) for improved recommendations.
- Incorporate additional attributes (e.g., genres, author names) into the recommendation logic.
- Optimize deployment for faster response times.

