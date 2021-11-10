from django.db import models

class Enquiry(models.Model):
    user_name = models.CharField(max_length=10000)
    book_name = models.CharField(max_length=10000)
    publication_name = models.CharField(max_length=10000, null=True)
    book_edition = models.CharField(max_length=10000, null=True)

    def __str__(self):
        return self.book_name

    
