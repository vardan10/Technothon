from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.feature import HashingTF
import json

countPositive = 0;
countNegative = 0;

def remove_stopwords(sentence):

	word_list = sentence.split(" ")
	processed_word_list = []

	for word in word_list:
		word = word.lower()
		if word not in STOPWORDS:
			processed_word_list.append(word)
	return ' '.join(processed_word_list)




STOPWORDS = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 
'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until',
'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 
'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 
'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 
'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 
'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 
'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than', 'very']




if __name__ == "__main__":
	sc = SparkContext(appName="PythonBookExample")

	# Load 2 types of emails from text files: spam and ham (non-spam).
	# Each line has text from one email.
	positive = sc.textFile("sentiment/positive.txt")
	negative = sc.textFile("sentiment/negative.txt")
	# neutral = sc.textFile("neutral.txt")

	# Create a HashingTF instance to map email text to vectors of 100 features.
	tf = HashingTF(numFeatures = 20)
	# Each email is split into words, and each word is mapped to one feature.
	positiveFeatures = positive.map(lambda email: tf.transform(remove_stopwords(email).split(" ")))
	negativeFeatures = negative.map(lambda email: tf.transform(remove_stopwords(email).split(" ")))

	# Create LabeledPoint datasets for positive (spam) and negative (ham) examples.
	positiveExamples = positiveFeatures.map(lambda features: LabeledPoint(1, features))
	negativeExamples = negativeFeatures.map(lambda features: LabeledPoint(0, features))
	
	#training_data = positiveExamples.union(negativeExamples).union(neutralExamples)
	training_data = positiveExamples.union(negativeExamples)
	training_data.cache() # Cache data since Logistic Regression is an iterative algorithm.

	# Run Logistic Regression using the SGD optimizer.
	# regParam is model regularization, which can make models more robust.
	model = LogisticRegressionWithSGD.train(training_data)


	json_data=open("sentiment/youtubeData.json").read()
	data = json.loads(json_data)

	count = 0;
	for xyz in data['Items']:
		count += 1;
		test = xyz['Comment'].encode('ascii', 'ignore').decode('ascii')
		TestExample = tf.transform(remove_stopwords(test).split(" "))
		if model.predict(TestExample) == 0:
			countNegative += 1;
		elif model.predict(TestExample) == 1:
			countPositive += 1;


	target = open("sentiment.txt", 'w')
	target.write(str(count))
	target.write("\n")
	target.write(str(countPositive))
	target.write("\n")
	target.write(str(countNegative))
	target.write("\n")
	target.close()

	sc.stop()

