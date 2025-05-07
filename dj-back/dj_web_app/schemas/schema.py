import graphene
from dj_web_app.models import Book
from graphene_django.types import DjangoObjectType

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    hello = graphene.String(default_value="Hello, world!")

    def resolve_all_books(self, info):
        return Book.objects.all()
    
schema = graphene.Schema(query=Query)
