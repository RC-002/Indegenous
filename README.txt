
- I have an application as per the requirements provided.
- The application is responsive across all screen sizes.

- Tech Stack:
	- HTML
	- CSS
	- Bootstrap
	- JavaScript
	- Django
	- SQLITE

- Development Summary
	- The project is named Indegenous. An app called details is created and contains 
		- the view.py
		- urls.py 
 		- models.py files
	- The database chosen was SQLite.
	- The table name is Info and it contains
		- id (numeric/int) auto-increment, primary key
		- title (varchar2(100))
		- details - models.textField
	- The db constraints were not elaborated and I have tried to keep it simple. I wanted to make another table for counties and have a foreign key in the details table. This will allow me to specify a list which the user can select for the details.

- Workflow:
	- 4 entires (given in the internship test specification0 are added in the database
	- The buttons in the home page are dynamically displayed based on the entries in the db. The text in the button is the title of the entry
	- When the user clicks on the button, a js function is invoked with the title and details of the entry as parameters.
	- This is then displayed in a static div in the index.html file

