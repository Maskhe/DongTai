#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:owefsad
# software: PyCharm
# project: lingzhi-webapi
import time
from dongtai.endpoint import R
from dongtai.endpoint import UserEndPoint
from dongtai.models.agent import IastAgent
from dongtai.models.project import IastProject
from dongtai.models.vul_level import IastVulLevel
from dongtai.models.vulnerablity import IastVulnerabilityModel
from iast.base.project_version import get_project_version, get_project_version_by_id, ProjectsVersionDataSerializer
from django.utils.translation import gettext_lazy as _
from dongtai.models.vulnerablity import IastVulnerabilityStatus
from iast.serializers.project import ProjectSerializer
from dongtai.models.hook_type import HookType
from django.db.models import Q
from rest_framework import serializers
from iast.utils import extend_schema_with_envcheck, get_response_serializer
from dongtai.models.strategy import IastStrategyModel
from iast.views.utils.commonstats import get_summary_by_agent_ids
from dongtai.utils import const

class ProjectSummaryQuerySerializer(serializers.Serializer):
    version_id = serializers.CharField(
        help_text=_("The version id of the project"))


class ProjectSummaryDataTypeSummarySerializer(serializers.Serializer):
    type_name = serializers.CharField(help_text=_("Name of vulnerability"))
    type_count = serializers.IntegerField(
        help_text=_("Count of thi vulnerablity type"))
    type_level = serializers.IntegerField(
        help_text=_("Level of vulnerability"))


class ProjectSummaryDataDayNumSerializer(serializers.Serializer):
    day_label = serializers.CharField(help_text=_('Timestamp, format %M-%d'))
    day_num = serializers.IntegerField(
        help_text=_('The number of vulnerabilities corresponding to the time'))


class ProjectSummaryDataLevelCountSerializer(serializers.Serializer):
    level_name = serializers.CharField(
        help_text=_('Level name of vulnerability'))
    level_id = serializers.IntegerField(
        help_text=_('Level id of vulnerability'))
    num = serializers.IntegerField(help_text=_(
        'The number of vulnerabilities corresponding to the level'))


class _ProjectSummaryDataSerializer(serializers.Serializer):
    name = serializers.CharField(help_text=_('The name of project'))
    mode = serializers.ChoiceField(['插桩模式'],
                                   help_text=_('The mode of project'))
    id = serializers.IntegerField(help_text=_("The id of the project"))
    latest_time = serializers.IntegerField(help_text=_("The latest update time of the project"))
    versionData = ProjectsVersionDataSerializer(
        help_text=_('Version information about the project'))
    type_summary = ProjectSummaryDataTypeSummarySerializer(
        many=True,
        help_text=_('Statistics on the number of types of vulnerabilities'))
    agent_language = serializers.ListField(
        child=serializers.CharField(),
        help_text=_("Agent language currently included in the project"))
    level_count = ProjectSummaryDataLevelCountSerializer(
        many=True,
        help_text=_(
            "Statistics on the number of danger levels of vulnerabilities"))


_ProjectSummaryResponseSerializer = get_response_serializer(
    _ProjectSummaryDataSerializer())


class ProjectSummary(UserEndPoint):
    name = "api-v1-project-summary-<id>"
    description = _("Item details - Summary")

    @staticmethod
    def weeks_ago(week=1):

        weekend = 7 * week
        current_timestamp = int(time.time())
        weekend_ago_time = time.localtime(current_timestamp - 86400 * weekend)
        weekend_ago_time_str = str(weekend_ago_time.tm_year) + "-" + str(weekend_ago_time.tm_mon) + "-" + str(
            weekend_ago_time.tm_mday) + " 00:00:00"
        beginArray = time.strptime(weekend_ago_time_str, "%Y-%m-%d %H:%M:%S")

        beginT = int(time.mktime(beginArray))
        return current_timestamp, beginT, weekend

    @extend_schema_with_envcheck(
        tags=[_('Project')],
        summary=_('Projects Summary'),
        description=
        _("Get project deatils and its statistics data about vulnerablity."
          ),
        response_schema=_ProjectSummaryResponseSerializer,
    )
    def get(self, request, id):
        auth_users = self.get_auth_users(request.user)
        project = IastProject.objects.filter(user__in=auth_users,
                                             id=id).first()

        if not project:
            return R.failure(status=203, msg=_('no permission'))
        version_id = request.GET.get('version_id', None)
        data = dict()
        data['owner'] = project.user.get_username()
        data['name'] = project.name
        data['id'] = project.id
        data['mode'] = project.mode
        data['latest_time'] = project.latest_time
        data['type_summary'] = []
        data['day_num'] = []
        data['level_count'] = []

        if not version_id:
            current_project_version = get_project_version(
                project.id, auth_users)
        else:
            current_project_version = get_project_version_by_id(version_id)
        data['versionData'] = current_project_version
        relations = IastAgent.objects.filter(
            user__in=auth_users,
            bind_project_id=project.id,
            project_version_id=current_project_version.get("version_id", 0)
        ).values("id")

        agent_ids = [relation['id'] for relation in relations]
        agent_id = request.query_params.get('agent_id')
        if agent_id:
            agent_ids = [agent_id]
        data_stat = get_summary_by_agent_ids(agent_ids)
        data.update(data_stat)
        data['agent_language'] = ProjectSerializer(
            project).data['agent_language']
        data['agent_alive'] = IastAgent.objects.filter(
            bind_project_id=project.id, online=const.RUNNING).count()
        return R.success(data=data)
