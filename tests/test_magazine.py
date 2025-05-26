from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.setup import setup_db

setup_db()
def test_create_magazine():
    mag = Magazine.create("Test Mag", "Science")
    assert mag.name == "Test Mag"
    assert mag.category == "Science"

def test_magazine_articles_and_contributors():
    mag = Magazine.create("WritersWeekly", "Writing")
    author1 = Author.create("Alice")
    author2 = Author.create("Bob")

    author1.add_article(mag, "How to Write Well")
    author2.add_article(mag, "Creative Fiction")

    assert len(mag.articles()) >= 2
    assert "How to Write Well" in mag.article_titles()
    assert "Creative Fiction" in mag.article_titles()

    contributors = mag.contributors()
    assert any(a.name == "Alice" for a in contributors)
    assert any(a.name == "Bob" for a in contributors)

def test_contributing_authors():
    mag = Magazine.create("HeavyWriters", "Deep Stuff")
    author = Author.create("Marathon Writer")
    for i in range(3):
        author.add_article(mag, f"Longform Part {i+1}")

    assert any(a.name == "Marathon Writer" for a in mag.contributing_authors())
