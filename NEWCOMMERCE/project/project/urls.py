from django.contrib import admin
from django.urls import path, include
from shop.views import SignupView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('',include('shop.urls'))
    path('accounts/signup/', SignupView, name="signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# accounts// [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']