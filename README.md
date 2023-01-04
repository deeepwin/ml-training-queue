### usage

To install simple machine learning queue:

1. Open code project in folder `ml-training-queue` 
2. Run in terminal `python setup.py install`


To start the queue run

`mlq-executor`

in a terminal. To add a job to the queue run in a seperate terminal:

`mlq-pusher -s "python file_to_exectue --work_dir=path_to_work_dir"`
