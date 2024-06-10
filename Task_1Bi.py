class Book:
  def _init_(self , title , author , publisher , price , royalty , copies):
    self.title = title
    self.author = author
    self.publisher = publisher
    self.price = price
    self.royalty = royalty
    self.copies = copies

  def set_title(self , x):
      self.title = x
  def set_author(self , x):
      self.author = x
  def set_publisher(self , x):
      self.publisher = x
  def set_price(self , x):
      self.price = x
  def set_copies(self , x):
      self.copies = x

  def get_title(self):
      return self.title
  def get_author (self):
      return self.author
  def get_publisher(self):
      return self.publisher
  def get_price(self):
      return self.price

  def royalty_method(self):
    if self.copies <= 500 :
      self.royalty  = 0.1*self.price*self.copies
    if self.copies > 500 and self.copies <= 1500:
      self.royalty = 0.1*self.price*500 + 0.125*self.price*(self.copies - 500)
    if self.copies > 1500 :
      self.royalty = 0.1*self.price*500 + 0.125*self.price*1000 + 0.15*self.price*(self.copies - 1500)

    return self.royalty


Ebook = Book()
Ebook.set_title("Software Engineering")
Ebook.set_author("NILESH KUMAR")
Ebook.set_publisher("SkillRAAce")
Ebook.set_price(500)
print("Title of the book is : " , Ebook.get_title())
print("Author of the book is : "  , Ebook.get_author())
print("Publisher of the book is : " , Ebook.get_publisher())
print("Price of the book is : " , Ebook.get_price())

Ebook.set_copies(2000)
Ebook.royalty_method()
print("Royalty of a book is " , Ebook.royalty_method())