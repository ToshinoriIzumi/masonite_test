""" A BlogController Module """
from app.Blog import Blog
from masonite.request import Request
from masonite.response import Response
from masonite.view import View

class BlogController:
    """BlogController
    """
    def __init__(self, request:Request, view:View, response: Response):
        self.request = request
        self.response = response
        self.view = view

    def index(self):
        blogs = Blog.all()
        return self.view.render('blog.index', {'blogs':blogs})
    
    def show(self):
        id = self.request.param('id')
        blog = Blog.find(id)
        return self.view.render('blog.show', {'blog':blog})

    def add(self):
        return self.view.render('blog.add')

    def create(self):
        blog = Blog()
        blog.title = self.request.input('title')
        blog.body = self.request.input('body')
        blog.save()
        return self.response.redirect('/')

    def edit(self):
        id = self.request.param('id')
        blog = Blog.find(id)
        return self.view.render('blog.edit', {'blog': blog})
    
    def update(self):
        id = self.request.param('id')
        blog = Blog.find(id)
        blog.title = self.request.input('title')
        blog.body = self.request.input('body')
        blog.save()
        return self.response.redirect('/')
    
    def delete(self):
        id = self.request.input('id')
        blog = Blog.find(id)
        blog.delete()
        return {'id':id}
