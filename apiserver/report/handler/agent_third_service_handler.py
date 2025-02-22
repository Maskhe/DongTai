######################################################################
# @author      : bidaya0 (bidaya0@$HOSTNAME)
# @file        : api_route_handler
# @created     : Tuesday Aug 17, 2021 19:59:29 CST
#
# @description :
######################################################################

from apiserver.report.handler.report_handler_interface import IReportHandler
from apiserver.report.report_handler_factory import ReportHandler
from dongtai.models.api_route import IastApiRoute, IastApiMethod, \
        IastApiResponse, IastApiParameter, \
        IastApiMethodHttpMethodRelation, HttpMethod
from dongtai.models.agent import IastAgent
from dongtai.utils import const
import logging
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from dongtai.models.project import IastProject
from dongtai.models.agent_thirdservice import IastThirdPartyService
logger = logging.getLogger('dongtai.openapi')


@ReportHandler.register(const.REPORT_THIRD_PARTY_SERVICE)
class ThirdPartyServiceHandler(IReportHandler):

    def parse(self):
        self.service_data = self.detail.get('serviceData')

    def save(self):
        try:
            agent = IastAgent.objects.filter(pk=self.agent_id)[0:1]
            if not agent:
                raise ValueError(_("No such agent"))
            agent = agent[0]
            third_party_models = _data_dump(self.service_data, self.agent_id,
                                            agent.bind_project_id)
            IastThirdPartyService.objects.bulk_create(third_party_models,
                                                      ignore_conflicts=True)
        except Exception as e:
            logger.info(_('third log failed, why: {}').format(e))


def _data_dump(items, agent_id: int, project_id: int):
    return (IastThirdPartyService(agent_id=agent_id,
                                  project_id=project_id,
                                  address=item['address'],
                                  service_type=item['serviceType'],
                                  port=item['port']) for item in items)
