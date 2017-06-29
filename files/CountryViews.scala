//Scala code to get top 5 videos with max no.of views countrywise with videotitle.

val t0 = System.nanoTime()

val textFile = sc.textFile("hdfs://localhost:54310/youtubeData.txt")
val counts = textFile.filter { x => {if(x.toString().split("\t").length >= 10) true else false} }.map(line=>{line.toString().split("\t")})
val makeMap  = counts.map(x => {(x(11),x(3),x(6).toInt)})
val grouping = makeMap.groupBy(makeMap=>(makeMap._1)).sortByKey(true)
val sorting = grouping.mapValues(iter => iter.toList.sortWith(_._3 > _._3))
val finalresult = sorting.foreach(p => println(">>> key=" + (p._1) + ", value1=" + (p._2).take(5)))

val t1 = System.nanoTime()


import java.io._
val pw = new PrintWriter(new File("sparkET6.txt" ))
pw.write((t1-t0).toString)
pw.close

System.exit(0)