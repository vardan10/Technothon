//Scala code to get top 5 categories with most number of videos uploaded.

val t0 = System.nanoTime()

val textFile = sc.textFile("hdfs://localhost:54310/youtubeData.txt")
var counts=textFile.filter { x => {if(x.toString().split("\t").length >= 6) true else false} }.map(line=>{var YoutubeRecord = ""; val temp=line.split("\t"); ;if(temp.length >= 3) {YoutubeRecord=temp(5)};YoutubeRecord})
val test=counts.map ( x => (x,1) )
val res=test.reduceByKey(_+_).map(item => item.swap).sortByKey(false).take(5)

val t1 = System.nanoTime()


import java.io._
val pw = new PrintWriter(new File("sparkET2.txt" ))
pw.write((t1-t0).toString)
pw.close

System.exit(0)