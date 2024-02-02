from django.db import models

# SPECIAL IMPORTS 
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _ 
from django.utils.text import slugify 
from ckeditor.fields import RichTextField

# INTERNAL
from api.auther.models import BaseModel

# CUstomer User 
User = get_user_model()

class BlogPost(BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    title = models.CharField(_('blog title'),max_length=100,null=True,blank=True)
    content = RichTextField()
    draft = models.BooleanField(default=False)
    slug  = models.SlugField(unique=True,max_length=150,editable=False)
    image = models.ImageField(upload_to='post',null=True)
    modifyed_by = models.ForeignKey(User,on_delete=models.CASCADE,default=1,related_name='modifyed_by')

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = slugify(self.title.replace("ı", "i"))
        unique = slug
        number = 1

        while BlogPost.objects.filter(slug=unique).exists():
            unique = '{}-{}'.format(slug, number)
            number += 1
        return unique

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.get_slug()
        super().save(*args, **kwargs)
        
# COMMENT
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='post')
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created = models.DateTimeField(editable=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.post.title  