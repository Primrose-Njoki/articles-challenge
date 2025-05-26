from lib.models.author import Author
from lib.models.magazine import Magazine

def seed_data():
    author1 = Author.create("Alice Walker")
    author2 = Author.create("Bob Smith")

    mag1 = Magazine.create("Tech World", "Technology")
    mag2 = Magazine.create("Health Daily", "Health")

    author1.add_article(mag1, "AI is the Future")
    author1.add_article(mag2, "Healthy Living Tips")
    author2.add_article(mag1, "Tech in 2025")
    author2.add_article(mag1, "Gadgets Review")
    author2.add_article(mag1, "The Rise of Robotics")
