# coding: utf-8

"""
    Speech Services API v3.1

    Speech Services API v3.1.  # noqa: E501

    OpenAPI spec version: v3.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EndpointProperties(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'logging_enabled': 'bool',
        'time_to_live': 'str',
        'email': 'str',
        'error': 'EntityError'
    }

    attribute_map = {
        'logging_enabled': 'loggingEnabled',
        'time_to_live': 'timeToLive',
        'email': 'email',
        'error': 'error'
    }

    def __init__(self, logging_enabled=None, time_to_live=None, email=None, error=None, _configuration=None):  # noqa: E501
        """EndpointProperties - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._logging_enabled = None
        self._time_to_live = None
        self._email = None
        self._error = None
        self.discriminator = None

        if logging_enabled is not None:
            self.logging_enabled = logging_enabled
        if time_to_live is not None:
            self.time_to_live = time_to_live
        if email is not None:
            self.email = email
        if error is not None:
            self.error = error

    @property
    def logging_enabled(self):
        """Gets the logging_enabled of this EndpointProperties.  # noqa: E501

        A value indicating whether content logging (audio & transcriptions) is being used for a deployment.  # noqa: E501

        :return: The logging_enabled of this EndpointProperties.  # noqa: E501
        :rtype: bool
        """
        return self._logging_enabled

    @logging_enabled.setter
    def logging_enabled(self, logging_enabled):
        """Sets the logging_enabled of this EndpointProperties.

        A value indicating whether content logging (audio & transcriptions) is being used for a deployment.  # noqa: E501

        :param logging_enabled: The logging_enabled of this EndpointProperties.  # noqa: E501
        :type: bool
        """

        self._logging_enabled = logging_enabled

    @property
    def time_to_live(self):
        """Gets the time_to_live of this EndpointProperties.  # noqa: E501

        How long the endpoint will be kept in the system. Once the endpoint reaches the time to live  after completion (successful or failed) it will be automatically deleted. Not setting this value or setting  to 0 will disable automatic deletion. The longest supported duration is 31 days.  The duration is encoded as ISO 8601 duration (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :return: The time_to_live of this EndpointProperties.  # noqa: E501
        :rtype: str
        """
        return self._time_to_live

    @time_to_live.setter
    def time_to_live(self, time_to_live):
        """Sets the time_to_live of this EndpointProperties.

        How long the endpoint will be kept in the system. Once the endpoint reaches the time to live  after completion (successful or failed) it will be automatically deleted. Not setting this value or setting  to 0 will disable automatic deletion. The longest supported duration is 31 days.  The duration is encoded as ISO 8601 duration (\"PnYnMnDTnHnMnS\", see https://en.wikipedia.org/wiki/ISO_8601#Durations).  # noqa: E501

        :param time_to_live: The time_to_live of this EndpointProperties.  # noqa: E501
        :type: str
        """

        self._time_to_live = time_to_live

    @property
    def email(self):
        """Gets the email of this EndpointProperties.  # noqa: E501

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :return: The email of this EndpointProperties.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this EndpointProperties.

        The email address to send email notifications to in case the operation completes.  The value will be removed after successfully sending the email.  # noqa: E501

        :param email: The email of this EndpointProperties.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def error(self):
        """Gets the error of this EndpointProperties.  # noqa: E501


        :return: The error of this EndpointProperties.  # noqa: E501
        :rtype: EntityError
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this EndpointProperties.


        :param error: The error of this EndpointProperties.  # noqa: E501
        :type: EntityError
        """

        self._error = error

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EndpointProperties, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EndpointProperties):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EndpointProperties):
            return True

        return self.to_dict() != other.to_dict()
