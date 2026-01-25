# Feedback API - cURL Request Documentation

## Base URL
```
http://localhost:8000/api/feedbacks
```

---

## 1. Create Feedback

**Endpoint:** `POST /api/feedbacks/` 

**Description:** Create a new feedback entry

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "user_id": 1,
  "course_id": 1,
  "answers": [
    {
      "question_id": 1,
      "question_text": "How would you rate the course content?",
      "rating": 5
    },
    {
      "question_id": 2,
      "question_text": "Was the instructor knowledgeable?",
      "rating": 4
    }
  ],
  "feedback_text": "This course was very informative and well-structured.",
  "rating": 4
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/feedbacks/ \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "course_id": 1,
    "answers": [
      {
        "question_id": 1,
        "question_text": "How would you rate the course content?",
        "rating": 5
      },
      {
        "question_id": 2,
        "question_text": "Was the instructor knowledgeable?",
        "rating": 4
      }
    ],
    "feedback_text": "This course was very informative and well-structured.",
    "rating": 4
  }'
```

**Success Response (201 Created):**
```json
{
  "success": true,
  "message": "Feedback created successfully",
  "data": {
    "id": 1,
    "user_name": "john_doe",
    "course_title": "Introduction to Python",
    "course_code": "CS101",
    "feedback_text": "This course was very informative and well-structured.",
    "rating": 4,
    "created_at": "2026-01-24T10:30:00Z"
  }
}
```

---

## 2. Update Feedback

**Endpoint:** `PUT /api/feedbacks/<feedback_id>/`

**Description:** Update an existing feedback entry

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "feedback_text": "Updated feedback text",
  "rating": 5
}
```

**cURL Command:**
```bash
curl -X PUT http://localhost:8000/api/feedbacks/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "feedback_text": "Updated feedback text",
    "rating": 5
  }'
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Feedback updated successfully",
  "data": {
    "id": 1,
    "user_name": "john_doe",
    "course_title": "Introduction to Python",
    "course_code": "CS101",
    "feedback_text": "Updated feedback text",
    "rating": 5,
    "created_at": "2026-01-24T10:30:00Z"
  }
}
```

---

## 3. List Feedbacks (with Filters)

**Endpoint:** `GET /api/feedbacks/list/`

**Description:** Retrieve filtered list of feedbacks

**Query Parameters:**
- `year` (optional): Academic year
- `semester` (optional): Semester number
- `degree_program` (optional): Degree program name
- `course_id` (optional): Course ID
- `course_code` (optional): Course code

**cURL Commands:**

**Get all feedbacks:**
```bash
curl -X GET http://localhost:8000/api/feedbacks/list/
```

**Filter by year and semester:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/list/?year=2026&semester=1"
```

**Filter by course:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/list/?course_id=1"
```

**Filter by course code:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/list/?course_code=CS101"
```

**Filter by degree program:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/list/?degree_program=Computer%20Science"
```

**Combined filters:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/list/?year=2026&semester=1&degree_program=Computer%20Science&course_code=CS101"
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": null,
  "data": [
    {
            "id": 4,
            "course_title": "Introduction to Computer Science",
            "course_code": "CS101",
            "feedback_text": "This course was very informative and well-structured.",
            "rating": 4,
            "answers": [
                {
                    "rating": 5,
                    "question_id": 1,
                    "question_text": "How would you rate the course content?"
                },
                {
                    "rating": 4,
                    "question_id": 2,
                    "question_text": "Was the instructor knowledgeable?"
                }
            ],
            "created_at": "2026-01-25T05:29:11.153169Z"
        },
        {
            "id": 5,
            "course_title": "Introduction to SQL",
            "course_code": "CS104",
            "feedback_text": "This course was very informative and well-structured.",
            "rating": 4,
            "answers": [
                {
                    "rating": 4,
                    "question_id": 1,
                    "question_text": "How would you rate the course content?"
                },
                {
                    "rating": 2,
                    "question_id": 2,
                    "question_text": "Was the instructor knowledgeable?"
                }
            ],
            "created_at": "2026-01-25T05:29:41.233640Z"
        }
  ]
}
```

---

## 4. Get Feedback Statistics

**Endpoint:** `GET /api/feedbacks/stats/`

**Description:** Get average rating statistics by course

**Query Parameters:**
- `year` (optional): Academic year
- `semester` (optional): Semester number
- `degree_program` (optional): Degree program name

**cURL Commands:**

**Get all statistics:**
```bash
curl -X GET http://localhost:8000/api/feedbacks/stats/
```

**Filter by year and semester:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/stats/?year=2026&semester=1"
```

**Filter by degree program:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/stats/?degree_program=Computer%20Science"
```

**Combined filters:**
```bash
curl -X GET "http://localhost:8000/api/feedbacks/stats/?year=2026&semester=1&degree_program=Computer%20Science"
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": null,
  "data": [
    {
      "course_id": 1,
      "course_code": "CS101",
      "course_title": "Introduction to Python",
      "average_rating": 4.5,
      "total_feedbacks": 2
    },
    {
      "course_id": 2,
      "course_code": "CS102",
      "course_title": "Data Structures",
      "average_rating": 4.2,
      "total_feedbacks": 5
    }
  ]
}
```

---

## 5. List All Questions

**Endpoint:** `GET /api/feedbacks/questions/`

**Description:** Retrieve all available feedback questions

**cURL Command:**
```bash
curl -X GET http://localhost:8000/api/feedbacks/questions/
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": null,
  "data": [
    {
      "id": 1,
      "text": "Was the course content relevant?"
    },
    {
      "id": 2,
      "text": "Was the instructor knowledgeable?"
    },
    {
      "id": 3,
      "text": "Would you recommend this course?"
    }
  ]
}
```

---

## 6. Create Question

**Endpoint:** `POST /api/feedbacks/questions/`

**Description:** Create a new feedback question

**Request Headers:**
```
Content-Type: application/json
```

**Request Body:**
```json
{
  "text": "How satisfied are you with the course materials?"
}
```

**cURL Command:**
```bash
curl -X POST http://localhost:8000/api/feedbacks/questions/ \
  -H "Content-Type: application/json" \
  -d '{
    "text": "How satisfied are you with the course materials?"
  }'
```

**Success Response (201 Created):**
```json
{
  "success": true,
  "message": "Question created successfully",
  "data": {
    "id": 4,
    "text": "How satisfied are you with the course materials?"
  }
}
```

---

## 7. Delete Question

**Endpoint:** `DELETE /api/feedbacks/questions/<question_id>/`

**Description:** Delete a feedback question

**cURL Command:**
```bash
curl -X DELETE http://localhost:8000/api/feedbacks/questions/1/
```

**Success Response (200 OK):**
```json
{
  "success": true,
  "message": "Question deleted successfully",
  "data": null
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "message": "Invalid request data",
  "data": {
    "field_name": ["Error message"]
  }
}
```

### 404 Not Found
```json
{
  "success": false,
  "message": "Feedback not found",
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

- All timestamps are in ISO 8601 format (UTC)
- Ratings must be between 1 and 5
- Permission class is set to `AllowAny` for all endpoints (consider adding authentication in production)
- Query parameters are case-sensitive where applicable
- URL-encode special characters in query parameters (spaces as `%20`, etc.)
