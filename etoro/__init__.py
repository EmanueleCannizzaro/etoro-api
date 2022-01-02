# coding: utf-8

# flake8: noqa

"""
    eToro Discovery API
    eToro Metadata API
    eToro Rates API	
    eToro Trading API
	User

    The Discovery API allows you to discover customers in the eToro network. It is important to note that only customers who have opted-in for discovery will be shown by this API  # noqa: E501
    The metadata API provides basic meta data for the eToro system. The metadata is comprised of reference tables for all the other end-points in this API  # noqa: E501
    The Rates API provides eToro live and historical rates  # noqa: E501
    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501
    The User API provides data on a user including trading statistics  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from etoro.discovery import Discovery
from etoro_metadata.api.default_api import DefaultApi
# import ApiClient
from etoro_metadata.api_client import ApiClient
from etoro_metadata.configuration import Configuration
from etoro_rates.api.default_api import DefaultApi
# import ApiClient
from etoro_rates.api_client import ApiClient
from etoro_rates.configuration import Configuration

from etoro.system import System
from etoro.trading import Trading
from etoro_user.api.default_api import DefaultApi
# import ApiClient
from etoro_user.api_client import ApiClient
from etoro_user.configuration import Configuration
# import ApiClient
#from etoro_discovery.api_client import ApiClient
#from etoro_discovery.configuration import Configuration
# import models into sdk package
