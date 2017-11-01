# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse, Http404
from django.template.loader import render_to_string
from django.shortcuts import render, render_to_response, redirect
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import auth

from article.models import Article, Comments
from forms import CommentForm
# Create your views here.

# def basic_one(request):
# 	view = "basic_one"
# 	html = ["<html><body>This is  view</body></html>"]
# 	return HttpResponse(html)

# def template_two(request):
# 	view = "template_two"
# 	ctx = {
# 		'name': view
# 	}
# 	message = render_to_string('myview.html', ctx)
# 	return HttpResponse(message)


# def template_three(request):
# 	view = "template_three"
# 	ctx = {
# 		'name': view
# 	}
# 	message = render_to_string('myview.html', ctx)
# 	return HttpResponse(message)



def articles(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 2)
	return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})


def article(request,article_id =  1):
	comment_form = CommentForm
	args = {}
	args.update(csrf(request))
	args['article'] = Article.objects.get(id = article_id)
	args['comments'] = Comments.objects.filter(comments_article_id = article_id)
	args['form'] = comment_form
	args['username'] = auth.get_user(request).username
	return render_to_response('article.html', args)



def addlike(request,article_id):
	try:
		if article_id in request.COOKIES:
			redirect(request.META['HTTP_REFERER'])
		else:
			article = Article.objects.get(id = article_id)
			article.article_likes += 1
			article.save()
			response = redirect(request.META['HTTP_REFERER'])
			response.set_cookie(article_id,'test')
			return response
	except ObjectDoesNotExist: 
		raise Http404
	return redirect(request.META['HTTP_REFERER'])

def addcomment(request,article_id):
	if request.POST and ("pause" not in request.session):
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit = False)
			comment.comments_article = Article.objects.get(id = article_id)
			form.save()
			request.session.set_expiry(60)
			request.session['pause'] =  True 
	return redirect('/articles/get/%s/' % article_id)



























