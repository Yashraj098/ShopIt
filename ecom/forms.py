from django.forms import ModelForm
from .models import Used,Item,Business


class UsedPostForm(ModelForm):
    class Meta:
        model= Used
        exclude=["user"]

    def __init__(self, *args, **kwargs):
        super(UsedPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False

    
class ItemForm(ModelForm):
    class Meta:
        model=Item
        exclude=[]

    def __init__(self, *args, **kwargs):
        super(UsedPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False


class BusinessForm(ModelForm):
    class Meta:
        model=Business
        exclude=[]
    
    def __init__(self, *args, **kwargs):
        super(UsedPostForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False