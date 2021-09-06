#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from django.apps import AppConfig
from django.core.checks import register

from .checks import check_settings


class ServiceKombuAppConfig(AppConfig):
    """ ServiceKombu应用配置 """

    name = 'django_service_kombu'
    verbose_name = 'django-service-kombu'

    def ready(self) -> None:
        """ 加载应用前检查配置 """
        register(self.name)(check_settings)
