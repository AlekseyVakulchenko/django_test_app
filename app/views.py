from django.views.generic import ListView

from .models import Orders


class OrderListView(ListView):
    """
    View for render orders with status paid=True and info of them
    """
    template_name = 'order.html'
    model = Orders

    def get_queryset(self):
        qs = self.model.objects.filter(status__paid=True)
        return qs
