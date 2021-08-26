import requests
from pprint import pprint
from auth_data import api_key, project_id

base_url = 'https://cloud.roistat.com/api/v1/'
auth_ = f'?key={api_key}&project={project_id}'

analytics_data = 'project/analytics/data'
dimensions = 'project/analytics/dimensions'
metrics = 'project/analytics/metrics'

params = {
  "dimensions": ["marker_level_1"],
  "metrics": ["marketing_cost", "visitsCost"],
  "period": {
    "from":"2021-07-26T00:00:00+0300",
    "to":"2021-08-25T23:59:59+0300"
  }
}

# url = f'{base_url}project/analytics/data{auth_}'
url = f'{base_url}{analytics_data}{auth_}'
response = requests.post(url=url, json=params)
# pprint(response.json())
channels = response.json()['data'][0]['items']
# pprint(channels[0])
with open('channels.txt', 'w', encoding='utf-8') as f,\
     open('channels_.txt', 'w', encoding='utf-8') as f_:
    for i in range(len(channels)):
        f.write(channels[i]['dimensions']['marker_level_1']['title'].replace(u'\xa0', ' ') + ': ' +\
                str(channels[i]['metrics'][0]['value']) + '\n')
        if channels[i]['metrics'][0]['value'] != 0:
            f_.write(channels[i]['dimensions']['marker_level_1']['title'].replace(u'\xa0', ' ') + ': ' + \
                str(channels[i]['metrics'][0]['value']) + '\n')
        pprint(channels[i]['dimensions']['marker_level_1']['title'])