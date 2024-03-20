# GuestBook
 
GuestBook is a simple scrapbook. It is written with Clean Architecture and strictly adheres to OOP principles. Pep8 standards were used throughout the project.

It uses SQLite, which is very lightweight, as a database. If there is no database at the beginning, it creates it and creates the tables.

Some of the APIs (get/entries etc.) use pagination.

There is also a sample test in the tests folder. These tests use mock service and repository. Contains a sample approach to mock strategy.

#### To run project inside backend folder;
````
uvicorn api.main:app --reload
````