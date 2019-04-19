"""Blog Model"""

from config.database import Model


class Blog(Model):
    """Blog Model"""
    __fillable__ = ['title', 'body']