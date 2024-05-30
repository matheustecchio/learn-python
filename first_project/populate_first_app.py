import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## FAKE POPULATION SCRIPT
import random
from faker import Faker
from first_app.models import AccessRecord, Topic, Webpages

fake = Faker()

# Creating possibilities for Topics
topics = ['Search','Social','Marketplace','News','Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

# Creating fake data for Webpage 
def populate(N=5):
    for entry in range(N):
        
        top = add_topic()
        fake_name = fake.company()
        fake_url = fake.url()
        fake_date = fake.date()

        web_pg = Webpages.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=web_pg,date=fake_date)[0]

if __name__ == '__main__':
    data_entries_quantity = int(input("How many data entries do you want? "))
    print("Populating...")
    populate(data_entries_quantity)
    print("Population of " + str(data_entries_quantity) + " more data complete!")

