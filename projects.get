```python
from pprint import pprint

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

credentials = GoogleCredentials.get_application_default()

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

# The Project ID (for example, `my-project-123`).
# Required.
project_id = 'my-project-id'  # TODO: Update placeholder value.

request = service.projects().get(projectId=project_id)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)

```
