# coding: utf-8

from __future__ import absolute_import

from flask import json

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.one_notification import OneNotification  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificationController(BaseTestCase):
    """NotificationController integration test stubs"""

    def test_send_notification_all(self):
        """Test case for send_notification_all

        Send notification to all the people close to the user
        """
        body = Notification()
        response = self.client.open(
            '/notification',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_notification_one_person(self):
        """Test case for send_notification_one_person

        Send notification to one relative of the user
        """
        body = OneNotification()
        response = self.client.open(
            '/notification/legitimate_person',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_send_notification_user(self):
        """Test case for send_notification_user

        Send notification to the user
        """
        body = Notification()
        response = self.client.open(
            '/notification/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
