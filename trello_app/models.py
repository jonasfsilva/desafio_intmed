# from django.db import models


# class Board(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)


# class List(models.Model):
    
#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)

#     board = models.ForeignKey(Board, on_delete=models.PROTECT)


# class Card(models.Model):

#     trello_id = models.CharField(max_length=200)
#     nome = models.CharField(max_length=100)
#     board = models.ForeignKey(List, on_delete=models.PROTECT)