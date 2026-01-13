from typing import List, Union
from fastapi import Depends
from sqlalchemy import desc

import sqlalchemy
import sqlalchemy.orm

from core.db import get_db
from core.errors import MissingResources
from crud.base import CRUDBase
from models import Product, ProductCategory, ProductImage, ProductReview
from schemas import (
    ProductCreate,
    ProductUpdate,
    ProductCategoryCreate,
    ProductImageCreate,
    ProductReviewCreate,
    ProductReviewUpdate,
)

class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):

    def get_all_products_public(
        self, search: str | None, skip=0, limit=10
    ) -> Union[List[Product], None]:
        """Return public products (search + pagination).

        TODO: Implement actual DB query here. For the exercise,
        replace this stub with logic that queries `self.model` and
        applies filters for `product_status`, `search`, pagination
        and eager-loads relations as needed.

        Expected return type: list[Product] | None
        """
        raise NotImplementedError("get_all_products_public not implemented")

    def get_products_for_vendor(
        self, vendor_id: int, search: str | None, skip=0, limit=10
    ) -> Union[List[Product], None]:
        """Return vendor products (search + pagination).

        TODO: Implement actual DB query here. Replace this stub
        with logic that filters by `vendor_id`, `product_status`, and
        applies search/pagination.
        """
        raise NotImplementedError("get_products_for_vendor not implemented")

    def sort_product_by_price(self, skip: int = 0, limit: int = 20) -> List[Product]:
        """Return products ordered by price.

        TODO: Implement ordering by price with pagination.
        """
        raise NotImplementedError("sort_product_by_price not implemented")

    def get_active_products(self, id: int) -> Product:
        """Return a single active product by id or raise MissingResources.

        TODO: Implement actual lookup and active-status check.
        """
        raise NotImplementedError("get_active_products not implemented")

    def get_single_product_by_id(self, id: int):
        """Return single product with relations preloaded.

        TODO: Implement actual query using joinedload for images and
        category, returning the product or None.
        """
        raise NotImplementedError("get_single_product_by_id not implemented")


class CRUDProductReview(
    CRUDBase[ProductReview, ProductReviewCreate, ProductReviewUpdate]
):
    pass


class CRUDProductImage(CRUDBase[ProductImage, ProductImageCreate, ProductImageCreate]):
    pass


class CRUDProductCategory(
    CRUDBase[ProductCategory, ProductCategoryCreate, ProductCategoryCreate]
):
    def get_by_category_name(self, category_name):
        query = (
            self._db.query(self.model)
            .filter(self.model.category_name == category_name)
            .first()
        )
        return query if query else None


crud_product_image = CRUDProductImage(db=get_db(), model=ProductImage)
crud_product_category = CRUDProductCategory(db=get_db(), model=ProductCategory)


def get_crud_product(db=Depends(get_db)) -> CRUDProduct:
    return CRUDProduct(db=db, model=Product)


def get_crud_product_image(db=Depends(get_db)) -> CRUDProductImage:
    return CRUDProductImage(db=db, model=ProductImage)


def get_crud_product_category(db=Depends(get_db)) -> CRUDProductCategory:
    return CRUDProductCategory(db=db, model=ProductCategory)


def get_crud_product_review(db=Depends(get_db)) -> CRUDProductReview:
    return CRUDProductReview(db=db, model=ProductReview)