import stripe
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, ListView
from .models import Item

from config import settings
from items.models import Item
from items.services.stripe_service import create_stripe_session

class IndexView(ListView):
    model = Item
    template_name = 'items/index.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all().order_by('id')

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'
    context_object_name = 'item'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = settings.STRIPE_PUBLIC_KEY
        return context

class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs["id"]
        item = get_object_or_404(Item, id=item_id)
        session_id = create_stripe_session(item)
        return JsonResponse({'sessionId': session_id})


def success_view(request):
    return render(request, 'items/success.html')