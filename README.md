# vendor Sweets

## Dependencies
1. Python 3+
2. pyrhon flask `pip install flask`
3. sqlAlchemy "     "
4. React frontend or postman 


## initilizing the project if migrations and db does not exist
- open the termial in project root directory
- run `flask db init` to initialize the project 
- run `flask db migrate -m "Initial migration"`
- commit changes  `flask db upgrade`

## seed to database
- run `python seed.py` on the terminal

## starting the routes
- run `python app.py`

## Files and their functions

### models.py
- creates the models to add the data to the database
- Tables include Sweets + Vendors + VendorSweets

### routes.py
- creates the routes for database communication with the user
- GET /vendors `gets all the current present vendors`
- GET /vendors<id> `gets a vendor by id and lists all the current sweets of the vendor`
 returns `error': 'Vendor not found'}), 404` when a vendor is not present
- GET /sweets `gets a list of all current availabe sweets`
- GET /sweets<id> `gets an existing sweet by id`
- POST /vendor_ sweets  `adds an existing sweet to a vendor` 
 returns `not found,404`if vendor or sweet doesn't exist
- DELETE/ vendor_sweets `deletes an existing vendor sweets`

### seed.py
- adds data to the database for testing purposes

### app.py
- starting point of the project
- connects to the database
- calls the routes for communication
