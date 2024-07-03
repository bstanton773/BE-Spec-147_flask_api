from faker import Faker

import faker_commerce
from random import randint

fake = Faker()
fake.add_provider(faker_commerce.Provider)

for _ in range(10):
    print(fake.ecommerce_name() + ' costs $' + str(randint(1, 100)))
