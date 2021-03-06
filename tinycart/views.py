from django.views.generic import ListView
from .models import Cart


class CartItemList(ListView):

    def get_queryset(self):
        return self.request.cart.items.all()

    def get_context_data(self, **kwargs):
        context = super(CartItemList, self).get_context_data(**kwargs)
        context.update({
            'available_object_list': [],
            'unavailable_object_list': [],
            'held_object_list': [],
        })
        for object in context['object_list']:
            if object.is_available:
                if object.is_held:
                    context['held_object_list'].append(object)
                else:
                    context['available_object_list'].append(object)
            else:
                context['unavailable_object_list'].append(object)
        return context

    def get(self, request, *args, **kwargs):
        return super(CartItemList, self).get(request, *args, **kwargs)
