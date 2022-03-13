from django.urls import path
from .merchant_views import PaymeCallbackView
from .views import CardView, CardGetVerifyCodeView, CardRemoveView, PayTransactionView

urlpatterns = [
    # path('click/transaction/', ClickCallbackView.as_view()),
    # path('payme/transaction/', PaymeCallbackView.as_view()),
    path('card/', CardView.as_view()),
    path('card/verify/', CardGetVerifyCodeView.as_view()),
    path('card/remove/<int:pk>/', CardRemoveView.as_view()),
    path('pay/<int:pk>/', PayTransactionView.as_view())
]

