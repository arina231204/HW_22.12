from django.db import models

class Tweet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.author} - {self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text} - {self.title}'

class Mark(models.Model):
    choices_like = [('like','Like'), ('dislike','Dislike')]
    mark_value = models.CharField(max_length=255, choices=choices_like)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.mark_value
