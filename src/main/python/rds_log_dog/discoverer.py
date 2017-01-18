from __future__ import print_function, absolute_import, unicode_literals, division

import boto3
from .rds_instance import RDSInstance
from .config import get_logger

logger = get_logger(__name__)


class Discoverer(object):

    def __init__(self):
        pass

    def discover(self):
        client = boto3.client('rds')
        response = client.describe_db_instances()
        return [RDSInstance(i['DBInstanceIdentifier']) for i in response['DBInstances']]
