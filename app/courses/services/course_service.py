from app.courses.models.course_model import Course

def get_course_by_id(course_id):
    return Course.objects.filter(id=course_id).first()

def get_all_courses():
    return Course.objects.all()

def create_course(name, course_code, degree_programs):
    new_course = Course(title=name, course_code=course_code, degree_programs=degree_programs)
    new_course.save()
    return new_course

def update_course(course_id, name=None, course_code=None, degree_programs=None):
    course = get_course_by_id(course_id)
    if not course:
        raise ValueError("Course not found")
    
    if name:
        course.title = name
    if course_code:
        course.course_code = course_code
    if degree_programs is not None:
        course.degree_programs = degree_programs
    
    course.save()
    return course

def delete_course(course_id):
    course = get_course_by_id(course_id)
    if not course:
        raise ValueError("Course not found")
    
    course.delete()
    return True

def get_courses_by_degree_and_semester(degree_program, semester):
    all_courses = Course.objects.all()
    filtered_courses = []
    for course in all_courses:
        for program in course.degree_programs:
            if (str.upper(program['degree_program']) == str.upper(degree_program) and int(program['semester']) == int(semester)):
                filtered_courses.append(course)
    return filtered_courses