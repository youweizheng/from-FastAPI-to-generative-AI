from sqlalchemy.orm import Session

from app_business.models_business import Cuisine
from app_business.database import BusinessSessionMaker

db_session_global = BusinessSessionMaker()

def query_all_cuisines_from_db():
    """Get all cuisines from the database as plain text."""
    cuisines = db_session_global.query(Cuisine).all()

    return cuisines


def query_all_cuisines(db_session: Session) -> str:
    """Get all cuisines from the database as plain text."""
    cuisines = db_session.query(Cuisine).all()
    return "\n".join(
        [
            f"ID: {c.id}, Name: {c.name}, Description: {c.description}, Price: {c.unit_price}, Available: {c.is_available}"
            for c in cuisines
        ]
    )


if __name__ == "__main__":
    # Create a new database session
    db_session = BusinessSessionMaker()

    try:
        # Fetch all cuisines
        cuisines_text = query_all_cuisines(db_session)
        print(cuisines_text)
    finally:
        # Close the session
        db_session.close()
