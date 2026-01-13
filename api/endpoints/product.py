from fastapi import Depends, APIRouter, Query, status
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from core.db import get_db
from schemas import (
    ProductCreate,
    ProductUpdate,
    ProductReturn,
    ProductsReturn,
    ProductUpdateReturn,
    ProductImageUpdate,
    ProductImageUpdateReturn,
    ProductReviewCreate,
    ProductReviewReturn,
    ProductReviewUpdate,
    ProductReviewUpdateReturn,
)

router = APIRouter(prefix="/products", tags=["Product"])


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ProductReturn)
def create_product(data_obj: ProductCreate, db: Session = Depends(get_db)):
    # TODO: Implement create_product in ProductService
    pass


@router.get("", response_model=list[ProductsReturn])
def get_products_customer(
    search: str | None = Query(default="", max_length=20, description="Search products with name or category"),
    skip: int = Query(default=0),
    limit: int = Query(default=20),
    db: Session = Depends(get_db),
):
    # TODO: Implement get_products_customer in ProductService
    pass


@router.get("/me", response_model=list[ProductReturn])
def get_products_vendor(
    search: str | None = Query(default="", max_length=20, description="Search products with name or category"),
    skip: int = Query(default=0),
    limit: int = Query(default=10),
    db: Session = Depends(get_db),
):
    # TODO: Implement get_products_vendor in ProductService
    pass


@router.get("/price", response_model=list[ProductReturn])
def sort_product_by_price(
    skip: int = Query(default=0),
    limit: int = Query(default=20),
    db: Session = Depends(get_db),
):
    # TODO: Implement sort_product_by_price in ProductService
    pass


@router.get("/{id}", response_model=ProductReturn)
def get_one_product(id: int, db: Session = Depends(get_db)):
    # TODO: Implement get_one_product in ProductService
    pass


@router.put("/{id}", response_model=ProductUpdateReturn)
def update_product(id: int, data_obj: ProductUpdate, db: Session = Depends(get_db)):
    # TODO: Implement update_product in ProductService
    pass


@router.put("/image/{product_image_id}", response_model=ProductImageUpdateReturn)
def update_product_image(product_image_id: int, data_obj: ProductImageUpdate, db: Session = Depends(get_db)):
    # TODO: Implement update_product_image in ProductService
    pass


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db)):
    # TODO: Implement delete_product in ProductService
    pass


@router.post("/add-review", status_code=status.HTTP_201_CREATED, response_model=ProductReviewReturn)
def create_product_review(data_obj: ProductReviewCreate, db: Session = Depends(get_db)):
    # TODO: Implement create_product_review in ProductService
    pass


@router.put("/edit-review/{review_id}", status_code=status.HTTP_201_CREATED, response_model=ProductReviewUpdateReturn)
def update_product_review(review_id: int, data_obj: ProductReviewUpdate, db: Session = Depends(get_db)):
    # TODO: Implement update_product_review in ProductService
    pass
