# etoro-api
The User API provides data on a user including trading statistics

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import etoro_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import etoro_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import etoro_api
from etoro_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we want to get the aggregate data on
period = 'SixMonthsAgo' # str | The name of the period which we would like to get aggregate data on. The possible values are according to the period name in the metadata <a href=\"docs/services/5784e8446361c811ccfdf536/operations/578501516361c811ccfdf53c\">StatsPeriods API</a> (optional) (default to SixMonthsAgo)

try:
    # Trade/History/Aggregates
    api_instance.get_aggregates_history(username, period=period)
except ApiException as e:
    print("Exception when calling DefaultApi->get_aggregates_history: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which I would like to get the copier history
min_date = 'min_date_example' # str | The minimum date for the response. The date should be formatted as YYYY/MM/DD (optional)

try:
    # Copiers/History
    api_instance.get_copiers_history(username, min_date=min_date)
except ApiException as e:
    print("Exception when calling DefaultApi->get_copiers_history: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username to simulate
period = 'SixMonthsAgo' # str | The name of the period which we would like to get simulation data on. The possible values are according to the period name in the metadata <a href=\"docs/services/5784e8446361c811ccfdf536/operations/578501516361c811ccfdf53c\">StatsPeriods API</a> (default to SixMonthsAgo)
asset_allocation = true # bool | Return information on daily asset allocation (optional)

try:
    # CopySimulation
    api_instance.get_copy_simulation_data(username, period, asset_allocation=asset_allocation)
except ApiException as e:
    print("Exception when calling DefaultApi->get_copy_simulation_data: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we would like to get the gain information
type = 'Daily' # str | Type of data returned (default to Daily)
min_date = 'min_date_example' # str | The minimum date of the query. The date should be formatted as YYYY-MM-DD
max_date = 'max_date_example' # str | The maximum date of the query. The date should be formatted as YYYY-MM-DD

try:
    # Daily Gain
    api_instance.get_daily_gain(username, type, min_date, max_date)
except ApiException as e:
    print("Exception when calling DefaultApi->get_daily_gain: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we would like to get the gain information

try:
    # Monthly Gain
    api_instance.get_gains(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_gains: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we are trying to get the copiers

try:
    # Copiers/Live
    api_instance.get_live_copiers(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_live_copiers: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we would like to get the risk score information

try:
    # RiskScore/Live
    api_instance.get_live_risk_score(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_live_risk_score: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we would like to get the risk score information
min_date = 'min_date_example' # str | The minimum date to return information (optional)

try:
    # RiskScore/History
    api_instance.get_risk_history(username, min_date=min_date)
except ApiException as e:
    print("Exception when calling DefaultApi->get_risk_history: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | 
period = 'SixMonthsAgo' # str | Requested Period (optional) (default to SixMonthsAgo)

try:
    # Discovery
    api_instance.get_user_discovery_data(username, period=period)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_discovery_data: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we want to query

try:
    # Social/Followers
    api_instance.get_user_followers(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_followers: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The username which we would like to get the information

try:
    # Info
    api_instance.get_user_info(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_info: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The requested username

try:
    # PortfolioSummary
    api_instance.get_user_portfolio_summary(username)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_portfolio_summary: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
username = 'username_example' # str | The requested username
top = 1.2 # float | The number of results to return

try:
    # VisualPortfolio
    api_instance.get_user_visual_portfolio(username, top)
except ApiException as e:
    print("Exception when calling DefaultApi->get_user_visual_portfolio: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
usernames = 'usernames_example' # str | A comma delimited list of usernames which I would like to get discovery data
period = 'SixMonthsAgo' # str | Requested Period (default to SixMonthsAgo)
fields = 'fields_example' # str | A comma delimited list of fields which should be returned (optional)

try:
    # Multiple Discovery
    api_instance.get_users_discovery_data(usernames, period, fields=fields)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_discovery_data: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
user_names = 'user_names_example' # str | A comma delimited list of usernames (optional)

try:
    # Multiple Info
    api_instance.get_users_info(user_names=user_names)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_info: %s\n" % e)

# Configure API key authorization: apiKeyHeader
configuration = etoro_api.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: apiKeyQuery
configuration = etoro_api.Configuration()
configuration.api_key['subscription-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['subscription-key'] = 'Bearer'

# create an instance of the API class
api_instance = etoro_api.DefaultApi(etoro_api.ApiClient(configuration))
user_names = 'user_names_example' # str | A comma delimited list of usernames (optional)

try:
    # Multiple Visual Portfolio
    api_instance.get_users_visual_portfolio(user_names=user_names)
except ApiException as e:
    print("Exception when calling DefaultApi->get_users_visual_portfolio: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.etoro.com/API/User/V1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_aggregates_history**](docs/DefaultApi.md#get_aggregates_history) | **GET** /{Username}/Trade/History/Aggregates | Trade/History/Aggregates
*DefaultApi* | [**get_copiers_history**](docs/DefaultApi.md#get_copiers_history) | **GET** /{Username}/Copiers/History | Copiers/History
*DefaultApi* | [**get_copy_simulation_data**](docs/DefaultApi.md#get_copy_simulation_data) | **GET** /{Username}/CopySimulation | CopySimulation
*DefaultApi* | [**get_daily_gain**](docs/DefaultApi.md#get_daily_gain) | **GET** /{Username}/DailyGain | Daily Gain
*DefaultApi* | [**get_gains**](docs/DefaultApi.md#get_gains) | **GET** /{Username}/Gain | Monthly Gain
*DefaultApi* | [**get_live_copiers**](docs/DefaultApi.md#get_live_copiers) | **GET** /{Username}/Copiers/Live | Copiers/Live
*DefaultApi* | [**get_live_risk_score**](docs/DefaultApi.md#get_live_risk_score) | **GET** /{Username}/RiskScore/Live/ | RiskScore/Live
*DefaultApi* | [**get_risk_history**](docs/DefaultApi.md#get_risk_history) | **GET** /{Username}/RiskScore/History | RiskScore/History
*DefaultApi* | [**get_user_discovery_data**](docs/DefaultApi.md#get_user_discovery_data) | **GET** /{Username}/Discovery | Discovery
*DefaultApi* | [**get_user_followers**](docs/DefaultApi.md#get_user_followers) | **GET** /{Username}/Social/Followers | Social/Followers
*DefaultApi* | [**get_user_info**](docs/DefaultApi.md#get_user_info) | **GET** /{Username}/Info | Info
*DefaultApi* | [**get_user_portfolio_summary**](docs/DefaultApi.md#get_user_portfolio_summary) | **GET** /{Username}/PortfolioSummary | PortfolioSummary
*DefaultApi* | [**get_user_visual_portfolio**](docs/DefaultApi.md#get_user_visual_portfolio) | **GET** /{Username}/VisualPortfolio | VisualPortfolio
*DefaultApi* | [**get_users_discovery_data**](docs/DefaultApi.md#get_users_discovery_data) | **GET** /Multiple/Discovery | Multiple Discovery
*DefaultApi* | [**get_users_info**](docs/DefaultApi.md#get_users_info) | **GET** /Multiple/Info | Multiple Info
*DefaultApi* | [**get_users_visual_portfolio**](docs/DefaultApi.md#get_users_visual_portfolio) | **GET** /Multiple/VisualPortfolio | Multiple Visual Portfolio

## Documentation For Models


## Documentation For Authorization


## apiKeyHeader

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

## apiKeyQuery

- **Type**: API key
- **API key parameter name**: subscription-key
- **Location**: URL query string


## Author

