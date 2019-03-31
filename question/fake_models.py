from faker import Faker

from question.models import Tag

fake = Faker()

def generate_tag():
    Tag.objects.create_tag(title=fake.name())


for _ in range(10000):
    generate_tag()
