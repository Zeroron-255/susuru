# susuru
susuruDatabase
#get_susuru_movie_data.py
outubeAPIを使ってSUSURUTVの動画を取得し、csvを書き出すプログラム <br>
参照サイト : https://diy-programming.site/youtube/channel-video-info-get/ <br>
APIKEY : YoutubeAPI で発行した API を入れる <br>
channel_id : 抽出するYoutube Channed ID を入れる. SUSURUTVの場合は "UCXcjvt8cOfwtcqaMeE7-hqA" <br>

#extract_susuru_movie_csv.py
データベースで必要な部分を切り取り csv を書き出すプログラム <br>
input_filename : get_susuru_movie_data で作成した csvファイル名 を入れる <br>

#20230111_201817_UCXcjvt8cOfwtcqaMeE7-hqA_channel-video-info.csv
get_susuru_movie_data.py で出力される csv <br>

#susuru.csv
extract_susuru_movie_csv.py で出力される csv <br>
