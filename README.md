
# Vendor Management System with Performance Metrics

Vendor Management System using Django and Django REST Framework. This system will handle vendor profiles, track purchase orders, and calculate vendor performance metrics.


## Tech Stack

 Django, Django Rest Framework.


## Installation

Clone this Repo.

```
git clone git@github.com:pratikaman/vendor_management_sys.git
```

Activate a virtual environment and install required packages.

```
cd vendor_management_system

pip install -r requirements.txt
```
    
Create an env file and paste following in it.
```
touch .env
```

```
DJANGO_SECRET_KEY = "YOUR SECRET KEY"
DJANGO_DEBUG = "True"
```
To generate a DJANGO_SECRET_KEY, run following in django shell

```
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```

Make migrations
```
python manage.py makemigrations
python manage.py migrate
```

Create super user to access admin page.
```
python manage.py createsuperuser
```

Run the server
```
python manage.py runserver
```

For Creating dummy Vendors run following in django shell.
```
python manage.py shell

from vendor_management.test_data import *

create_dummy_vendors()
```



## APIs


### To generate auth token via api. 
- POST `/api/api-token-auth/`
- In the body of request send as following:
	- *username*: "user-name",
	- *password*: "user-password"
- Response will be a token.
	- ex- `{"token": "994b09199c62bcf9418ad846dd0eewffc6ee4b"}`
- Send the generated token in each api request using `Authorization` HTTP header
		- ex- `Authorization: Token 994b09199c62bcf9418ad846dd0eewffc6ee4b`

*All the apis also support session authentication. 
So while accessing these API endpoints using browser we can login there using user credentials.
New user credentials can be created using django admin.*

### Vendor Profile Management

- To create a new vendor.
	- make POST request to `/api/vendors/` 
	- In the body of request send as following:
		- *name*: "Rahul",
	    - *contact_details* : "123456789",
        - *address*: "xyz",

- List all vendors.
	- make GET request to  `/api/vendors/`
- Retrieve a specific vendor's details.
	- make GET `/api/vendors/{vendor_id}/`
- Update a vendor's details.
	- make PUT request to `/api/vendors/{vendor_id}/`
	- In the body of request send details that needs to be updated as following:
		
		Example- if *address* and *contact_details* needs to be updated-
	    - *address*: "hsr layout, bangalore",
        - *contact_details*: "987654321"
        
- Delete a vendor.
	- make DELETE request to `/api/vendors/{vendor_id}/`

### Purchase Order Tracking

 - Create a purchase order.
	- make POST request to `/api/purchase_orders/`
	- In the body of request send as following:
			
		- *po_number*: 1234566,
		- *vendor*: RHL6789,
		- *order_date*: "2024-05-04T12:19:14Z",
		- *delivery_date*: "2024-08-04T12:19:14Z",
		- *items*: {
						   "fruits":  "apples"
					    },
		 - *quantity*: 5,
		 - *status*: pending,
		 - *quality_rating*: 2, **Can be null**.
		 - *issue_date*: "2024-05-04T12:19:14Z",
		 - *acknowledgment_date*: "2024-07-04T12:19:14Z" **#Can be null.**  
		

 - List all purchase orders with an option to filter by vendor.
	- make GET request to `/api/purchase_orders/`
 - Retrieve details of a specific purchase order.
	- make GET request to `/api/purchase_orders/{po_id}/`
 - Update a purchase order.
	- make PUT request to `/api/purchase_orders/{po_id}/`
	-  In the body of request send details that needs to be updated as following:

	Example- if *quantity* and *status* needs to be updated:
	
	- *quantity*: 3,
	- *status*: completed,

		    
- Delete a purchase order.
	- make DELETE request to `/api/purchase_orders/{po_id}/`

### Vendor Performance Evaluation

- Retrieve a following vendor's performance metrics.
	- On-time Delivery Rate: Percentage of orders delivered by promise date.
	- Quality Rating: Average of quality ratings given to a vendor's purchase orders.
	- Response Time: Average time taken by a vendor to acknowledge or respond to purchase orders.
	- Fulfilment Rate: Percentage of purchase orders fulfilled without issues.
	
- make GET request to `/api/vendors/{vendor_id}/performance/`

### Update Acknowledgment
- For vendors to acknowledge POs.
	- make POST request to `/api/purchase_orders/{po_id}/acknowledge/`


    
