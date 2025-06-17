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
