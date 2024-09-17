# SPDX-FileCopyrightText: 2020 PANGAEA (https://www.pangaea.de/)
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from datetime import date, datetime  # noqa: F401

from fuji_server import util
from fuji_server.models.base_model_ import Model


class VersionIdentifierOutput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self):
        """VersionIdentifierOutput - a model defined in Swagger"""
        self.swagger_types = {}

        self.attribute_map = {}

    @classmethod
    def from_dict(cls, dikt) -> "VersionIdentifierOutput":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VersionIdentifier_output of this VersionIdentifierOutput.  # noqa: E501
        :rtype: VersionIdentifierOutput
        """
        return util.deserialize_model(dikt, cls)