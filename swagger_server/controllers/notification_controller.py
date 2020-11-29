import connexion
import six
from flask import jsonify

from swagger_server.models.notification import Notification  # noqa: E501
from swagger_server.models.one_notification import OneNotification  # noqa: E501
from swagger_server import util

from swagger_server.static.constants import *


def send_notification_all(visit):  # noqa: E501
    """Send notification to all the people close to the user

    Send notification to all the people close to the user # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    known_visitor = ""
    if connexion.request.is_json:
        visit = Notification.from_dict(connexion.request.get_json())  # noqa: E501
        if visit.known:
            known_visitor = 'known and his/her name is ' + visit.name
        else:
            known_visitor = 'not known'
    return jsonify({"message": MESSAGE_TO_ALL_LEGITIMATE_PERSON.format(known_visitor)})


def send_notification_one_person(visit):  # noqa: E501
    """Send notification to one relative of the user

    Send notification to one relative of the user # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: str
    """
    known_visitor = ""
    if connexion.request.is_json:
        visit = OneNotification.from_dict(connexion.request.get_json())  # noqa: E501
        if visit.known:
            known_visitor = 'known and his/her name is ' + visit.name
        else:
            known_visitor = 'not known'
    return jsonify({"message": MESSAGE_TO_ONE_LEGITIMATE_PERSON.format(visit.person_phone, known_visitor)})


def send_notification_user(visit):  # noqa: E501
    """Send notification to the user

    Send notification to the user # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: str
    """
    known_visitor = ""
    if connexion.request.is_json:
        visit = Notification.from_dict(connexion.request.get_json())  # noqa: E501
        if visit.known:
            known_visitor = 'known and his/her name is ' + visit.name
        else:
            known_visitor = 'not known'
    return jsonify({"message": MESSAGE_TO_USER.format(known_visitor)})
