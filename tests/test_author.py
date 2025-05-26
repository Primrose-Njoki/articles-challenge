from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.setup import setup_db

setup_db()
def test_create_author():
    author = Author.create("Test Author")
    assert author.name == "Test Author"

def test_author_articles_and_magazines():
    author = Author.create("Multi Writer")
    mag = Magazine.create("MultiMag", "General")
    article = author.add_article(mag, "Sample Title")
    
    assert article.title == "Sample Title"
    assert article.author_id == author.id
    assert article.magazine_id == mag.id

    assert len(author.articles()) >= 1
    assert any(a.title == "Sample Title" for a in author.articles())

    assert len(author.magazines()) >= 1
    assert any(m.name == "MultiMag" for m in author.magazines())

def test_topic_areas():
    author = Author.create("Topic Tester")
    mag1 = Magazine.create("CatMag", "Pets")
    mag2 = Magazine.create("FitMag", "Fitness")
    author.add_article(mag1, "Cats are Great")
    author.add_article(mag2, "Fitness for All")

    areas = author.topic_areas()
    assert "Pets" in areas
    assert "Fitness" in areas
