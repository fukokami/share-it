from django.views.generic.base import TemplateView


class ProfileView(TemplateView):
    template_name = "account/profile.html"


profile = ProfileView.as_view()