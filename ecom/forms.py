from django.forms import ModelForm
from .models import Used


class UsedPostForm(ModelForm):
    class Meta:
        model= Used
        exclude=["user"]

    def __init__(self, *args, **kwargs):
        super(UsedPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False