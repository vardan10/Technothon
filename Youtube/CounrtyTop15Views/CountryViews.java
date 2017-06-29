import java.io.IOException;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;


import java.io.DataInput;
import java.io.DataOutput;
import java.io.File;
import java.util.*;

import java.util.*;
import java.io.*;



public class CountryViews {

    public static class Map2 extends Mapper<LongWritable, Text, Text, CompositeGroupKey> {

        private Text video_name = new Text();

        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
            String line = value.toString();
            String str[]=line.split("\t");

            if(str.length > 10){
                video_name.set(str[11]);
                CompositeGroupKey cntry = new CompositeGroupKey(str[3], str[6]);
                context.write(video_name, cntry);
            }
        }

    }




    public static class Reduce extends Reducer<Text, CompositeGroupKey, Text, Text> {

        private Text video_name = new Text();
        private LinkedHashMap<String,Float> map = new LinkedHashMap<String,Float>();

        public void reduce(Text key, Iterable<CompositeGroupKey> values,Context context) throws IOException, InterruptedException {

            String videos = "";
            
           for (CompositeGroupKey val : values) {
                   map.put(val.getTitle(),Float.parseFloat(val.getCount()));
           }



            List<Map.Entry<String, Float>> list = new LinkedList<Map.Entry<String, Float>>( map.entrySet() );
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
                result.put(entry.getKey(),entry.getValue());
              }catch(Exception e){
                System.out.println("Exception");
              }
            }
            map=result;

            int count = 0;
            String text = "\n";
            for(String s:map.keySet()){
                text = text + s + "\t" + map.get(s);
                count ++;

                if (count>=5)
                    break;
                else
                    text += "\n";
            }

            context.write(new Text(key), new Text(text));
        }
    }

    private static class CompositeGroupKey implements WritableComparable<CompositeGroupKey> {
        String title;
        String count;

        public CompositeGroupKey(String title, String count) {
            this.title = title;
            this.count = count;
        }
        public CompositeGroupKey() {
            this.title = "";
            this.count = "";

        }

        public String getTitle(){
            return this.title;
        }

        public String getCount(){
            return this.count;
        }

        public void write(DataOutput out) throws IOException {
            WritableUtils.writeString(out, title);
            WritableUtils.writeString(out, count);
        }

        public void readFields(DataInput in) throws IOException {
            this.title = WritableUtils.readString(in);
            this.count = WritableUtils.readString(in);
        }

        public int compareTo(CompositeGroupKey pop) {
            if (pop == null)
                return 0;
            int intcnt = title.compareTo(pop.title);
            return intcnt == 0 ? count.compareTo(pop.count) : intcnt;
        }

        @Override
        public String toString() {
            return title.toString() + ":" + count.toString();
        }
    }




    public static void main(String[] args) throws Exception {
        long t0 = System.nanoTime();

        Configuration conf = new Configuration();

        @SuppressWarnings("deprecation")
        Job job = new Job(conf, "videorating");
        job.setJarByClass(CountryViews.class);

        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(CompositeGroupKey.class);
        //job.setNumReduceTasks(0);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);

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
       FileWriter writer = new FileWriter(new File("mapreduceET6.txt"));
       writer.write(String.valueOf(t1-t0)); 
       writer.flush();
       writer.close();
    }

}