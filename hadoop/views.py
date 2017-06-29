from django.shortcuts import render
from django.http import HttpResponse
import subprocess
import time
from datetime import datetime
from jinja2 import Template
from furl import furl


def index(request):
	return render(request,'index.html')


def runProcesses(file,number):
	# processes = set()

	# mapReduce = "$HADOOP_HOME/bin/hadoop jar files/" + jar + " /youtubeData.txt /mapreduce_output_sales"
	# spark = "~/spark/bin/spark-shell -i files/"+ scala
	# hive = "$HIVE_HOME/bin/hive -f /home/vardan/Desktop/YoutubeAnalysis/files/" + hql + " > output.txt"

	# processes.add(subprocess.Popen(mapReduce, stdout=subprocess.PIPE, shell=True));
	# processes.add(subprocess.Popen(spark, shell=True));
	# processes.add(subprocess.Popen(hive, stdout=subprocess.PIPE, shell=True));

	# for p in processes:
	# 	if p.poll() is None:
	# 		p.wait()

	file = str(file)

	some_command = "cat sparkET" + file + ".txt"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(spark, err) = p.communicate()  
	p_status = p.wait()

	some_command = "cat mapreduceET" + file + ".txt"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(mapreduce, err) = p.communicate()  
	p_status = p.wait()

	some_command = "cat output" + file + ".txt | head -n1"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(hiveST, err) = p.communicate()  
	p_status = p.wait()
	some_command = "cat output" + file + ".txt | tail -n1"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(hiveET, err) = p.communicate()  
	p_status = p.wait()
	hive = float(hiveET) - float(hiveST)
	if hive<=0:
		hive = 60 + hive


	number1 = number + 1;
	some_command = "cat output" + file + ".txt | head -n" + str(number1) + " | tail -n" + str(number)
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()  
	p_status = p.wait()

	return mapreduce,spark,hive,output





def CategoryComments(request):
	mapreduce,spark,hive,output = runProcesses(1,5);

	returnList = []
	outputList = output.split('\n');
	i = 1;
	for xyz in outputList:
		if not xyz == "":
			returndict = {}
			returndict["key"] = xyz.split('\t')[0]
			returndict["value"] = xyz.split('\t')[1]
			i = i + 1;
			returnList.append(returndict)

	return render(request,'CategoryComments.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":float(hive)})




def CategoryUploaded(request):
	mapreduce,spark,hive,output = runProcesses(2,5);

	returnList = []
	outputList = output.split('\n');
	i = 1;
	for xyz in outputList:
		if not xyz == "":
			returndict = {}
			returndict["key"] = xyz.split('\t')[0]
			returndict["value"] = xyz.split('\t')[1]
			i = i + 1;
			returnList.append(returndict)

	return render(request,'CategoryUploaded.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":float(hive)})




def ChannelLikes(request):
	mapreduce,spark,hive,output = runProcesses(3,10);

	returnList = []
	outputList = output.split('\n');
	i = 1;
	for xyz in outputList:
		if not xyz == "":
			returndict = {}
			returndict["key"] = xyz.split('\t')[0]
			returndict["value"] = xyz.split('\t')[1]
			i = i + 1;
			returnList.append(returndict)

	return render(request,'ChannelLikes.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":float(hive)})





def TopLikes(request):
	mapreduce,spark,hive,output = runProcesses(4,10);

	returnList = []
	outputList = output.split('\n');
	i = 1;
	for xyz in outputList:
		if not xyz == "":
			returndict = {}
			returndict["key"] = xyz.split('\t')[0]
			returndict["value"] = xyz.split('\t')[1]
			i = i + 1;
			returnList.append(returndict)

	return render(request,'TopRated.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":float(hive)})





def TopViewed(request):
	mapreduce,spark,hive,output = runProcesses(5,10);

	returnList = []
	outputList = output.split('\n');
	i = 1;
	for xyz in outputList:
		if not xyz == "":
			returndict = {}
			returndict["key"] = xyz.split('\t')[1]
			returndict["value"] = xyz.split('\t')[2]
			i = i + 1;
			returnList.append(returndict)

	return render(request,'TopViewed.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":float(hive)})




def CountryViews(request):
	# processes = set()

	# #mapReduce = "gnome-terminal --command='/home/vardan/hadoop/bin/hadoop jar files/CountryViews.jar /youtubeData.txt /mapreduce_output_sales'"
	# mapReduce = "$HADOOP_HOME/bin/hadoop jar files/CountryViews.jar /youtubeData.txt /mapreduce_output_sales"
	# spark = "~/spark/bin/spark-shell -i files/CountryViews.scala"
	# #spark = "gnome-terminal --command='/home/vardan/spark/bin/spark-shell -i files/CountryViews.scala'"
	# hive = "$HIVE_HOME/bin/hive -f /home/vardan/Desktop/YoutubeAnalysis/files/CountryViews.hql > output.txt"
	# #hive = "gnome-terminal --command='/home/vardan/apache-hive-2.1.0-bin/bin/hive -f /home/vardan/Desktop/YoutubeAnalysis/files/CountryViews.hql > /home/vardan/Desktop/YoutubeAnalysis/output.txt'"
	# processes.add(subprocess.Popen(mapReduce));
	# processes.add(subprocess.Popen(spark));
	# processes.add(subprocess.Popen(hive));

	# for p in processes:
	# 	if p.poll() is None:
	# 		p.wait()

	some_command = "cat sparkET6.txt"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(spark, err) = p.communicate()  
	p_status = p.wait()

	some_command = "cat mapreduceET6.txt"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(mapreduce, err) = p.communicate()  
	p_status = p.wait()

	some_command = "cat output6.txt | head -n1"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(hiveST, err) = p.communicate()  
	p_status = p.wait()
	some_command = "cat output6.txt | tail -n1"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(hiveET, err) = p.communicate()  
	p_status = p.wait()
	hive = float(hiveET) - float(hiveST)
	if hive<=0:
		hive = 60 + hive

	some_command = "cat output6.txt | head -n153 | tail -n150"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()  
	p_status = p.wait()


	returnList = []
	outputList = output.split('\n');
	for xyz in outputList:
		try:
			returndict = {}
			returndict["country"] = str(xyz.split('\t')[0])
			returndict["title"] = str(xyz.split('\t')[1])
			returndict["count"] = str(xyz.split('\t')[2])
			returnList.append(returndict)
		except:
			pass
			
	return render(request,'CountryViews.html',{"data":returnList,"mapReduce":float(mapreduce)/1000000000,"spark":float(spark)/1000000000,"hive":hive})









def Sentiment(request):

	cId = request.GET["cid"];
	f = furl(cId)

	processes = set()
	some_command = "java -jar comments.jar " + f.args['v'] + " /home/vardan/Desktop/YoutubeAnalysis/sentiment/youtubeData.json"
	processes.add(subprocess.Popen(some_command, shell=True));
	
	for p in processes:
		if p.poll() is None:
			p.wait()


	processes = set()
	some_command = "~/spark/bin/spark-submit sentiment/MLib.py"
	processes.add(subprocess.Popen(some_command, shell=True));
	
	for p in processes:
		if p.poll() is None:
			p.wait()

	some_command = "cat sentiment.txt"
	p = subprocess.Popen(some_command, stdout=subprocess.PIPE, shell=True)
	(sentiment, err) = p.communicate()  
	p_status = p.wait()

	count = sentiment.split('\n')[0]
	positive = sentiment.split('\n')[1]
	negative = sentiment.split('\n')[2]

	return render(request,'sentiment.html',{"count":count,"positive":int(positive),"negative":int(negative)})