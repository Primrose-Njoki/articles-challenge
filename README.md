# articles-challenge

# Object Relations - Articles

A simple SQLite-based ORM system modeling Authors, Magazines, and Articles.

## Setup
1. `python -m venv env`
2. `source env/bin/activate`
3. `pip install pytest`
4. `python scripts/setup_db.py`
5. `python -c "from lib.db.seed import seed_data; seed_data()"`

## Run Tests
pytest

## Debug
`python lib/debug.py`

## features
Class-based Models (Author, Article, Magazine)

Raw SQL queries for full control and learning

Many-to-many relationship handling via articles

Query methods for real-world functionality

