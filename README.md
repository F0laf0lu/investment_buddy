# Investment Buddy
Investment Buddy is an AI-powered financial advisor that turns Stanbic IBTC from just a place to store money into a 
partner that actively grows customer wealth. This smart system watches customer spending, finds extra money they can 
invest, and suggests the best Stanbic IBTC investment products to help them reach their financial goals.


## What Investment Buddy Does
Investment Buddy works like having a financial expert as your best friend. It connects to customer bank accounts, 
analyzes their money habits, and identifies opportunities to grow their wealth. The system learns each customer's 
spending patterns, understands their financial situation, and recommends investments that match their comfort level 
and goals.

### Key capabilities include:
* Smart money tracking - Automatically categorizes spending and finds surplus funds available for investment
* Personal risk assessment - Determines what investment types suit each customer based on their behavior and preferences  
* Goal-based planning - Helps customers set and achieve specific financial targets like buying a house or planning retirement
* 24/7 chat support - Answers questions about investments, market conditions, and financial planning anytime
* Investment simulations - Shows customers what could happen with different investment choices before they commit real money
* Automatic investing - Can execute approved investment strategies without constant customer input
* Simple dashboards - Presents complex financial information in easy-to-understand visuals


## Prime Features
As a user I can:
* View a list of investments available from Stanbic IBTC, ordered by how relevant they are to me
* Set my risk appetite which changes investments recommended to me
* Talk to the investment buddy and get recommendations based on my profile and risk appetite
* Get periodic nudges (perhaps when my salary comes in) to set aside money for an investment
* Through the investment buddy I can set up an investment plan with a target goal.
* The plan can work automatically to maje deposits from my account at predetermined intervals.
* Can view a dashboard displaying portfolio detailing total value, withdrawals and deposits made.

# Usage
To use this application in your own environment, use virtualenv and pip:

## If no virtualenv already exist:
On macOS/Linux
```
$ python3 -m venv venv
$ source venv/bin/activate
```

On Windows
```
$ python -m venv venv
$ venv\Scripts\activate
```

## Setting dependencies
```
$ pip install -r requirements.txt
```

## Run development server
```
$ python manage.py runserver
```

## Makefile shortcuts
We've added a Makefile to simplify common development tasks. Make sure you're in the project root where the Makefile is
located. Ensure you have the correct database credentials configured in your `.env` file, and reflect that in the 
`db_init.sql`.

### Set up the environment
```
make setup
```

### Set up the database
```
make resetdb
```

### Applying database migrations
```
make migrate
```

### Run django Development server
```
make runserver
```
