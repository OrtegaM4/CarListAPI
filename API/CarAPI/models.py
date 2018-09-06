from django.db import models
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.styles import get_all_styles
from django.contrib.auth import get_user_model

# Create your models here.
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Cars(models.Model):
    make= models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    horsepower = models.IntegerField( null=False)
    #owner = models.ForeignKey('auth.User', related_name='cars', on_delete=models.CASCADE,default=get_user_model)
    highlighted = models.TextField(default='')
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    linenos= models.BooleanField(default=True)
    title = models.CharField(max_length=100, blank=True, default='')
    style = models.CharField(choices=STYLE_CHOICES, default='friendly',max_length=100)
    code = models.TextField(default='')
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Cars, self).save(*args, **kwargs)


    def ___str___(self):
        return "A {} {} with {} horsepower".format(self.make, self.name, self.horsepower)
