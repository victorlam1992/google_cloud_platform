# google_cloud_platform

## Create the Projects in Google Cloud

https://console.cloud.google.com/cloud-resource-manager?_ga=2.46029604.-1830551699.1508119907

## Enable the Google Cloud Resource Manager API

Click the link below:

https://console.developers.google.com/apis/api/cloudresourcemanager

Error may occur. Click the ```Dashboard``` at right-hand side, press ```Enable API```, Find out the ```Google Cloud Resource Manager API```. Enable it.

## Install Google Cloud SDK

Follow the link below to install the SDK:

https://cloud.google.com/sdk/docs/quickstart-windows

Run:

```gcloud beta auth application-default login``` at SDK command prompt.

## Install Python library for Google API

```pip install google-api-python-client```

## Enable Google Cloud Machine Learning Engine to your project

https://console.cloud.google.com/flows/enableapi?apiid=ml.googleapis.com,compute_component&_ga=1.73374291.1570145678.1496689256

If error, follow the Google Cloud Resource Manager API Step.

## Set up a Google Cloud Storage (GCS) bucket

Create a new bucket:

https://cloud.google.com/storage/docs/creating-buckets

ML Engine training jobs can only access files on a Google Cloud Storage bucket. 

In this tutorial, we'll be required to upload our dataset and configuration to GCS.

Substitute ```${YOUR_GCS_BUCKET}``` with the name of your bucket in this document. For your convenience, you should define the environment variable below:

```export YOUR_GCS_BUCKET=${YOUR_GCS_BUCKET}```

## Important Links:

Creating and Managing Projects

https://cloud.google.com/resource-manager/docs/creating-managing-projects

API Library

https://console.cloud.google.com/apis/library?project=oxford-iiit-pets-183103
