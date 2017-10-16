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
