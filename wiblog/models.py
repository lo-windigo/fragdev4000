from django.db import models
from django.core.urlresolvers import reverse


## Tag - A text tag, used to categorize posts
class Tag(models.Model):
	desc = models.CharField('Tag', max_length=50)

	def __unicode__(self):
		return self.desc

	def get_absolute_url(self):
		return reverse("wiblog:tags", args=[self.desc])


## Post - a blog post
class Post(models.Model):
	DFT = 'DFT'
	PUB = 'PUB'
	PUBLISH_STATUS = (
		(DFT, 'Draft'),
		(PUB, 'Published'),
	)
	body = models.TextField()
	date = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=150)
	status = models.CharField(max_length=9, choices=PUBLISH_STATUS)
	tags = models.ManyToManyField(Tag, blank=True)
	title = models.CharField(max_length=150)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("wiblog:post", args=[self.slug])


## Comments - Other people's input on posts
class Comment(models.Model):
	HAM = 'HAM'
	SPM = 'SPM'
	UNK = 'UNK'
	MOD_STATUS = (
		(HAM, 'Valid'),
		(SPM, 'Invalid (Spam)'),
		(UNK, 'Unmoderated'),
	)
	comment = models.TextField()
	name = models.CharField(max_length=150)
	moderated = models.CharField(choices=MOD_STATUS, default=UNK, max_length=14)
	post = models.ForeignKey(Post)
	url = models.URLField()
