from django.db import models


TOPIC_TYPE =(
    ('key_features','Key Features'),
    ('topics','Topics Of Discussion'),
    ('people','Guests')
)

class Item(models.Model):
    Topic = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=2000, unique=False)
    topic_type = models.CharField(max_length=200, choices=TOPIC_TYPE,default='Key Features')
    image = models.ImageField(upload_to="G20/images",default="")

def __str__(self):
    return self.Title