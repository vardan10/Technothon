import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import java.util.*;
import java.io.*;

public class ChannelLikes {

    public static class Map2 extends Mapper<LongWritable, Text, Text, FloatWritable> {

       private Text video_name = new Text();
       private  FloatWritable rating = new FloatWritable();

       public void map(LongWritable key, Text value, Context context ) throws IOException, InterruptedException {
           String line = value.toString();
           String str[]=line.split("\t");

          if(str.length > 6){
                video_name.set(str[4]);
                if(str[7].matches("\\d+.+")){ //this regular expression specifies that the string should contain only floating values
                float f=Float.parseFloat(str[7]); //typecasting string to float
                rating.set(f);
                }
          }

      context.write(video_name, rating);
      }

    }




    public static class Reduce extends Reducer<Text, FloatWritable, Text, FloatWritable> {

       LinkedHashMap<String , Float>  map = new LinkedHashMap<String , Float>();

       public void reduce(Text key, Iterable<FloatWritable> values, Context context) throws IOException, InterruptedException {
           float max = -1;
           for (FloatWritable val : values) {
              if (max == -1 || max < val.get())
              {
                  max = val.get();
              }
           }
           
           map.put(key.toString(), max);
       }

      public void cleanup(Context context){ 

              /*for ( String key : map.keySet() ) {


              }*/
              List<Map.Entry<String, Float>> list =
            new LinkedList<Map.Entry<String, Float>>( map.entrySet() );
        Collections.sort( list, new Comparator<Map.Entry<String, Float>>()
        {
            public int compare( Map.Entry<String, Float> o1, Map.Entry<String, Float> o2 )
            {
                return (o2.getValue()).compareTo( o1.getValue() );
            }
        } );

        LinkedHashMap<String, Float> result = new LinkedHashMap<String, Float>();
        for (Map.Entry<String, Float> entry : list)
        {
          try{
            context.write(new Text(entry.getKey()),new FloatWritable(entry.getValue()));
          }catch(Exception e){
            System.out.println("Exception");
          }
        }
        map=result;
      }

    }




    public static void main(String[] args) throws Exception {
      

      long t0 = System.nanoTime();

      Configuration conf = new Configuration();

       @SuppressWarnings("deprecation")
            Job job = new Job(conf, "videorating");
       job.setJarByClass(ChannelLikes.class);

       job.setMapOutputKeyClass(Text.class);
       job.setMapOutputValueClass(FloatWritable.class);
      //job.setNumReduceTasks(0);
       job.setOutputKeyClass(Text.class);
       job.setOutputValueClass(FloatWritable.class);

       job.setMapperClass(Map2.class);
       job.setReducerClass(Reduce.class);

       job.setInputFormatClass(TextInputFormat.class);
       job.setOutputFormatClass(TextOutputFormat.class);

       FileInputFormat.addInputPath(job, new Path(args[0]));
       FileOutputFormat.setOutputPath(job, new Path(args[1]));
        Path out=new Path(args[1]);
        out.getFileSystem(conf).delete(out);
       job.waitForCompletion(true);

        long t1 = System.nanoTime();
       FileWriter writer = new FileWriter(new File("mapreduceET3.txt"));
       writer.write(String.valueOf(t1-t0)); 
       writer.flush();
       writer.close();
    }

  }