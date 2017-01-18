from __future__ import print_function, absolute_import, unicode_literals, division

import unittest2 as unittest
import os
import re
from local import execute_command
from rds_log_dog.cfn_utils import cfn_get_output
import rds_log_dog.s3_utils


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        with open('target/DST_BUCKET_STACK_NAME', 'r') as f:
            self.bucket_stack_name = f.read().strip()

        self.bucket_name = cfn_get_output(self.bucket_stack_name, 'name')

    def test_s3_rds_logs_dst_exists(self):
        folder_result = rds_log_dog.s3_utils.list_folders(
            self.bucket_name, 'rds_logs')
        self.assertEqual(1, len(folder_result), "rds_log/ not found")

if __name__ == '__main__':
    unittest.main()
