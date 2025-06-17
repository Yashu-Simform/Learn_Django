# Django ORM:

### Django ORM and corresponding SQL query
| Django ORM Concept | What it does                          | Corresponding SQL Concept                                      |
| ------------------ | ------------------------------------- | -------------------------------------------------------------- |
| `objects` manager  | Entry point to query the model        | Table access & query execution                                 |
| QuerySet           | Lazy, chainable query builder         | SQL SELECT statement (constructed but not run until evaluated) |
| `.filter()`        | Adds WHERE clauses                    | WHERE clause                                                   |
| `.exclude()`       | Adds NOT conditions                   | WHERE NOT conditions                                           |
| `.all()`           | Select all rows                       | SELECT \* FROM table                                           |
| `.get()`           | Select single row (error if multiple) | SELECT with LIMIT 1                                            |
| `.update()`        | Bulk update without loading objects   | UPDATE statement                                               |
| `.delete()`        | Bulk delete without loading objects   | DELETE statement                                               |
| `.order_by()`      | Sorts results                         | ORDER BY                                                       |
| `.values()`        | Select specific columns               | SELECT columns                                                 |


### What does `select_related` do in Django ORM?

* It **performs a SQL JOIN** and fetches related objects **in a single query**.
* Used for **single-valued relationships** like `ForeignKey` and `OneToOneField`.
* It reduces the number of queries by joining tables and retrieving related data at once.

---

#### Example:

```python
books = Book.objects.select_related('author').all()
```

This will generate a single SQL query with a JOIN between `book` and `author` tables, so when you later access `book.author.name`, no extra query is executed.

---

#### When to use `select_related`?

* When you know you’ll access related objects that are linked by a foreign key or one-to-one.
* When you want to avoid the "N+1 query problem" where accessing related objects causes many additional queries.

---

#### Important:

* `select_related` **only works for single-object relationships**.
* For many-to-many or reverse foreign key relationships, use `prefetch_related`, which executes **separate queries** but efficiently caches results.

---


### JOIN Operations 

Absolutely! Here are examples of common SQL **JOIN** queries along with their equivalent **Django ORM** and **modern SQLAlchemy (1.4+)** queries using `select()`.

---

## Setup assumption

Let's assume two models/tables:

```python
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

In SQLAlchemy, similar models:

```python
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship("Author")
```

---

# 1. **INNER JOIN**

### SQL:

```sql
SELECT book.title, author.name
FROM book
INNER JOIN author ON book.author_id = author.id;
```

### Django ORM:

```python
books = Book.objects.select_related('author').all()
for book in books:
    print(book.title, book.author.name)
```

* `select_related()` performs an SQL INNER JOIN and fetches related author in one query.

### SQLAlchemy (1.4+):

```python
from sqlalchemy import select
from sqlalchemy.orm import joinedload

stmt = select(Book).options(joinedload(Book.author))
results = session.scalars(stmt).all()
for book in results:
    print(book.title, book.author.name)
```

* `joinedload` instructs SQLAlchemy to do a JOIN and load related author objects eagerly.

---

# 2. **LEFT OUTER JOIN**

### SQL:

```sql
SELECT book.title, author.name
FROM book
LEFT JOIN author ON book.author_id = author.id;
```

### Django ORM:

```python
books = Book.objects.select_related('author').all()
# Django's select_related performs LEFT OUTER JOIN by default
for book in books:
    print(book.title, book.author.name if book.author else 'No Author')
```

> Note: Django’s `select_related` always does a LEFT OUTER JOIN.

### SQLAlchemy (1.4+):

```python
from sqlalchemy.orm import joinedload, contains_eager, aliased
from sqlalchemy import outerjoin

stmt = select(Book).options(joinedload(Book.author))
results = session.scalars(stmt).all()
for book in results:
    print(book.title, book.author.name if book.author else 'No Author')
```

> By default, `joinedload` produces a LEFT OUTER JOIN.

If you want explicit outer join in core:

```python
from sqlalchemy import outerjoin

stmt = select(Book, Author).outerjoin(Author, Book.author_id == Author.id)
results = session.execute(stmt).all()
for book, author in results:
    print(book.title, author.name if author else 'No Author')
```

---

# 3. **Filtering with JOIN**

### SQL:

```sql
SELECT book.title, author.name
FROM book
INNER JOIN author ON book.author_id = author.id
WHERE author.name = 'Alice';
```

### Django ORM:

```python
books = Book.objects.filter(author__name='Alice')
```

* This generates an INNER JOIN with filtering on author’s name.

### SQLAlchemy (1.4+):

```python
stmt = select(Book).join(Book.author).where(Author.name == 'Alice')
results = session.scalars(stmt).all()
for book in results:
    print(book.title, book.author.name)
```

---

# 4. **Many-to-Many JOIN (Bonus)**

Assume:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)
```

### SQL:

```sql
SELECT student.name, course.name
FROM student
JOIN student_course ON student.id = student_course.student_id
JOIN course ON course.id = student_course.course_id;
```

### Django ORM:

```python
courses = Course.objects.filter(students__name='Alice')
```

### SQLAlchemy (1.4+):

Assuming association table `student_course`:

```python
stmt = select(Course).join(Course.students).where(Student.name == 'Alice')
results = session.scalars(stmt).all()
for course in results:
    print(course.name)
```

---
