# FastAPI Product CRUD Exam

## 📌 Exam Instructions

### Exam Goal
Complete implementation of E-commerce Product CRUD (Create, Read, Update, Delete) functionality using FastAPI

### Exam Duration
Approximately 4 hours

### Procedure
1. **Environment Setup** (10 minutes)
2. **CRUD Layer Implementation** (60 minutes)
3. **Service Layer Implementation** (60 minutes)
4. **API Endpoint Implementation** (60 minutes)
5. **Test Writing and Validation** (30 minutes)

---

## 🎯 Problems to Solve (Total 18)

### 1️⃣ CRUD Layer (5 Methods) - `crud/product.py`

| # | Method | Functionality | Difficulty |
|---|--------|---------------|------------|
| 1 | `get_all_products_public()` | Retrieve public products + search + pagination | ⭐⭐ |
| 2 | `get_products_for_vendor()` | Retrieve products by vendor | ⭐⭐ |
| 3 | `sort_product_by_price()` | Sort products by price | ⭐ |
| 4 | `get_active_products()` | Retrieve active products (by ID) | ⭐ |
| 5 | `get_single_product_by_id()` | Retrieve detailed product info (N+1 solved) | ⭐⭐⭐ |

**Key Requirements:**
- Use SQLAlchemy ORM queries
- `get_single_product_by_id()` must use joinedload to solve N+1 problem
- Implement pagination (skip, limit)
- Support search filters

---

### 2️⃣ Service Layer (6 Methods) - `services/product_service.py`

| # | Method | Functionality | Difficulty |
|---|--------|---------------|------------|
| 1 | `get_product_categories()` | Retrieve all categories | ⭐ |
| 2 | `create_product()` | Create product (SKU, images, categories) | ⭐⭐⭐ |
| 3 | `get_products_customer()` | Retrieve products for customers | ⭐ |
| 4 | `get_products_vendor()` | Retrieve vendor products | ⭐ |
| 5 | `update_product()` | Update product (verify ownership) | ⭐⭐ |
| 6 | `delete_product()` | Delete product (verify ownership) | ⭐⭐ |

**Key Requirements:**
- Use async/await
- Call CRUD layer methods
- Implement business logic (auto SKU generation, category creation)
- Handle errors (MissingResource, InvalidRequest)
- Verify ownership (for update/delete)

---

### 3️⃣ API Endpoints (7 Total) - `api/endpoints/product.py`

| HTTP | Path | Description | Difficulty |
|------|------|-------------|------------|
| POST | `/products` | Create product | ⭐⭐ |
| GET | `/products` | Retrieve public products (search+pagination) | ⭐⭐ |
| GET | `/products/me` | Retrieve vendor products | ⭐⭐ |
| GET | `/products/price` | Sort by price | ⭐ |
| GET | `/products/{id}` | Retrieve single product | ⭐ |
| PUT | `/products/{id}` | Update product | ⭐⭐ |
| DELETE | `/products/{id}` | Delete product | ⭐⭐ |

**Key Requirements:**
- Use FastAPI router
- Dependency injection (Depends)
- Correct HTTP status codes (201, 200, 204, 404, 403)
- Specify response_model
- Authentication required

---

## 🔧 Development Flow

```
HTTP Request 
  ↓
API Endpoints (api/endpoints/product.py)
  ↓
Service Business Logic (services/product_service.py)
  ↓
CRUD Database Operations (crud/product.py)
  ↓
Database (PostgreSQL)
```

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
poetry install

# 2. Run database migrations
poetry run alembic upgrade head

# 3. Start the server
poetry run uvicorn main:app --reload

# 4. Run tests
poetry run pytest tests/endpoints/test_product.py -v

# 5. Check API documentation
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```

---

## 📚 Reference File Structure

```
models/product.py           # Product, ProductCategory, ProductImage models
schemas/product.py          # ProductCreate, ProductUpdate, ProductReturn schemas
crud/product.py             # ✅ Implementation needed
services/product_service.py # ✅ Implementation needed
api/endpoints/product.py    # ✅ Implementation needed
tests/endpoints/test_product.py # Reference test cases
```

---

## ✅ Evaluation Criteria

| Category | Points | Requirements |
|----------|--------|--------------|
| CRUD Layer | 25 | All 5 methods working correctly |
| Service Layer | 30 | All 6 methods working correctly + business logic |
| API Endpoints | 30 | All 7 endpoints working correctly |
| Tests | 15 | Test case pass rate 80% or higher |
| **Total** | **100** | - |

---

## 💡 Important Notes

1. **N+1 Problem**: Must use joinedload in `get_single_product_by_id()`
2. **Ownership Verification**: Vendor verification required for update/delete
3. **Error Handling**: Raise appropriate exceptions (404, 403, 400)
4. **Pagination**: Use skip and limit parameters
5. **Async**: Service layer must use async/await
