from django.urls import path
from main.views import (show_main, create_product, show_product
                        , register, login_user, logout_user
                        , update_product, delete_product
                        , show_xml, show_json, show_xml_by_id, show_json_by_id
                        )

app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
    path("add/", create_product, name="create_product"),
    path("detail/<uuid:id>/", show_product, name="show_product"),

    # product update
    path("edit/<uuid:id>/", update_product, name="update_product"),
    path("delete/<uuid:id>/", delete_product, name="delete_product"),

    # login page
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # non Main func
    path("xml/", show_xml, name="show_xml"),
    path("json/", show_json, name="show_json"),
    path("xml/<uuid:id>/", show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", show_json_by_id, name="show_json_by_id"),

]