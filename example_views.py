from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import CreateView, UpdateView, ListView, \
    DeleteView, TemplateView

from example.forms import EditorTextForm
from example.models import EdidorText


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.

    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class EditorHomeView(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    form_class = EditorTextForm
    model = EditorText

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_texts'] = EditorText.objects.filter(
            created_by=self.request.user
        )[:5]
        return context

    def get_object(self):
        pk = self.request.POST.get('pk')
        if not pk:
            return None
        return EdidorText.objects.get(pk=int(pk))

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        self.object = self.get_object()
        kwargs = super().get_form_kwargs()
        return kwargs
