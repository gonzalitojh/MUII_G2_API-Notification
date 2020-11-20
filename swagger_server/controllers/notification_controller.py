import connexion
import six

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.one_notification import OneNotification  # noqa: E501
from swagger_server import util


def send_notification_all(body):  # noqa: E501
    """Send notification to all the people close to the user

    Send notification to all the people close to the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_notification_one_person(body):  # noqa: E501
    """Send notification to one relative of the user

    Send notification to one relative of the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = OneNotification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def send_notification_user(body):  # noqa: E501
    """Send notification to the user

    Send notification to the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = Notification.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
