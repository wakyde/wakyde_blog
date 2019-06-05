from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Link


class LinkListView(CommonViewMixin, ListView):
    queryset = Link.get_by_link()
    template_name = 'config/links.html'
    context_object_name = 'link_list'
