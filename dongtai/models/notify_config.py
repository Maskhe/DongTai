#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: owefsad@huoxian.cn
# datetime: 2021/5/6 下午2:34
# project: dongtai-models
from django.db import models

from dongtai.models import User
from dongtai.utils.settings import get_managed

WEB_HOOK = 1
GITLAB = 2
JIRA = 3
ZENDAO = 4
FEISHU = 5
WEIXIN = 6
DING_DING = 7



NOTIFY_TYPE_CHOICES = (
    (WEB_HOOK, WEB_HOOK),
    (GITLAB, GITLAB),
    (JIRA, JIRA),
    (ZENDAO, ZENDAO),
    (FEISHU, FEISHU),
    (WEIXIN, WEIXIN),
    (DING_DING, DING_DING),
)


class IastNotifyConfig(models.Model):
    WEB_HOOK = WEB_HOOK
    DING_DING = DING_DING
    FEISHU = FEISHU
    WEIXIN = WEIXIN
    NOTIFY_TYPE_CHOICES = NOTIFY_TYPE_CHOICES

    notify_type = models.SmallIntegerField(blank=True, null=True, choices=NOTIFY_TYPE_CHOICES)
    notify_meta_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING, blank=True, null=True)
    test_result = models.SmallIntegerField(blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = get_managed()
        db_table = 'iast_notify_config'
