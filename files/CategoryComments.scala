//Scala code to get top 5 categories with max comments

val t0 = System.nanoTime()

val textFile = sc.textFile("hdfs://localhost:54310/youtubeData.txt")
val counts = textFile.filter { x => {if(x.toString().split("\t").length >= 10) true else false} }.map(line=>{line.toString().split("\t")})	
val pairs = counts.map(x => {(x(5),x(10).toInt)})
val res=pairs.reduceByKey(math.max(_, _)).map(item => item.swap).sortByKey(false).take(5)

val t1 = System.nanoTime()


import java.io._
val pw = new PrintWriter(new File("sparkET1.txt" ))
pw.write((t1-t0).toString)
pw.close

System.exit(0)