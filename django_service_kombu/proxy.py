#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from django.conf import settings
from service_kombu.constants import KOMBU_CONFIG_KEY

from service_kombu.core.standalone.amqp.pub import AMQPPubStandaloneProxy
from service_kombu.core.standalone.amqp.rpc import AMQPRpcStandaloneProxy


def get_amqp_pub_proxy() -> AMQPPubStandaloneProxy:
    """ 获取AMQP PUB代理 - 惰性加载

    @return: AMQPPubStandaloneProxy
    """
    config = getattr(settings, KOMBU_CONFIG_KEY, {})
    return AMQPPubStandaloneProxy(config=config)


def get_amqp_rpc_proxy() -> AMQPRpcStandaloneProxy:
    """ 获取AMQP RPC代理 - 惰性加载

    @return: AMQPRpcStandaloneProxy
    """
    config = getattr(settings, KOMBU_CONFIG_KEY, {})
    return AMQPRpcStandaloneProxy(config=config)
