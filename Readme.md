# Steps to run inventory (Dev mode):


####This project is about inventory as following

Users

	- Admin: 
	
		- can login
		- can logout

		- can create users/manager
		- can update users info
		- can delete users
		- can list all users

		- can create batch and assign a manager
		- can delete batches
		- can update batches
		- can list all batches

		- can create items
		- can delete items
		- can update items
		- can list batches
				

	- Managers:
	
		- can login
		- can logout

		- can see own account information

		- can list own batches

		- can create items against his/her batch
		- can delete items against his/her batch
		- can list items against his/her batch
		- can update items against his/her batch



## 1. Dependencies:

To be able to run **Inventory** you have to meet following dependencies:

- python3 and pip3

## 2. Install App Requirements:

- Switch to project root directory.
- run `$ pip3 install -r requirements.txt`

## 3. Start Postgres DB:

- setup postgers on aws rdn or somewhere and put the host, database name etc in project settings.py to integrae

## 4. Make and apply migrations:
 
- Switch to project root directory.
- Run `$ bash migrate.sh`


## 5. Start Application Server

- `python3 manage.py runserver`

inventory REST server is now up on `localhost:8000`
