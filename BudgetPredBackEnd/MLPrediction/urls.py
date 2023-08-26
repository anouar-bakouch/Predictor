from django.contrib import admin
from django.urls import path
from BudgetPRed.views import MostBoughtCategoryView,GetLastMonthsBudgetExpensesView,GetActualBudgetExpensesView,SaveFormAPIView,NewFormAPIView,ListMonthlyBudgetView,GetUserInfoView,ItemsCartAPIView,AddToCartAPIVIEW, ListMonthlyPurchaseView, ListPurchaseView,LoginView, PredictNextMonthMONTSTRUView, PurchaseView,refreshTokenView, AddItemView, DeleteItemView, GetItemView, GetUserView, ItemAPIView, ItemCategorieAPIView, PredictedItems, UpdateItemView, UpdateUserView, UserRegistrationView, index
urlpatterns = [
    path('',index),
    path('admin/', admin.site.urls),
    # ITEM ------------------------------
    path('add-item/', AddItemView.as_view()),
    path('update-item/', UpdateItemView.as_view()),
    path('delete-item/<int:pk>/', DeleteItemView.as_view()),
    path('get-item/', GetItemView.as_view()),
    # CART 
    path('add-cart/', AddToCartAPIVIEW.as_view()), 
    path('get-cart/',ItemsCartAPIView.as_view()),
    path('delete-item/<int:pk>/',DeleteItemView.as_view()),
    #TOKEN 
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='token-obtain-pair'),
    path('auth/refresh/', refreshTokenView.as_view(), name='token-refresh'),
    # USER ------------------------------
    path('GetUser/<int:pk>/',GetUserView.as_view()),
    path('DeleteUser/<int:pk>/',DeleteItemView.as_view()),
    path('updateuser/<int:pk>/',UpdateUserView.as_view()),
    path('userinfo/<int:pk>/',GetUserInfoView.as_view(),name='user-info'),
    # PREDICTION ------------------------
    path('predict-items/', PredictedItems.as_view(), name='PredictItems'),
    path('predict-budget/',PredictNextMonthMONTSTRUView.as_view(),name='PredictBudget'),
    # path('PredictMONTSTRU')
    path('list-item/',ItemAPIView.as_view() , name='list-item'),
    path('list-item-categorie/',ItemCategorieAPIView.as_view() , name='list-item-categorie'),
    # PURCHASE ---------------------------
    path('add-purchase/', PurchaseView.as_view()),
    path('list-purchase/', ListPurchaseView.as_view()),
    path('list-month-purchase/',ListMonthlyPurchaseView.as_view()),
    # Months DATA -------- 
    path('list-data/',ListMonthlyBudgetView.as_view()),
    # Objectives PART --------------------
    path('save-new-form/',SaveFormAPIView.as_view()),
    path('get-new-form/',NewFormAPIView.as_view()),
    path('get-objectives/',GetActualBudgetExpensesView.as_view()),
    path('get-last-months-objectives/',GetLastMonthsBudgetExpensesView.as_view()),
    path('most-bought-categories/',MostBoughtCategoryView.as_view())
]

