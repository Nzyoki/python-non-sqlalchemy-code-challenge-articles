class Article:
    all=[]
    def __init__(self, author, magazine, title):
        """if not isinstance(title,str): # Title must return a string of characters between 5 and 50
            raise TypeError("Title must be a string")
        if len(title)<5 or len(title)>50:
            raise ValueError("Title must be between 5 and 50 characters")"""
        
        self.author = author
        self.magazine = magazine
        self.title = title # title cannot be changed after instantiating
        Article.all.append(self)  # Add new article to all list

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,new_title):
        if hasattr(self,"title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title,str):
                if 5 <= len(new_title) <= 50:
                    self._title=new_title
                else:
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")
    
    @property
    def author(self):
        return self._author
    

    @author.setter
    def author(self, new_author):
        if isinstance(new_author,Author):
            self._author=new_author
        else:
            TypeError("Author must be an instance of Author class")
        


    @property
    def magazine(self):
        return self._magazine
    

    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be an instance of Magazine class")
        


        
class Author:
    def __init__(self, name):
       self.name=name
       """ if not isinstance(name,str): #name must be a string of characters longer than 0
            raise TypeError("Name must be a string")
        if len(name)==0:
            raise ValueError("Names must be longer than 0 characters")"""
       

    @property # name is a read-only property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        if hasattr(self,"name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name,str):
                if len(new_name):
                    self._name=new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self==article.author]
        
    
    def magazines(self):
        return list({article.magazine for article in self.articles()})
        
        
    
    def add_article(self, magazine, title):
       return Article(self,magazine,title)
       

    def topic_areas(self):
        topic_areas=list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None

       

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self,new_name):
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name=new_name
            else:
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")
    
    @property
    def category(self):
        return self._category
       
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str):
            if len(new_category):
                self._category=new_category
            else:
                 ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")
    
    
    def articles(self):
        return [article for article in Article.all if self==article.magazine]
        
    
    def contributors(self):
        return list({article.author for article in self.articles()})
       

    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:
            return None
    

    def contributing_authors(self):
        authors={}
        list_of_authors=[]
        for article in self.articles():
            if article.author in authors:
                authors[article.author]+=1
            else:
                authors[article.author]=1
        for author in authors:
            if authors[author]>=2:
                list_of_authors.append(author)
        if (list_of_authors):
            return list_of_authors
        else:
            return None
       

        
      
    