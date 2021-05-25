from django import forms
from .models import Thought

# Title: Creating the ModelForm
# Author: Learning about Electronics
# Date: 2-10-21
# Code version: n/a
# URL: http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php
# Software License: n/a
# Comments: Used to create ThoughtForm model


class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['thought_text', ]
