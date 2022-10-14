from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField(default="message")
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # toString() 과 같음
    def __str__(self):
        # return f"Custom Post object({self.id})"
        return self.message

    class Meta:
        ordering = ["-id"]  # 기본 정렬

    # def message_length(self):
    #     return len(self.message)

    # message_length.short_description = "메세지 글자수"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, limit_choices_to={"is_public": True}
    )  # post_id 필드가 생성됨
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
