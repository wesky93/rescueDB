from django import forms
from multiupload.fields import MultiFileField

from .models import Rescue, Attachment

class RescueForm(forms.ModelForm):
    class Meta:
        model = Rescue
        fields = ['name', 'age', 'burth','address','phone','location','symptom','cause','content']  # not attachments!

    files = MultiFileField(required=False,min_num=0, max_num=5, max_file_size=1024*1024*6)

    def save(self, commit=True):
        instance = super(RescueForm, self).save(commit)
        for each in self.cleaned_data['files']:
            Attachment.objects.create(file=each, rescue=instance)

        return instance