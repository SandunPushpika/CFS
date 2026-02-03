from app.degrees.models.degree_model import Degree


def get_degree_by_id(degree_id):
    return Degree.objects.filter(id=degree_id).first()


def get_all_degrees():
    return Degree.objects.all()


def create_degree(name, short_code):
    # Simple create; uniqueness of short_code is enforced by DB
    new_degree = Degree(name=name, short_code=short_code)
    new_degree.save()
    return new_degree


def delete_degree(degree_id):
    degree = get_degree_by_id(degree_id)
    if not degree:
        raise ValueError("Degree not found")
    degree.delete()
    return True
