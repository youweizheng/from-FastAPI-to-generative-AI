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
    
    # Create a session
    db = BusinessSessionMaker()
    
    try:
        # Insert 10 rows of fake data
        for dish_name in chinese_dishes:
            # Generate a more detailed description using Faker
            description = f"{dish_name} - {fake.sentence(nb_words=6, variable_nb_words=True)}. {fake.sentence(nb_words=8, variable_nb_words=True)}"
            
            # Generate a more realistic price (in cents)
            base_price = random.randint(800, 2000)  # $8.00 to $20.00
            unit_price = base_price + random.randint(-200, 200)  # Add some variation
            
            dish = Cuisine(
                name=dish_name,
                description=description,
                unit_price=unit_price,
                is_available=fake.boolean(chance_of_getting_true=80)  # 80% chance of being available
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
