#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

import inspect
import typing as t

from kombu import Consumer
from kombu import Producer
from kombu import Connection
from inspect import Signature
from django.conf import settings
from django.apps import AppConfig
from django.core.checks import Error
from service_kombu.constants import KOMBU_CONFIG_KEY
from service_core.core.as_helper import get_obj_string_repr


def check_settings(app_configs: t.List[AppConfig], **kwargs: t.Any) -> t.List[Error]:
    """ 检查应用的配置

    @param app_configs: 应用配置
    @param kwargs: 其它参数
    @return: t.List[Error]
    """
    all_config_check_errors = errors = []
    config = getattr(settings, KOMBU_CONFIG_KEY, {})
    # 验证connect_options连接配置参数
    connect_options = config.get('connect_options', {})
    connect_signature = inspect.signature(Connection)
    try:
        connect_signature.bind(**connect_options)
    except Exception as e:
        errors.append(Error(get_obj_string_repr(e)))
    try:
        Connection(**connect_options).connect()
    except Exception as e:
        errors.append(Error(get_obj_string_repr(e)))
    # 验证consume_options消费配置参数
    consume_options = config.get('consume_options', {})
    consume_parameters = inspect.signature(Consumer).parameters.values()
    # 忽略掉首个配置参数,后续再单独传递
    consume_parameters = [
        p for i, p in enumerate(consume_parameters) if i != 0
    ]
    consume_signature = Signature(consume_parameters)
    try:
        consume_signature.bind(**consume_options)
    except Exception as e:
        errors.append(Error(get_obj_string_repr(e)))
    # 验证publish_options发布配置参数
    publish_options = config.get('publish_options', {})
    publish_parameters = inspect.signature(Producer).parameters.values()
    # 忽略掉首个配置参数,后续再单独传递
    publish_parameters = [
        p for i, p in enumerate(publish_parameters) if i != 0
    ]
    publish_signature = Signature(publish_parameters)
    try:
        publish_signature.bind(**publish_options)
    except Exception as e:
        errors.append(Error(get_obj_string_repr(e)))
    return all_config_check_errors
