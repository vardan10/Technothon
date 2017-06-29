## Youtube data Analysis Using Spark, MapReduce and Hive

This is a study project and includes running queries using Spark, MapReduce and Hive and compare execution time of all three platforms. Also it performs sentimental analysis of a pariticular video on youtube and classifies how many comments are positive and negative.


### How to run
1. Clone This project

2. Setup hadoop 2.x.x (2.7.3 used for testing). HADOOP_HOME variable should be set

3. Setup Spark 2.x.x (2.1.0 used for testing). spark folder should be extracted to home folder and the folder should be renamed as spark. OR Set up SPARK_HOME variable and change '~/spark' of cron.py (line 10) to SPARK_HOME

4. Setup hive 2.x.x (2.1.0 used for testing). HIVE_HOME variable should be set

5. Move youtubeData.txt to HDFS as /youtubeData.txt

6. Install Java

7. Install Python (Sudo apt-get install python)

8. Install pip (sudo apt-get install python-pip)

9. Run the command pip install -r requirements.txt

10. Run the cron.py file to run all the queries (python cron.py)

11. Run Django server (python manage.py runserver)

12. Open localhost:8000/app/ in browser