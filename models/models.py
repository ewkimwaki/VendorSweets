from app import db

class Sweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define relationship to VendorSweet with a different backref name
    sweet_vendor_sweets = db.relationship('VendorSweet', backref='sweet', cascade='all, delete-orphan')

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    # Define relationship to VendorSweet
    vendor_sweets = db.relationship('VendorSweet', backref='vendor', cascade='all, delete-orphan')

class VendorSweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
