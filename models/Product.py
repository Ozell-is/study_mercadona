import base64
import datetime
import json

from app import db
from models import Category


class Product(db.Model):
    __tablename__ = "Product"

    _id_product = db.Column(
        "id_product", db.Integer, primary_key=True, autoincrement=True, nullable=False
    )
    _libelle = db.Column("libelle", db.String(100), nullable=False)
    _description = db.Column("description", db.String(500), nullable=False)
    _price = db.Column("price", db.Float, nullable=False)
    _image = db.Column("image", db.Text,nullable=False)
    _date_debut_promotion = db.Column("date_debut_promotion", db.Date,nullable = True)
    _date_fin_promotion = db.Column("date_fin_promotion", db.Date,nullable = True)
    _pourcentage_promotion = db.Column("pourcentage_promotion", db.Integer,nullable = True)
    # relationship one-to-many
    _category_id = db.Column("category_id", db.Integer, db.ForeignKey("Category.id_category"), nullable=False)
    _category = db.relationship("Category", back_populates="_products", overlaps="category")

    def __init__(
            self,
            id_product: int,
            libelle: str,
            description: str,
            price: float,
            image: str,
            category_id: int,
            date_debut_promotion: datetime = None,
            date_fin_promotion: datetime = None,
            pourcentage_promotion: float = None,
    ):
        self._id_product = id_product
        self._libelle = libelle
        self._description = description
        self._price = price
        self._image = image
        self._category_id = category_id
        self._date_debut_promotion = date_debut_promotion
        self._date_fin_promotion = date_fin_promotion
        self._pourcentage_promotion = pourcentage_promotion

    @property
    def id_product(self):
        return self._id_product

    @id_product.setter
    def id_product(self, id_product: int):
        self._id_product = id_product

    @property
    def libelle(self):
        return self._libelle

    @libelle.setter
    def libelle(self, libelle: str):
        self._libelle = libelle

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def category_id(self):
        return self._category_id

    @category_id.setter
    def category_id(self, category_id: str):
        self._category_id = category_id

    @property
    def date_debut_promotion(self):
        return self._date_debut_promotion

    @date_debut_promotion.setter
    def date_debut_promotion(self, date_debut_promotion: str):
        self._date_debut_promotion = date_debut_promotion

    @property
    def date_fin_promotion(self):
        return self._date_fin_promotion

    @date_fin_promotion.setter
    def date_fin_promotion(self, date_fin_promotion: str):
        self._date_fin_promotion = date_fin_promotion

    @property
    def pourcentage_promotion(self):
        return self._pourcentage_promotion

    @pourcentage_promotion.setter
    def pourcentage_promotion(self, pourcentage_promotion: float):
        self._pourcentage_promotion = pourcentage_promotion

    def to_json(self):
        return self.__str__()

    def __iter__(self):
        yield from {  # yield batis un objet
            "id_product": self._id_product,
            "libelle": self._libelle,
            "description": self._description,
            "price": self._price,
            "image": self._image,
            "category_id": self._category_id,
            "date_debut_promotion": self._date_debut_promotion,
            "date_fin_promotion": self._date_fin_promotion,
            "pourcentage_promotion": self._pourcentage_promotion,
        }.items()  # renvoi clefs-valeur

    def __str__(self):
        return json.dumps(dict(self), ensure_ascii=False)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def from_json(json_dct):
        return Product (json_dct["id_product"],
                json_dct["libelle"],
                json_dct["description"],
                json_dct["price"],
                json_dct["image"],
                json_dct["category_id"],
                json_dct["date_debut_promotion"],
                json_dct["date_fin_promotion"],
                json_dct["pourcentage_promotion"],
        )