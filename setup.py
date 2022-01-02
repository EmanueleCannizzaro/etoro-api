# coding: utf-8

"""
    eToro API
    eToro Metadata API
    eToro Rates API
	User

    The discovery API allows you to discover customers in the eToro network. It is important to note that only customers who have opted-in for discovery will be shown by this API  # noqa: E501
    The metadata API provides basic meta data for the eToro system. The metadata is comprised of reference tables for all the other end-points in this API  # noqa: E501
    The Rates API provides eToro live and historical rates  # noqa: E501	
    The System API provides general data on the full eToro System  # noqa: E501
    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501
	The User API provides data on a user including trading statistics  # noqa: E501
	
    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "etoro"
VERSION = "0.6.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="eToro API",
    author_email="",
    url="https://github.com/ecannizzaro/etoro/",
    keywords=["Swagger", "Discovery", "Metadata", "Rates", "System", "Trading", "User"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    The discovery API allows you to discover customers in the eToro network. It is important to note that only customers who have opted-in for discovery will be shown by this API  # noqa: E501
    The metadata API provides basic meta data for the eToro system. The metadata is comprised of reference tables for all the other end-points in this API  # noqa: E501
    The Rates API provides eToro live and historical rates  # noqa: E501
    The System API provides general data on the full eToro System  # noqa: E501
    The Trading API allows the development of the full trading capabilities in the eToro platform  # noqa: E501
    The User API provides data on a user including trading statistics  # noqa: E501
    """
)