#! -*- coding: utf-8 -*-
#
# author: forcemain@163.com

from __future__ import annotations

from django.conf import settings
from service_kombu.constants import KOMBU_CONFIG_KEY

from service_kombu.core.standalone.amqp.pub import AMQPPubStandaloneProxy
from service_kombu.core.standalone.amqp.rpc import AMQPRpcStandaloneProxy

__all__ = ('amqp_pub', 'amqp_rpc')

amqp_conf = getattr(settings, KOMBU_CONFIG_KEY, {})

amqp_pub = AMQPPubStandaloneProxy(config=amqp_conf).as_inst()
# 衍生的常驻消费者线程将与启动应用时候首个进程(具体看服务器实现)共生死,所以无需release
amqp_rpc = AMQPRpcStandaloneProxy(config=amqp_conf, drain_events_timeout=None).as_inst()
