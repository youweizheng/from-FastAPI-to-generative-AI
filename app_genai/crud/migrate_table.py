from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_business.models_business import Cuisine
from app_genai.models_vector import CuisinesContent

import json

# Database URLs - replace these with your actual database URLs
BUSINESS_DATABASE_URL = "postgresql://youwei:fromfastapi2genai@localhost:5118/business"  # business database URL
VECTOR_DATABASE_URL = "postgresql://youwei:fromfastapi2genai@localhost:5119/vector"  # vector database URL


def migrate_cuisine_to_content():
    # Create engines for both databases
    business_engine = create_engine(BUSINESS_DATABASE_URL)
    vector_engine = create_engine(VECTOR_DATABASE_URL)

    # Create sessions
    BusinessSession = sessionmaker(bind=business_engine)
    VectorSession = sessionmaker(bind=vector_engine)

    business_session = BusinessSession()
    vector_session = VectorSession()

    try:
        # Get all cuisines from business database
        cuisines = business_session.query(Cuisine).all()

        # Migrate each cuisine to cuisines_content
        for cuisine in cuisines:
            # Create metadata dictionary
            metadata = {
                "id": cuisine.id,
                "name": cuisine.name,
                "unit_price": cuisine.unit_price,
                "is_available": cuisine.is_available,
            }

            # Create content string
            contents = f"id: {cuisine.id} - name: {cuisine.name} - description: {cuisine.description} - unit_price: {cuisine.unit_price} - is_available: {cuisine.is_available}"

            # Create new CuisinesContent entry
            cuisine_content = CuisinesContent(
                metadata_value=json.dumps(metadata), contents=contents
            )

            # Add to vector database
            vector_session.add(cuisine_content)

        # Commit the changes
        vector_session.commit()
        print("Migration completed successfully!")

    except Exception as e:
        print(f"An error occurred during migration: {str(e)}")
        vector_session.rollback()
    finally:
        business_session.close()
        vector_session.close()


if __name__ == "__main__":
    migrate_cuisine_to_content()
