from faker import Faker


def get_random_text():
    faker = Faker()
    return faker.text()
