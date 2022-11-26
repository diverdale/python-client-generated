# coding: utf-8

"""
    IMDb-API

    The IMDb-API Documentation. You need a <a href='/Identity/Account/Manage' target='_blank'><code>API Key</code></a> for testing APIs.<br/><a class='link' href='/API'>Back to API Tester</a>  # noqa: E501

    OpenAPI spec version: 1.8.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserRatingDataDemographic(object):
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
        'all_ages': 'UserRatingDataDemographicDetail',
        'ages_under18': 'UserRatingDataDemographicDetail',
        'ages18_to29': 'UserRatingDataDemographicDetail',
        'ages30_to44': 'UserRatingDataDemographicDetail',
        'ages_over45': 'UserRatingDataDemographicDetail'
    }

    attribute_map = {
        'all_ages': 'allAges',
        'ages_under18': 'agesUnder18',
        'ages18_to29': 'ages18To29',
        'ages30_to44': 'ages30To44',
        'ages_over45': 'agesOver45'
    }

    def __init__(self, all_ages=None, ages_under18=None, ages18_to29=None, ages30_to44=None, ages_over45=None):  # noqa: E501
        """UserRatingDataDemographic - a model defined in Swagger"""  # noqa: E501
        self._all_ages = None
        self._ages_under18 = None
        self._ages18_to29 = None
        self._ages30_to44 = None
        self._ages_over45 = None
        self.discriminator = None
        if all_ages is not None:
            self.all_ages = all_ages
        if ages_under18 is not None:
            self.ages_under18 = ages_under18
        if ages18_to29 is not None:
            self.ages18_to29 = ages18_to29
        if ages30_to44 is not None:
            self.ages30_to44 = ages30_to44
        if ages_over45 is not None:
            self.ages_over45 = ages_over45

    @property
    def all_ages(self):
        """Gets the all_ages of this UserRatingDataDemographic.  # noqa: E501


        :return: The all_ages of this UserRatingDataDemographic.  # noqa: E501
        :rtype: UserRatingDataDemographicDetail
        """
        return self._all_ages

    @all_ages.setter
    def all_ages(self, all_ages):
        """Sets the all_ages of this UserRatingDataDemographic.


        :param all_ages: The all_ages of this UserRatingDataDemographic.  # noqa: E501
        :type: UserRatingDataDemographicDetail
        """

        self._all_ages = all_ages

    @property
    def ages_under18(self):
        """Gets the ages_under18 of this UserRatingDataDemographic.  # noqa: E501


        :return: The ages_under18 of this UserRatingDataDemographic.  # noqa: E501
        :rtype: UserRatingDataDemographicDetail
        """
        return self._ages_under18

    @ages_under18.setter
    def ages_under18(self, ages_under18):
        """Sets the ages_under18 of this UserRatingDataDemographic.


        :param ages_under18: The ages_under18 of this UserRatingDataDemographic.  # noqa: E501
        :type: UserRatingDataDemographicDetail
        """

        self._ages_under18 = ages_under18

    @property
    def ages18_to29(self):
        """Gets the ages18_to29 of this UserRatingDataDemographic.  # noqa: E501


        :return: The ages18_to29 of this UserRatingDataDemographic.  # noqa: E501
        :rtype: UserRatingDataDemographicDetail
        """
        return self._ages18_to29

    @ages18_to29.setter
    def ages18_to29(self, ages18_to29):
        """Sets the ages18_to29 of this UserRatingDataDemographic.


        :param ages18_to29: The ages18_to29 of this UserRatingDataDemographic.  # noqa: E501
        :type: UserRatingDataDemographicDetail
        """

        self._ages18_to29 = ages18_to29

    @property
    def ages30_to44(self):
        """Gets the ages30_to44 of this UserRatingDataDemographic.  # noqa: E501


        :return: The ages30_to44 of this UserRatingDataDemographic.  # noqa: E501
        :rtype: UserRatingDataDemographicDetail
        """
        return self._ages30_to44

    @ages30_to44.setter
    def ages30_to44(self, ages30_to44):
        """Sets the ages30_to44 of this UserRatingDataDemographic.


        :param ages30_to44: The ages30_to44 of this UserRatingDataDemographic.  # noqa: E501
        :type: UserRatingDataDemographicDetail
        """

        self._ages30_to44 = ages30_to44

    @property
    def ages_over45(self):
        """Gets the ages_over45 of this UserRatingDataDemographic.  # noqa: E501


        :return: The ages_over45 of this UserRatingDataDemographic.  # noqa: E501
        :rtype: UserRatingDataDemographicDetail
        """
        return self._ages_over45

    @ages_over45.setter
    def ages_over45(self, ages_over45):
        """Sets the ages_over45 of this UserRatingDataDemographic.


        :param ages_over45: The ages_over45 of this UserRatingDataDemographic.  # noqa: E501
        :type: UserRatingDataDemographicDetail
        """

        self._ages_over45 = ages_over45

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
        if issubclass(UserRatingDataDemographic, dict):
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
        if not isinstance(other, UserRatingDataDemographic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
