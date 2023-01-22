from django.urls import path
from .views import *

app_name = "main"



urlpatterns = [
    path('books/', BooksView.as_view()),
    path('create/', CreateBookView.as_view()),
    path('special/<int:pk>', SpecialBookView.as_view()),
    path('subcategory/', SubcategoryView.as_view()),
    path('create_sub/', CreateSubcategoryView.as_view()),
    path('special_sub/<int:pk>', SpecialSubcategoryView.as_view()),
    path('category/', CategoryView.as_view()),
    path('create_cat/', CreateCategoryView.as_view()),
    path('special_cat/<int:pk>', SpecialCategoryView.as_view()),
    path('image/', ListImageView.as_view()),
    path('image_del/<int:pk>', DeleteImageView.as_view()),
    path('audio/', ListAudioView.as_view()),
    path('audio_del/<int:pk>', DeleteAudioView.as_view()),


]