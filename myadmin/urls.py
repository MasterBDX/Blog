from django.urls import path

from .views import (authors_admin_view, DeleteAboutblogView,
                    confirm_author_view, DeleteAboutmeView,
                    AddAboutmeView, DeletePrvacyPolicyView,
                    AddAboutblogView,
                    AddPrvacyPolicyView,
                    EditAboutmeView,
                    EditAboutblogView,
                    EditPrvacyPolicyView,)

app_name = 'myadmin'
urlpatterns = [
    path('authors_admin/', authors_admin_view, name='authors_admin'),
    path('add_about_me/', AddAboutmeView.as_view(), name='add_aboutme'),
    path('add_about_blog/', AddAboutblogView.as_view(), name='add_aboutblog'),
    path('add_privacy_and_policy/', AddPrvacyPolicyView.as_view(),
         name='add_privacy_policy'),

    path('edit-about-me/<int:pk>/',
         EditAboutmeView.as_view(), name='edit_aboutme'),

    path('edit-about-blog//<int:pk>/',
         EditAboutblogView.as_view(), name='edit_aboutblog'),

    path('edit-privacy-and-policy/<int:pk>/', EditPrvacyPolicyView.as_view(),
         name='edit_privacy_policy'),

    path('delete-about-me/<int:pk>/',
         DeleteAboutmeView.as_view(), name='delete_aboutme'),

    path('delete-about-blog//<int:pk>/',
         DeleteAboutblogView.as_view(), name='delete_aboutblog'),

    path('delete-privacy-and-policy/<int:pk>/', DeletePrvacyPolicyView.as_view(),
         name='delete_privacy_policy'),

    path('confirm-author/<slug:slug>/',
         confirm_author_view, name='confirm_author')
]