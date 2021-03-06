# This file is part of the FragDev Website.
# 
# the FragDev Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# the FragDev Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the FragDev Website.  If not, see <http://www.gnu.org/licenses/>.

# This file is part of FragDev.
#
# FragDev is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FragDev is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FragDev.  If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils.text import slugify
from imghdr import what


class Image(models.Model):
    '''
    Represents a single uploaded image
    '''
    title = models.CharField(max_length=250)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    imgFile = models.FileField(upload_to='img/')
    slug = models.SlugField()
    content_type = models.CharField(max_length=30,
            blank=True,
            null=True)

    def save(self, *args, **kwargs):

        # Create a slug for this image
        if not self.id and self.slug == '':
            self.slug = slugify(self.title)

        # Generate different versions
        # TODO

        # Save the content type (required for headers later)
        self.content_type = what(self.imgFile)

        super(Image, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return self.imgFile.url

    def __str__(self):
        return self.title
