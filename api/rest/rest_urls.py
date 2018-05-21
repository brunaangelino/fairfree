# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api.rest.apis import FairList, FairDetail


urlpatterns = [
    path('rest/fair/', FairList.as_view(), name='api-fair-list'),
    path('rest/fair/<str:registro>/', FairDetail.as_view(), name='api-fair-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)