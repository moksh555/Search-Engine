# 🔍 Search Engine — From Scratch

A ground-up Python implementation of a search engine, built module by module to demonstrate the core concepts of information retrieval: web crawling, text preprocessing, inverted indexing, TF-IDF vector space retrieval, and PageRank. The project progresses from foundational algorithms to a fully functional Flask-based web search application.

## Project Structure

The repository is organized as a step-by-step learning progression:

```
1. Information Retrieval/    # Core IR algorithms
2. Web Spidering/            # BFS web crawler
3. PageRank/                 # Link graph + PageRank computation
4. Search Engine Application/ # Flask app using TF-IDF + PageRank (pickle-based)
5. Web Search Engine using Database/ # Flask app using SQLite + PageRank (persistent)
```

## Key Features

- **Inverted index** — custom implementation that maps terms to document IDs and positional offsets, supporting multi-term AND queries
- **Text preprocessing pipeline** — tokenization (`nltk`), stop word removal, stemming, and lemmatization
- **TF-IDF vector space retrieval** — `scikit-learn` TfidfVectorizer + cosine similarity for query-to-document ranking
- **BFS web crawler** — follows hyperlinks breadth-first, respects a max-pages limit; two versions: in-memory and SQLite-backed
- **PageRank integration** — builds a directed link graph with `networkx` and applies `nx.pagerank()` to rerank TF-IDF results
- **Flask web interface** — search bar UI with results page and a "not found" page for zero-match queries
- **SQLite persistence** — the Chapter 5 implementation stores crawled pages, cleaned content, and PageRank scores in a database for production-style querying

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| Web Framework | Flask |
| IR / ML | scikit-learn (TF-IDF, cosine similarity) |
| Graph / PageRank | networkx |
| NLP | NLTK (tokenization, stemming, lemmatization) |
| Web Scraping | requests + BeautifulSoup4 |
| Storage | pickle (Chapter 4) / SQLite via sqlite3 (Chapter 5) |

## Module Breakdown

### 1. Information Retrieval (`1.Information Retreival/`)

| File | What it demonstrates |
|---|---|
| `inverted_index.py` | Custom `invertedIndex` class with positional indexing and AND-query search |
| `lemmatization_and_tokenization.py` | NLTK word tokenization + WordNet lemmatization |
| `steeming.py` | Porter stemmer applied to token lists |
| `stopwords_removal.py` | Stop word filtering |
| `vector_space_retrieval.py` | TF-IDF vectorization + cosine similarity ranking |

### 2. Web Spidering (`2. Web Spidering/`)

BFS crawler that starts from a seed URL, follows `<a href>` links, avoids revisits, and stores crawled content in SQLite.

### 3. PageRank (`3.PageRank/`)

Fetches live pages, extracts outgoing links, constructs a `networkx.DiGraph`, and runs `nx.pagerank()` to score each page.

### 4. Search Engine Application (`4.Search Engine Apllication/`)

A complete Flask app that:
1. Pre-crawls 5 local HTML pages and serializes tokenized content to a pickle file
2. At query time: loads tokens, builds a TF-IDF matrix, computes cosine similarity against the query, constructs a PageRank graph weighted by similarity scores, and returns top results above a score threshold

### 5. Database-Backed Search Engine (`5. Web Search Engine using Database/`)

An upgraded version where crawled pages (including cleaned content, outgoing links, and PageRank scores) are stored in SQLite. The search endpoint queries the DB with a `LIKE` clause and orders by pre-computed `pagerank` score.

## Setup & Installation

**Prerequisites**: Python 3.x, pip.

1. **Clone the repository**
   ```bash
   git clone https://github.com/moksh555/Search-Engine.git
   cd Search-Engine
   ```

2. **Install dependencies**
   ```bash
   pip install flask scikit-learn networkx nltk requests beautifulsoup4
   python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')"
   ```

### Running the Chapter 4 Flask App

```bash
cd "4.Search Engine Apllication"
# Pre-build the token index (one-time)
python crawl_store_as_tokens_pickle.py
# Start the search server
python search_engine.py
```

Open `http://localhost:5000` and search against the local HTML pages.

### Running the Chapter 5 Database App

```bash
cd "5. Web Search Engine using Database"
# Crawl and store pages into SQLite
python web_spider.py
# Compute and store PageRank scores
python pagerank.py
# Start the search server
python web_search.py
```

Open `http://localhost:5000` to search the SQLite-backed index.
