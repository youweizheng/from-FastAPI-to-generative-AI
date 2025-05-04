from sqlalchemy.orm import sessionmaker
from models_business import Base, Cuisine
from faker import Faker
import random
from database import business_engine, BusinessSessionMaker

# Create tables
Base.metadata.create_all(bind=business_engine)

# Initialize Faker
fake = Faker()

def create_fake_chinese_cuisine():
    # List of common Chinese dishes
    chinese_dishes = [
        "Kung Pao Chicken",
        "Sweet and Sour Pork",
        "Mapo Tofu",
        "Peking Duck",
        "Dim Sum",
        "Hot Pot",
        "Wonton Soup",
        "Spring Rolls",
        "Chow Mein",
        "Dumplings"
    ]
    
    # List of descriptions for Chinese dishes
    descriptions = [
        "A spicy, stir-fried dish with chicken, peanuts, vegetables, and chili peppers",
        "Crispy pork pieces in a tangy sweet and sour sauce",
        "Spicy tofu dish with minced meat in a chili sauce",
        "Crispy roasted duck served with thin pancakes and hoisin sauce",
        "Assorted small bite-sized portions of food served in small steamer baskets",
        "Interactive dining experience with a simmering pot of broth",
        "Clear broth with wonton dumplings and vegetables",
        "Crispy fried rolls filled with vegetables and meat",
        "Stir-fried noodles with vegetables and meat",
        "Steamed or fried dough pockets filled with meat or vegetables"
    ]
    
    # Create a session
    db = BusinessSessionMaker()
    
    try:
        # Insert 10 rows of fake data
        for i in range(10):
            dish = Cuisine(
                name=chinese_dishes[i],
                description=descriptions[i],
                unit_price=random.randint(100, 500),  # Random price between 100 and 500
                is_available=random.choice([True, False])
            )
            db.add(dish)
        
        # Commit the changes
        db.commit()
        print("Successfully inserted 10 rows of Chinese cuisine data!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_fake_chinese_cuisine()
