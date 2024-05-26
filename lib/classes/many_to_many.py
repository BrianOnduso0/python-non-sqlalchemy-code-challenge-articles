class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise TypeError("title must be a string")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        # Automatically add this article to the author's and magazine's list of articles
        author._add_article(self)
        magazine._add_article(self)

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Author name is immutable")

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

    def _add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(category, str):
            raise TypeError("category must be a string")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must not be empty")

        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Magazine name is immutable")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        raise AttributeError("Magazine category is immutable")

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        authors = {}
        for article in self._articles:
            author = article.author
            authors[author] = authors.get(author, 0) + 1
        return [author for author, count in authors.items() if count > 2]

    def _add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)
