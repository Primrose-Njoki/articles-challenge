from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.setup import setup_db

setup_db()
def test_create_article():
    author = Author.create("Article Tester")
    mag = Magazine.create("Test Mag", "Tech")
    article = Article.create("Test Article", author.id, mag.id)

    assert article.title == "Test Article"
    assert article.author_id == author.id
    assert article.magazine_id == mag.id

def test_find_article_by_id():
    author = Author.create("Findy McFindface")
    mag = Magazine.create("Finder's Mag", "Mystery")
    article = Article.create("Where Am I?", author.id, mag.id)

    found = Article.find_by_id(article.id)
    assert found is not None
    assert found.title == "Where Am I?"
    assert found.author_id == author.id
    assert found.magazine_id == mag.id
