//Scala code to get top 10 viewed videos uploaded.

val t0 = System.nanoTime()

val textFile = sc.textFile("hdfs://localhost:54310/youtubeData.txt")
val counts = textFile.filter { x => {if(x.toString().split("\t").length >= 6) true else false} }.map(line=>{line.toString().split("\t")})
val pairs = counts.map(x => {(x(3),x(6).toInt)})
val res=pairs.reduceByKey(_+_).map(item => item.swap).sortByKey(false).take(10)

val t1 = System.nanoTime()


import java.io._
val pw = new PrintWriter(new File("sparkET5.txt" ))
pw.write((t1-t0).toString)
pw.close

System.exit(0)