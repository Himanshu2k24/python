# Campus Bites - University Food Delivery Startup

A quick commerce food delivery platform tailored for busy university students, offering food and snacks delivery within campus and providing pickup options from the canteen.

## Problem Statement

University students often have only 5-minute gaps between classes, making it difficult to get food from distant canteens. They waste time waiting in long lines and for food preparation. Campus Bites solves this problem by:

1. Delivering snacks and meals directly to classrooms
2. Offering pickup notifications when food is ready at the canteen
3. Saving students' time and energy by eliminating waiting time

## Features

- **Two-Section Homepage**: Browse food items and quick snacks separately
- **User Authentication**: Login/Register to place orders
- **Cart Management**: Add items, update quantities, and remove products
- **Checkout Process**: Select delivery location or pickup option
- **Payment Options**: Multiple payment methods including cash and online payments
- **Order Tracking**: See order status and history
- **User Profile**: View past orders and account details

## Technology Stack

- **Backend**: Python with Flask framework
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Authentication**: Flask-Login

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/campus-bites.git
   cd campus-bites
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Configure the MySQL database:
   - Create a MySQL database named `campus_food_delivery`
   - Update the `.env` file with your MySQL credentials

6. Initialize the database:
   ```
   python init_db.py
   ```

7. Run the application:
   ```
   python app.py
   ```

8. Access the application in your browser:
   ```
   http://localhost:5000
   ```

## Test Account

For testing purposes, you can use the following credentials:
- Username: test_user
- Password: password123

## Future Enhancements

1. Real-time order tracking
2. Notifications system for order updates
3. Loyalty program for regular customers
4. Mobile application development
5. Integration with university meal plans
6. Delivery personnel tracking

## Business Model

- **Revenue Streams**: Delivery fee, commission from vendors, premium subscription
- **Target Market**: University students, faculty, and staff
- **Value Proposition**: Save time and energy by eliminating food wait times
- **Unique Selling Point**: Quick delivery to classrooms during short breaks

## Contributors

- [Your Name](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the LICENSE file for details.