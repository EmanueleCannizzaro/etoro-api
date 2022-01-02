# coding: utf-8

"""
    eToro System API

    The System API provides general data on the full eToro System  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from etoro_system.api_client import ApiClient


class System_Configuration(Configuration):
    def __init__(self):
        self.host = "https://api.etoro.com/System/V1"
        self.logger["package_logger"] = logging.getLogger("etoro_system")


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_auto_complete(self, prefix, instrument_count, user_count, **kwargs):  # noqa: E501
        """Auto-Complete  # noqa: E501

        The auto-complete method allows you to create an \"auto-complete\" like widget with both users and instruments in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_complete(prefix, instrument_count, user_count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: The search term you will be executing (required)
        :param float instrument_count: The number of instruments in the result set (required)
        :param float user_count: The number of users in the result set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_auto_complete_with_http_info(prefix, instrument_count, user_count, **kwargs)  # noqa: E501
        else:
            (data) = self.get_auto_complete_with_http_info(prefix, instrument_count, user_count, **kwargs)  # noqa: E501
            return data

    def get_auto_complete_with_http_info(self, prefix, instrument_count, user_count, **kwargs):  # noqa: E501
        """Auto-Complete  # noqa: E501

        The auto-complete method allows you to create an \"auto-complete\" like widget with both users and instruments in the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_auto_complete_with_http_info(prefix, instrument_count, user_count, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str prefix: The search term you will be executing (required)
        :param float instrument_count: The number of instruments in the result set (required)
        :param float user_count: The number of users in the result set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prefix', 'instrument_count', 'user_count']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_auto_complete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prefix' is set
        if ('prefix' not in params or
                params['prefix'] is None):
            raise ValueError("Missing the required parameter `prefix` when calling `get_auto_complete`")  # noqa: E501
        # verify the required parameter 'instrument_count' is set
        if ('instrument_count' not in params or
                params['instrument_count'] is None):
            raise ValueError("Missing the required parameter `instrument_count` when calling `get_auto_complete`")  # noqa: E501
        # verify the required parameter 'user_count' is set
        if ('user_count' not in params or
                params['user_count'] is None):
            raise ValueError("Missing the required parameter `user_count` when calling `get_auto_complete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'prefix' in params:
            query_params.append(('Prefix', params['prefix']))  # noqa: E501
        if 'instrument_count' in params:
            query_params.append(('InstrumentCount', params['instrument_count']))  # noqa: E501
        if 'user_count' in params:
            query_params.append(('UserCount', params['user_count']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/AutoComplete', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_daily_price_change(self, sort, **kwargs):  # noqa: E501
        """Daily Price Change  # noqa: E501

        The daily price change method shows the daily price change of the instruments in the system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_daily_price_change(sort, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The order of the response regarding the daily change (required)
        :param float page: The current page. If omitted the default will be the first page
        :param float page_size: The number of results in each page. If omitted, the page size will default to 20
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_daily_price_change_with_http_info(sort, **kwargs)  # noqa: E501
        else:
            (data) = self.get_daily_price_change_with_http_info(sort, **kwargs)  # noqa: E501
            return data

    def get_daily_price_change_with_http_info(self, sort, **kwargs):  # noqa: E501
        """Daily Price Change  # noqa: E501

        The daily price change method shows the daily price change of the instruments in the system.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_daily_price_change_with_http_info(sort, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sort: The order of the response regarding the daily change (required)
        :param float page: The current page. If omitted the default will be the first page
        :param float page_size: The number of results in each page. If omitted, the page size will default to 20
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sort', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_daily_price_change" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sort' is set
        if ('sort' not in params or
                params['sort'] is None):
            raise ValueError("Missing the required parameter `sort` when calling `get_daily_price_change`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sort' in params:
            query_params.append(('Sort', params['sort']))  # noqa: E501
        if 'page' in params:
            query_params.append(('Page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('PageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/DailyPriceChange', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_insights(self, insight_type, **kwargs):  # noqa: E501
        """Insights  # noqa: E501

        The Insights method provides an insight on the trends inside the eToro system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_insights(insight_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str insight_type: What type of insight we wish to see (required)
        :param str instrument_ids: Comma delimited string containing instrument ids which will be explicitly returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_insights_with_http_info(insight_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_insights_with_http_info(insight_type, **kwargs)  # noqa: E501
            return data

    def get_insights_with_http_info(self, insight_type, **kwargs):  # noqa: E501
        """Insights  # noqa: E501

        The Insights method provides an insight on the trends inside the eToro system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_insights_with_http_info(insight_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str insight_type: What type of insight we wish to see (required)
        :param str instrument_ids: Comma delimited string containing instrument ids which will be explicitly returned
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['insight_type', 'instrument_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_insights" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'insight_type' is set
        if ('insight_type' not in params or
                params['insight_type'] is None):
            raise ValueError("Missing the required parameter `insight_type` when calling `get_insights`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'insight_type' in params:
            path_params['InsightType'] = params['insight_type']  # noqa: E501

        query_params = []
        if 'instrument_ids' in params:
            query_params.append(('InstrumentIds', params['instrument_ids']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/Insights/{InsightType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_market_events(self, **kwargs):  # noqa: E501
        """Market Events  # noqa: E501

        The Market Events method returns information on significant market events.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str min_date: Minimum date for events. In case it is omitted it will be 10 days
        :param str max_date: Maximum date for events. In case it is missing the current timestamp will be used
        :param float page: The current page. If omitted the default will by 1
        :param float page_size: The pagesize. If omitted the default page size will be 10
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_market_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_market_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_market_events_with_http_info(self, **kwargs):  # noqa: E501
        """Market Events  # noqa: E501

        The Market Events method returns information on significant market events.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_market_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str min_date: Minimum date for events. In case it is omitted it will be 10 days
        :param str max_date: Maximum date for events. In case it is missing the current timestamp will be used
        :param float page: The current page. If omitted the default will by 1
        :param float page_size: The pagesize. If omitted the default page size will be 10
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['min_date', 'max_date', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_market_events" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'min_date' in params:
            query_params.append(('MinDate', params['min_date']))  # noqa: E501
        if 'max_date' in params:
            query_params.append(('MaxDate', params['max_date']))  # noqa: E501
        if 'page' in params:
            query_params.append(('Page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('PageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyHeader', 'apiKeyQuery']  # noqa: E501

        return self.api_client.call_api(
            '/MarketEvents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)