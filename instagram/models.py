from django.db import models


class Post(models.Model):
    message = models.TextField(default="message")
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name="공개 여부")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return f"Custom Post object({self.id})"
        return self.message

    # def message_length(self):
    #     return len(self.message)

    # message_length.short_description = "메세지 글자수"
