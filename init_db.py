from app import app, db, Category, Product, User
from werkzeug.security import generate_password_hash
import random

# Create sample data for the application
def create_sample_data():
    with app.app_context():
        # Create categories
        food_category = Category(name='Food')
        snacks_category = Category(name='Snacks')
        
        db.session.add(food_category)
        db.session.add(snacks_category)
        db.session.commit()
        
        # Create sample food items
        food_items = [
            {
                'name': 'Chicken Biryani',
                'description': 'Flavorful rice dish with chicken, aromatic spices, and herbs.',
                'price': 8.99,
                'image_url': 'https://images.unsplash.com/photo-1589302168068-964664d93dc0?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Veg Fried Rice',
                'description': 'Rice stir-fried with mixed vegetables and soy sauce.',
                'price': 5.99,
                'image_url': 'https://images.unsplash.com/photo-1603133872878-684f208fb84b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Paneer Butter Masala',
                'description': 'Cottage cheese cubes in rich tomato and butter gravy.',
                'price': 7.49,
                'image_url': 'https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Chicken Burger',
                'description': 'Juicy chicken patty with lettuce, tomato, and special sauce.',
                'price': 6.99,
                'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Vegetable Sandwich',
                'description': 'Fresh vegetables and cheese between whole wheat bread.',
                'price': 4.49,
                'image_url': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Pasta Alfredo',
                'description': 'Creamy pasta with garlic, parmesan cheese, and herbs.',
                'price': 7.99,
                'image_url': 'https://images.unsplash.com/photo-1645112411341-6c4fd023714a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Pizza Margherita',
                'description': 'Classic pizza with tomato sauce, mozzarella, and basil.',
                'price': 9.99,
                'image_url': 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            },
            {
                'name': 'Veg Noodles',
                'description': 'Stir-fried noodles with mixed vegetables and soy sauce.',
                'price': 5.49,
                'image_url': 'https://images.unsplash.com/photo-1585032226651-759b368d7246?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': food_category.id
            }
        ]
        
        # Create sample snack items
        snack_items = [
            {
                'name': 'French Fries',
                'description': 'Crispy golden fries served with ketchup.',
                'price': 2.99,
                'image_url': 'https://images.unsplash.com/photo-1630384060421-cb20d0e0649d?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Samosa',
                'description': 'Fried pastry with savory potato filling.',
                'price': 1.49,
                'image_url': 'https://images.unsplash.com/photo-1601050690597-df0568f70950?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Chocolate Muffin',
                'description': 'Moist chocolate muffin with chocolate chips.',
                'price': 2.49,
                'image_url': 'https://images.unsplash.com/photo-1607958996333-41aef7caefaa?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Fruit Parfait',
                'description': 'Yogurt layered with fresh fruits and granola.',
                'price': 3.99,
                'image_url': 'https://images.unsplash.com/photo-1488477181946-6428a0291777?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Potato Chips',
                'description': 'Crunchy potato chips with various flavors.',
                'price': 1.29,
                'image_url': 'https://images.unsplash.com/photo-1566478989037-eec170784d0b?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Cheese Sandwich',
                'description': 'Grilled sandwich with melted cheese.',
                'price': 3.49,
                'image_url': 'https://images.unsplash.com/photo-1528736235302-52922df5c122?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Brownie',
                'description': 'Rich chocolate brownie with a fudgy center.',
                'price': 2.79,
                'image_url': 'https://images.unsplash.com/photo-1606313564200-e75d5e30476c?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            },
            {
                'name': 'Veg Spring Roll',
                'description': 'Crispy rolls filled with vegetables and served with dipping sauce.',
                'price': 3.99,
                'image_url': 'https://images.unsplash.com/photo-1626126525134-fbbc0db37b8a?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60',
                'category_id': snacks_category.id
            }
        ]
        
        # Add food items to database
        for food_item in food_items:
            product = Product(
                name=food_item['name'],
                description=food_item['description'],
                price=food_item['price'],
                image_url=food_item['image_url'],
                category_id=food_item['category_id'],
                is_available=True
            )
            db.session.add(product)
        
        # Add snack items to database
        for snack_item in snack_items:
            product = Product(
                name=snack_item['name'],
                description=snack_item['description'],
                price=snack_item['price'],
                image_url=snack_item['image_url'],
                category_id=snack_item['category_id'],
                is_available=True
            )
            db.session.add(product)
        
        # Create test user
        test_user = User(
            username='test_user',
            email='test@example.com'
        )
        test_user.password_hash = generate_password_hash('password123')
        
        db.session.add(test_user)
        db.session.commit()
        
        print('Sample data created successfully!')

if __name__ == '__main__':
    # Create all tables
    with app.app_context():
        db.create_all()
    
    # Create sample data
    create_sample_data()