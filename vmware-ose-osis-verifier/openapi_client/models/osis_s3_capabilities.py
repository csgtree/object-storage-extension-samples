# coding: utf-8

"""
    Object Storage Interoperability Services API

    This is VMware Cloud Director Object Storage Interoperability Services API. Once storage platform vendor implements REST APIs complying with this specification, Object Storage Extension can integrate with the platform without coding effort.  # noqa: E501

    The version of the OpenAPI document: 1.0.0-oas3
    Contact: wachen@vmware.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class OsisS3Capabilities(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'exclusions': 'dict(str, OsisS3CapabilitiesExclusions)'
    }

    attribute_map = {
        'exclusions': 'exclusions'
    }

    def __init__(self, exclusions=None, local_vars_configuration=None):  # noqa: E501
        """OsisS3Capabilities - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._exclusions = None
        self.discriminator = None

        if exclusions is not None:
            self.exclusions = exclusions

    @property
    def exclusions(self):
        """Gets the exclusions of this OsisS3Capabilities.  # noqa: E501

        return the S3 API code which is not supported by the storage platform; the API code complies with https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html  # noqa: E501

        :return: The exclusions of this OsisS3Capabilities.  # noqa: E501
        :rtype: dict(str, OsisS3CapabilitiesExclusions)
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """Sets the exclusions of this OsisS3Capabilities.

        return the S3 API code which is not supported by the storage platform; the API code complies with https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html  # noqa: E501

        :param exclusions: The exclusions of this OsisS3Capabilities.  # noqa: E501
        :type: dict(str, OsisS3CapabilitiesExclusions)
        """

        self._exclusions = exclusions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OsisS3Capabilities):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OsisS3Capabilities):
            return True

        return self.to_dict() != other.to_dict()
