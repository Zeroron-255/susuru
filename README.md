# susuru
susuruDatabase

get_susuru_movie_data.py
# https://diy-programming.site/youtube/channel-video-info-get/
YoutubeAPIを使ってSUSURUTVの動画を取得し, csvを書き出すプログラム
APIKEY : YoutubeAPIで発行したAPIKEYを入れる
channel_id : 参照するYoutube Channel id, SUSURUTV="UCXcjvt8cOfwtcqaMeE7-hqA"

extract_susuru_movie_csv.py : csvデータで必要な部分を切り取り, csvを書き出す
input_filename : get_susuru_movie_data で作成したcsvファイル名を入れる

20230111_201817_UCXcjvt8cOfwtcqaMeE7-hqA_channel-video-info.csv : get の出力ファイル

susuru.csv : extract の出力ファイル
