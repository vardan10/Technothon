import subprocess

queries=["CategoryComments","CategoryUploaded","ChannelLikes","TopRated","TopViewed","CountryViews"]
i = 1;

for query in queries:
	processes = set()

	mapReduce = "$HADOOP_HOME/bin/hadoop jar files/" + query + ".jar /youtubeData.txt /mapreduce_output_sales"
	spark = "~/spark/bin/spark-shell -i files/"+ query + ".scala"
	hive = "$HIVE_HOME/bin/hive -f /home/vardan/Desktop/YoutubeAnalysis/files/" + query + ".hql > output" + str(i) + ".txt"

	print mapReduce
	print spark
	print hive

	processes.add(subprocess.Popen(mapReduce, stdout=subprocess.PIPE, shell=True));
	processes.add(subprocess.Popen(spark, shell=True));
	processes.add(subprocess.Popen(hive, stdout=subprocess.PIPE, shell=True));

	for p in processes:
		if p.poll() is None:
			p.wait()

	i += 1;