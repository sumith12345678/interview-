from django.db import models

class Node(models.Model):
    name = models.CharField(max_length=255)
    node_id = models.IntegerField(unique=True)
    parent = models.IntegerField(unique=True)
    left_child = models.IntegerField()
    right_child = models.IntegerField()

    

    def __str__(self):
        return self.name
