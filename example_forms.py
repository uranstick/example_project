from django import forms
from django.forms import inlineformset_factory
from projects.models import Project


from .models import Invoice, InvoiceUser


class InvoiceForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(
            projectuser__user=user.id, status='active'
        )

    class Meta:
        model = Invoice
        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 3, 'cols': 10}
            ),
            'display_hours': forms.RadioSelect,
        }
        fields = "__all__"
        exclude = ('hours', 'hour_cost', 'status')


class InvoicePreviewForm(forms.ModelForm):
    class Meta:
        model = Invoice
        widgets = {
            'hours': forms.NumberInput(attrs={'step': 0.1}),
            'hour_cost': forms.NumberInput(attrs={'step': 0.01}),
        }
        fields = ('hours', 'hour_cost')


class BaseInvoiceUserFormSet(forms.BaseInlineFormSet):

    def __init__(self, *args, **kwargs):
        super(BaseInvoiceUserFormSet, self).__init__(*args, **kwargs)
        # restrict forms project_user field with only related project users
        project_users_qs = self.instance.project.projectuser_set.all()
        for form in self.forms:
            form.fields['project_user'].queryset = project_users_qs


InvoiceUserInlineFormSet = inlineformset_factory(
    Invoice,
    InvoiceUser,
    formset=BaseInvoiceUserFormSet,
    fields=('project_user', 'hours', 'hour_cost'),
    extra=0
)
