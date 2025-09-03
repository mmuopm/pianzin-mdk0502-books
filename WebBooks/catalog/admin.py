from django.contrib import admin

from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'photo')
admin.site.register(Author, AuthorAdmin)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

#admin.site.register(Book)
#admin.site.register(BookInstance)

admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)


