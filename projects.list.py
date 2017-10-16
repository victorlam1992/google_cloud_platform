from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

request = service.projects().list()
while request is not None:
    response = request.execute()

    for project in response['projects']:
        # TODO: Change code below to process each `project` resource:
        pprint(project)

    request = service.projects().list_next(previous_request=request, previous_response=response)
	
#==============================================
"""
Result:
	{'createTime': '2017-10-16T03:05:43.851Z',
	 'lifecycleState': 'DELETE_REQUESTED',
	 'name': 'Oxford-IIIT Pets',
	 'projectId': 'ornate-ensign-183103',
	 'projectNumber': '54890597624'}
	{'createTime': '2017-10-16T03:05:27.884Z',
	 'lifecycleState': 'ACTIVE',
	 'name': 'Oxford-IIIT Pets',
	 'projectId': 'oxford-iiit-pets-183103',
	 'projectNumber': '493151018659'}
	{'createTime': '2016-12-19T09:37:40.466Z',
	 'lifecycleState': 'ACTIVE',
	 'name': 'My Project',
	 'projectId': 'psyched-spark-153009',
	 'projectNumber': '1070136778506'}
"""
#==============================================
