from arq import ArqRedis

from core.errors import InvalidRequest, MissingResources
from crud import (
    CRUDAuthUser,
    CRUDProduct,
    CRUDProductCategory,
    CRUDProductImage,
    CRUDProductReview,
)
from models import AuthUser, ProductCategory
from schemas import (
    ProductCreate,
    ProductImageUpdate,
    ProductReviewCreate,
    ProductReviewUpdate,
    ProductUpdate,
    ProductImageCreate,
)
from utils.generate_sku import generate_random_sku


class ProductService:

    def __init__(
        self,
        crud_auth_user: CRUDAuthUser,
        crud_product: CRUDProduct,
        crud_product_category: CRUDProductCategory,
        crud_product_image: CRUDProductImage,
        crud_product_review: CRUDProductReview,
        queue_connection: ArqRedis,
    ):
        self.crud_auth_user = crud_auth_user
        self.crud_product = crud_product
        self.crud_product_category = crud_product_category
        self.crud_product_image = crud_product_image
        self.crud_product_review = crud_product_review
        self.queue_connection = queue_connection

    async def get_product_categories(self):
        """Return all product categories.

        TODO: Implement this method to return categories using
        `self.crud_product_category.get_multi`.
        """
        raise NotImplementedError("get_product_categories not implemented")

    async def create_product(
        self,
        data_obj: ProductCreate,
        current_user: AuthUser,
    ):
        """Create a product (simple CRUD stub).

        TODO: Implement full creation logic: create/find category,
        generate SKU, create product and product images.

        Expected to return the created product object.
        """
        raise NotImplementedError("create_product not implemented")

    async def get_products_customer(
        self,
        search: str,
        skip: int,
        limit: int,
    ):
        """Return public products (paged/search).

        TODO: Implement by calling `self.crud_product.get_all_products_public`.
        """
        raise NotImplementedError("get_products_customer not implemented")

    async def get_products_vendor(
        self,
        search: str,
        skip: int,
        limit: int,
        vendor_id: int,
    ):
        """Return products for a vendor.

        TODO: Implement by calling `self.crud_product.get_products_for_vendor`.
        """
        raise NotImplementedError("get_products_vendor not implemented")

    async def sort_product_by_price(
        self,
        skip: int,
        limit: int,
    ):
        """Return products sorted by price.

        TODO: Implement using `self.crud_product.sort_product_by_price`.
        """
        raise NotImplementedError("sort_product_by_price not implemented")

    async def get_one_product(
        self,
        product_id: int,
    ):
        """Return single active product by id.

        TODO: Implement using `self.crud_product.get_active_products`.
        """
        raise NotImplementedError("get_one_product not implemented")

    async def update_product(
        self,
        product_id: int,
        data_obj: ProductUpdate,
        vendor_id: int,
    ):
        """Update a product (simple stub).

        TODO: Implement product ownership check and update via
        `self.crud_product.update`.
        """
        raise NotImplementedError("update_product not implemented")

    async def update_product_image(
        self,
        product_image_id: int,
        data_obj: ProductImageUpdate,
        vendor_id: int,
    ):
        """Update a product image (stub).

        TODO: Implement lookup and update using `self.crud_product_image.update`.
        """
        raise NotImplementedError("update_product_image not implemented")

    async def delete_product(
        self,
        product_id: int,
        vendor_id: int,
    ):
        """Delete a product (stub).

        TODO: Implement deletion after ownership check using
        `self.crud_product.delete`.
        """
        raise NotImplementedError("delete_product not implemented")

    async def create_product_review(
        self,
        data_obj: ProductReviewCreate,
    ):
        """Create a product review (stub).

        TODO: Validate product exists and create review using
        `self.crud_product_review.create`.
        """
        raise NotImplementedError("create_product_review not implemented")

    async def update_product_review(
        self,
        review_id: int,
        data_obj: ProductReviewUpdate,
    ):
        """Update a product review (stub).

        TODO: Lookup and update the review via
        `self.crud_product_review.update`.
        """
        raise NotImplementedError("update_product_review not implemented")
