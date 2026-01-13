# FastAPI Product CRUD 시험

## 📌 시험 방법

### 시험 목표
FastAPI를 사용한 이커머스 상품 CRUD(Create, Read, Update, Delete) 기능 완전 구현

### 시험 시간
약 4시간

### 진행 절차
1. **환경 설정** (10분)
2. **CRUD 계층 구현** (60분)
3. **Service 계층 구현** (60분)
4. **API 엔드포인트 구현** (60분)
5. **테스트 작성 및 검증** (30분)

---

## 🎯 해결해야 할 문제 (총 18개)

### 1️⃣ CRUD 계층 (5개 메서드) - `crud/product.py`

| # | 메서드 | 기능 | 난이도 |
|---|--------|------|--------|
| 1 | `get_all_products_public()` | 공개 상품 조회 + 검색 + 페이지네이션 | ⭐⭐ |
| 2 | `get_products_for_vendor()` | 판매자별 상품 조회 | ⭐⭐ |
| 3 | `sort_product_by_price()` | 가격순 상품 정렬 | ⭐ |
| 4 | `get_active_products()` | 활성 상품 조회 (ID로) | ⭐ |
| 5 | `get_single_product_by_id()` | 상세 정보 포함 조회 (N+1 해결) | ⭐⭐⭐ |

**핵심 요구사항:**
- SQLAlchemy ORM 쿼리 사용
- `get_single_product_by_id()`는 joinedload 사용하여 N+1 문제 해결
- 페이지네이션 구현 (skip, limit)
- 검색 필터 지원

---

### 2️⃣ Service 계층 (6개 메서드) - `services/product_service.py`

| # | 메서드 | 기능 | 난이도 |
|---|--------|------|--------|
| 1 | `get_product_categories()` | 모든 카테고리 조회 | ⭐ |
| 2 | `create_product()` | 상품 생성 (SKU, 이미지, 카테고리) | ⭐⭐⭐ |
| 3 | `get_products_customer()` | 고객용 상품 조회 | ⭐ |
| 4 | `get_products_vendor()` | 판매자 상품 조회 | ⭐ |
| 5 | `update_product()` | 상품 수정 (소유권 확인) | ⭐⭐ |
| 6 | `delete_product()` | 상품 삭제 (소유권 확인) | ⭐⭐ |

**핵심 요구사항:**
- async/await 사용
- CRUD 계층 메서드 호출
- 비즈니스 로직 구현 (SKU 자동 생성, 카테고리 생성)
- 에러 처리 (MissingResource, InvalidRequest)
- 소유권 확인 (수정/삭제 시)

---

### 3️⃣ API 엔드포인트 (7개) - `api/endpoints/product.py`

| HTTP | 경로 | 설명 | 난이도 |
|------|------|------|--------|
| POST | `/products` | 상품 생성 | ⭐⭐ |
| GET | `/products` | 공개 상품 조회 (검색+페이징) | ⭐⭐ |
| GET | `/products/me` | 판매자 상품 조회 | ⭐⭐ |
| GET | `/products/price` | 가격순 정렬 | ⭐ |
| GET | `/products/{id}` | 단일 상품 조회 | ⭐ |
| PUT | `/products/{id}` | 상품 수정 | ⭐⭐ |
| DELETE | `/products/{id}` | 상품 삭제 | ⭐⭐ |

**핵심 요구사항:**
- FastAPI 라우터 사용
- 의존성 주입 (Depends)
- 올바른 HTTP 상태 코드 (201, 200, 204, 404, 403)
- response_model 지정
- 인증 필수

---

## 🔧 기본 개발 흐름

```
HTTP 요청 
  ↓
API 엔드포인트 (api/endpoints/product.py)
  ↓
Service 비즈니스 로직 (services/product_service.py)
  ↓
CRUD 데이터베이스 작업 (crud/product.py)
  ↓
데이터베이스 (PostgreSQL)
```

---

## 🚀 빠른 시작

```bash
# 1. 의존성 설치
poetry install

# 2. 데이터베이스 마이그레이션
poetry run alembic upgrade head

# 3. 서버 실행
poetry run uvicorn main:app --reload

# 4. 테스트 실행
poetry run pytest tests/endpoints/test_product.py -v

# 5. API 문서 확인
# http://localhost:8000/docs (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```

---

## 📚 참고 파일 구조

```
models/product.py           # Product, ProductCategory, ProductImage 모델
schemas/product.py          # ProductCreate, ProductUpdate, ProductReturn 스키마
crud/product.py             # ✅ 구현 필요
services/product_service.py # ✅ 구현 필요
api/endpoints/product.py    # ✅ 구현 필요
tests/endpoints/test_product.py # 테스트 케이스 참고
```

---

## ✅ 평가 기준

| 항목 | 배점 | 요구사항 |
|------|------|---------|
| CRUD 계층 | 25점 | 5개 메서드 모두 정상 작동 |
| Service 계층 | 30점 | 6개 메서드 모두 정상 작동 + 비즈니스 로직 |
| API 엔드포인트 | 30점 | 7개 엔드포인트 모두 정상 작동 |
| 테스트 | 15점 | 테스트 케이스 통과율 80% 이상 |
| **합계** | **100점** | - |

---

## 💡 주의사항

1. **N+1 문제**: `get_single_product_by_id()`에서 반드시 joinedload 사용
2. **소유권 확인**: 수정/삭제 시 판매자 검증 필수
3. **에러 처리**: 적절한 예외 발생 (404, 403, 400)
4. **페이지네이션**: skip, limit 파라미터 사용
5. **비동기**: Service 계층은 모두 async/await 사용

