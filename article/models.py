# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Article(models.Model):
	"""docstring for Article"""
	class Meta():
		db_table = "article"


	article_title = models.CharField(max_length = 200)
	article_thema = models.CharField(max_length = 100)
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default = 0)



class Comments(models.Model):
	class Meta():
		db_table = "comments"

	comments_text = models.TextField(verbose_name = "Comment text")
	comments_article = models.ForeignKey(Article)


