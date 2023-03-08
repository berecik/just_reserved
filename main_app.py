import flet as ft
from django.urls import path
import flet_django as fdj

from pods.ft_views import services
from pods.models import Pod
from flet_django.pages import GenericApp
from flet_django.views import ft_view
from flet_django.middlewares import simple_view_middleware
from flet_django.navigation import Fatum

from ft_views import home, get_view





main = fdj.GenericApp(
    # destinations=[
    #     fdj.Fatum("/", icon=ft.icons.HOME, label="home"),
    #     fdj.Fatum("/services", icon=ft.icons.LIST_SHARP, label="reservation")
    # ],
    urls=[
        path("", home),
        path("services", services),
        path("services/<int:pod_id>/", services)
    ],
    view_factory=get_view
)
