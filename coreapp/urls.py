from django.urls import path
from .views import AccountViewSet, MemberViewSet

urlpatterns = [
    url('members/$', MemberViewSet, name='members-list'),
    url('members/{pk}/$', MemberViewSet, name='members-details'),
    url('accounts/$', AccountViewSet, name='account-list'),
    url('accounts/{pk}/$', AccountViewSet, name='account-details')
]