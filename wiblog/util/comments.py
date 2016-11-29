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

from fragdev.contact import validate_ham
from django.forms import ModelForm
from django import forms
from wiblog.models import Comment

class CommentForm(ModelForm):
	verify = forms.CharField(label='Anti-spam: Type in the word "power"',validators=[validate_ham],max_length=5)
	class Meta:
		model = Comment
		fields = ('name', 'url', 'comment')