from django import urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/category/', include('category.urls')),
    path('api/coupon/', include('coupons.urls')),
    path('api/products/', include('product.urls')),
    path('api/shipping/', include('shipping.urls')),
    path('api/order/', include('orders.urls')),
    path('api/payment/', include('payment.urls')),
    path('api/user/', include('user.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', 
                        TemplateView.as_view(template_name='index.html'))]
