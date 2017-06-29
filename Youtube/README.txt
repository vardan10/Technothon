$HADOOP_HOME/bin/hdfs dfs -copyFromLocal ~/vardan/Desktop/youtubeData.txt /youtubeData.txt

$HADOOP_HOME/bin/hdfs dfs -ls /

export CLASSPATH="$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-2.7.3.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-common-2.7.3.jar:$HADOOP_HOME/share/hadoop/common/hadoop-common-2.7.3.jar:~/MapReduceTutorial/SalesCountry/*:$HADOOP_HOME/lib/*"

javac -d . <java class>

jar cfm <JAR FILENAME> Manifest.txt *.class

$HADOOP_HOME/bin/hadoop jar <JAR FILENAME> /youtubeData.txt/ /mapreduce_output_youtube

$HADOOP_HOME/bin/hdfs dfs -cat /mapreduce_output_youtube/part-r-00000