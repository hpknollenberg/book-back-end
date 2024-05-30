# Generated by Django 5.0.6 on 2024-05-30 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_book', '0002_bookshelf_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookshelves',
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='books',
            field=models.ManyToManyField(to='app_book.book'),
        ),
    ]