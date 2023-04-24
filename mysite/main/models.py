from django.db import models

# Create your models here.

class Parent(models.Model):

    name = models.CharField('Parent name', max_length=100)

    def __str__(self):
        return self.name

class Child1(models.Model):

    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_child1')
    name = models.CharField('Child1 name', max_length=100)  

    def __str__(self):
        return self.name
    
class Child2(models.Model):

    parent = models.ForeignKey(Child1, on_delete=models.CASCADE, related_name='parent_child2')
    name = models.CharField('Child2 name', max_length=100)  

    def __str__(self):
        return self.name
    

class Child3(models.Model):

    parent = models.ForeignKey(Child2, on_delete=models.CASCADE, related_name='parent_child3')
    name = models.CharField('Child3 name', max_length=100)  

    def __str__(self):
        return self.name