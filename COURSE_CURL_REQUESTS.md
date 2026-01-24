# Courses API - cURL Request Documentation

## Base URL
```
http://localhost:8000/api/courses
```

---

## 1. Create Course

**Endpoint:** `POST /api/courses/`

**Description:** Create a new course

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "title": "Introduction to Python",
  "course_code": "CS101",
  "degree_programs": [
    {'degree_program': 'CST', 'semester': 1},
    {'degree_program': 'IIT', 'semester': 2}
    ]
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Introduction to Python",
    "course_code": "CS101",
    "degree_programs": [
                        {'degree_program': 'CST', 'semester': 1},
                        {'degree_program': 'IIT', 'semester': 2}
                        ]
  }'
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Course created successfully",
  "data": {
    "id": 1,
    "title": "Introduction to Python",
    "course_code": "CS101",
    "degree_programs": [
            {'degree_program': 'CST', 'semester': 1},
            {'degree_program': 'IIT', 'semester': 2}
            ]
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Course alreay exists!",
  "data": null
}
```

---

## 2. Update Course

**Endpoint:** `PUT /api/courses/`

**Description:** Update an existing course

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "id": 1,
  "title": "Advanced Python Programming",
  "course_code": "CS101",
  "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
}
```

**cURL Command:**
```bash
curl -X PUT http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Advanced Python Programming",
    "course_code": "CS101",
    "degree_programs": "Computer Science"
  }'
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Course updated successfully",
  "data": {
    "id": 1,
    "title": "Advanced Python Programming",
    "course_code": "CS101",
    "degree_programs": "Computer Science"
  }
}
```

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "Course not found",
  "data": null
}
```

---

## 3. Delete Course

**Endpoint:** `DELETE /api/courses/<course_id>/`

**Description:** Delete a course by ID

**cURL Command:**
```bash
curl -X DELETE http://localhost:8000/api/courses/1/
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Course deleted successfully",
  "data": null
}
```

---

## 4. List All Courses

**Endpoint:** `GET /api/courses/all/`

**Description:** Retrieve all available courses

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/courses/all/
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "",
  "data": [
    {
      "id": 1,
      "title": "Introduction to Python",
      "course_code": "CS101",
      "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
    },
    {
      "id": 2,
      "title": "Data Structures",
      "course_code": "CS102",
      "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
    },
    {
      "id": 3,
      "title": "Linear Algebra",
      "course_code": "MATH101",
      "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
    }
  ]
}
```

---

## 5. Get Courses by Degree Program and Semester

**Endpoint:** `GET /api/courses/by-degree/`

**Description:** Retrieve courses filtered by degree program and semester

**Query Parameters:**
- `degree_program` (required): The degree program name
- `semester` (optional): Semester number (default: 1)

**cURL Commands:**

**Get courses for a specific degree program:**
```bash
curl -X GET "http://localhost:8000/api/courses/by-degree/?degree_program=Computer%20Science"
```

**Get courses for a specific degree program and semester:**
```bash
curl -X GET "http://localhost:8000/api/courses/by-degree/?degree_program=Computer%20Science&semester=2"
```

**Get courses for Mathematics program:**
```bash
curl -X GET "http://localhost:8000/api/courses/by-degree/?degree_program=Mathematics&semester=1"
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "",
  "data": [
    {
      "id": 1,
      "title": "Introduction to Python",
      "course_code": "CS101",
      "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
    },
    {
      "id": 2,
      "title": "Data Structures",
      "course_code": "CS102",
      "degree_programs": [
{'degree_program': 'CST', 'semester': 1},
{'degree_program': 'IIT', 'semester': 2}
]
    }
  ]
}
```

**Error Response (400 Bad Request):**
```json
{
  "success": false,
  "message": "degree_program and semester query parameters are required",
  "data": null
}
```

---

## Request/Response Examples

### Example 1: Create and List Courses

**Step 1: Create a new course**
```bash
curl -X POST http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Web Development",
    "course_code": "CS201",
    "degree_programs": "Computer Science"
  }'
```

**Step 2: Get all courses**
```bash
curl -X GET http://localhost:8000/api/courses/all/
```

**Step 3: Filter courses by degree program**
```bash
curl -X GET "http://localhost:8000/api/courses/by-degree/?degree_program=Computer%20Science&semester=1"
```

### Example 2: Update and Delete a Course

**Step 1: Update a course**
```bash
curl -X PUT http://localhost:8000/api/courses/ \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Advanced Web Development",
    "course_code": "CS201",
    "degree_programs": "Computer Science"
  }'
```

**Step 2: Delete the course**
```bash
curl -X DELETE http://localhost:8000/api/courses/1/
```

---

## Error Responses

### 400 Bad Request - Missing Parameters
```json
{
  "success": false,
  "message": "degree_program and semester query parameters are required",
  "data": null
}
```

### 400 Bad Request - Course Already Exists
```json
{
  "success": false,
  "message": "Course alreay exists!",
  "data": null
}
```

### 400 Bad Request - Course Not Found
```json
{
  "success": false,
  "message": "Course not found",
  "data": null
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "message": "An error occurred while processing the request",
  "data": null
}
```

---

## Notes

- Permission class is set to `AllowAny` for all endpoints (consider adding authentication in production)
- Query parameters are case-sensitive
- URL-encode special characters in query parameters (spaces as `%20`, etc.)
- The `semester` parameter defaults to 1 if not provided
- Course codes should be unique across the system
- The `degree_programs` field can contain comma-separated values for multiple programs
