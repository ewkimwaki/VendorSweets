from app import app, db
from models.models import Sweet, Vendor, VendorSweet

def seed_database():
    with app.app_context():
    # Create sample sweets
        sweet1 = Sweet(name="Chocolate Chip Cookie")
        sweet2 = Sweet(name="Brownie")
        sweet3 = Sweet(name="M&Ms Cookie")

        # Create sample vendors
        vendor1 = Vendor(name="Insomnia Cookies")
        vendor2 = Vendor(name="Cookies Cream")

        # Add sample sweets and vendors to the session
        db.session.add_all([sweet1, sweet2, sweet3, vendor1, vendor2])
        db.session.commit()

        # Create sample vendor sweets
        vs1 = VendorSweet(price=45, sweet=sweet1, vendor=vendor1)
        vs2 = VendorSweet(price=50, sweet=sweet2, vendor=vendor1)
        vs3 = VendorSweet(price=55, sweet=sweet3, vendor=vendor2)

        # Add sample vendor sweets to the session
        db.session.add_all([vs1, vs2, vs3])
        db.session.commit()

        print("Database seeded to successfully.")

if __name__ == '__main__':
    seed_database()