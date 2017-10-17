# Quick Start: Distributed Training on the Oxford-IIIT Pets Dataset on Google Cloud

## Download the Oxford-IIIT Pets Dataset

http://www.robots.ox.ac.uk/%7Evgg/data/pets/

download both the **image dataset** ```images.tar.gz``` and the **groundtruth data** ```annotations.tar.gz``` to the ```tensorflow/models/research/``` directory and unzip them.

After downloading the tarballs, your ```tensorflow/models/research/``` directory should appear as follows:

```
- images.tar.gz
- annotations.tar.gz
+ images/
+ annotations/
+ object_detection/
... other files and directories
```

## Convert the data to TFRecord Format

Run the ```create_pet_tf_record``` script to convert from the raw Oxford-IIIT Pet dataset into TFRecords. 

Run the following commands from the ```tensorflow/models/research/``` directory:

```
# From tensorflow/models/research/
python object_detection/create_pet_tf_record.py --label_map_path=object_detection/data/pet_label_map.pbtxt --data_dir=`pwd` --output_dir=`pwd`

# If error occur, use this instead
python object_detection/create_pet_tf_record.py --label_map_path=object_detection/data/pet_label_map.pbtxt --data_dir=C:\ProgramData\Anaconda3\envs\tensorflow\models\research --output_dir=C:\ProgramData\Anaconda3\envs\tensorflow\models\research
```

Note: It is normal to see some warnings when running this script. You may ignore them.

Two TFRecord files named ```pet_train.record``` and ```pet_val.record``` should be generated in the ```tensorflow/models/research/``` directory.

## Upload the TFRrecord to Google Cloud Storage

Upload it to Google Cloud Storage so the data can be accessed by ML Engine. Run the following command to copy the files into your GCS bucket ```(substituting ${YOUR_GCS_BUCKET})```:

```
# From tensorflow/models/research/
gsutil cp pet_train.record gs://${YOUR_GCS_BUCKET}/data/pet_train.record
gsutil cp pet_val.record gs://${YOUR_GCS_BUCKET}/data/pet_val.record
gsutil cp object_detection/data/pet_label_map.pbtxt gs://${YOUR_GCS_BUCKET}/data/pet_label_map.pbtxt
```

For example:
```
gsutil cp pet_train.record gs://oxford_pet_test/data/pet_train.record
gsutil cp pet_val.record gs://oxford_pet_test/data/pet_val.record
gsutil cp object_detection/data/pet_label_map.pbtxt gs://oxford_pet_test/data/pet_label_map.pbtxt
```

## Downloading a COCO-pretrained Model for Transfer Learning

Download ```COCO-pretrained Faster R-CNN with Resnet-101 model```:

http://storage.googleapis.com/download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz

Unzip the contents of the folder and copy the ```model.ckpt*``` files into your GCS Bucket.

```
wget http://storage.googleapis.com/download.tensorflow.org/models/object_detection/faster_rcnn_resnet101_coco_11_06_2017.tar.gz
tar -xvf faster_rcnn_resnet101_coco_11_06_2017.tar.gz
gsutil cp faster_rcnn_resnet101_coco_11_06_2017/model.ckpt.* gs://${YOUR_GCS_BUCKET}/data/
```

For example:
```
gsutil cp faster_rcnn_resnet101_coco_11_06_2017/model.ckpt.* gs://oxford_pet_test/data/
```

```model.ckpt.meta```, ```model.ckpt.index```, ```model.ckpt.data-00000-of-00001``` will be uploaded

## Configuring the Object Detection Pipeline

In the ```object_detection/samples/configs``` folder, there are skeleton object_detection configuration files. 

We will use ```faster_rcnn_resnet101_pets.config``` as a starting point for configuring the pipeline.

Search the file for instances of ```PATH_TO_BE_CONFIGURED``` and **replace** them with the appropriate value (typically ```gs://${YOUR_GCS_BUCKET}/data/```).

Then, **upload** your edited file onto GCS, making note of the path it was uploaded to (we'll need it when starting the ```training/eval``` jobs).

```
# From tensorflow/models/research/

# Edit the faster_rcnn_resnet101_pets.config template. Please note that there
# are multiple places where PATH_TO_BE_CONFIGURED needs to be set.
sed -i "s|PATH_TO_BE_CONFIGURED|"gs://${YOUR_GCS_BUCKET}"/data|g" object_detection/samples/configs/faster_rcnn_resnet101_pets.config

# Copy edited template to cloud.
gsutil cp object_detection/samples/configs/faster_rcnn_resnet101_pets.config gs://${YOUR_GCS_BUCKET}/data/faster_rcnn_resnet101_pets.config
```

If code above is not working, please open the config file and edit the 'PATH_TO_BE_CONFIGURED' to your Bucket name.

Then run:
```gsutil cp object_detection/samples/configs/faster_rcnn_resnet101_pets.config gs://oxford_pet_test/data/faster_rcnn_resnet101_pets.config```


## Checking Your Google Cloud Storage Bucket

You should have uploaded the ```training/validation datasets``` (including label map), our ```COCO trained FasterRCNN finetune checkpoint``` and your ```job configuration``` to your Google Cloud Storage Bucket. 

Your bucket should look like the following:

```
+ ${YOUR_GCS_BUCKET}/
  + data/
    - faster_rcnn_resnet101_pets.config
    - model.ckpt.index
    - model.ckpt.meta
    - model.ckpt.data-00000-of-00001
    - pet_label_map.pbtxt
    - pet_train.record
    - pet_val.record
```

You can inspect your bucket using the Google Cloud Storage browser:

https://console.cloud.google.com/storage/browser


