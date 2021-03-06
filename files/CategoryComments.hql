drop database if exists youtubedb cascade;
create database youtubedb;
use youtubedb;

select from_unixtime(unix_timestamp(), 'ss.ss') AS StartTime;

create table if not exists YouTube_data_table (vedioid STRING, cid STRING, upload_date STRING, vtitle STRING, ctitle STRING, catid STRING, no_of_views INT, no_of_likes INT,no_of_dislikes INT, no_of_fav INT, no_of_comments INT, country STRING)  ROW FORMAT DELIMITED  FIELDS TERMINATED BY '\t'  STORED AS TEXTFILE;
load data local inpath '/home/vardan/Desktop/youtubeData.txt'overwrite into table YouTube_data_table;

select catid,max(no_of_comments) as max_no_comments from YouTube_data_table group by catid order by max_no_comments desc limit 5;

select from_unixtime(unix_timestamp(), 'ss.ss') AS EndTime;
