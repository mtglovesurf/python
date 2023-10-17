【docker環境のセットアップ】
1. イメージ作成およびコンテナ起動
sudo docker login -u zukosha -p zukosha-pass
sudo docker-compose up -d
sudo docker logout

8. WEBコンテナへログインし、サーバ起動を確認する。
sudo docker exec -it CON1 /bin/bash
curl http://localhost:3000/

9. cronを有効にし、メール連携ジョブを登録する。
service cron start
crontab -e
--------------------------------------------------------------------------------------------------
SHELL=/bin/sh
BUNDLE_APP_CONFIG=/usr/local/bundle
GEM_HOME=/usr/local/bundle
PATH=/usr/local/bundle/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* *	* * *	/usr/src/redmine/mail_renkei.sh >> /usr/src/redmine/log/mail_renkei.log 2>&1
--------------------------------------------------------------------------------------------------
exit

10. ホストから、WEBコンテナへの接続を確認する。
curl http://18.178.181.33/

11. 外部ブラウザから、WEBコンテナへの接続を確認する。
http://18.178.181.33/

12. DBコンテナへログインし、MySQL起動と文字コードを確認する。
sudo docker exec -it CON2 /bin/bash
mysql -uroot -pexample
show create database redmine;


【共用メールボックス整備】
1. 共用メールボックスを取得する（※Yahoo!メール）
メールアドレス：fjhii26026@yahoo.co.jp 
パスワード：435aFs987

2. 振り分け用のメールボックスを作成する
成功時の振り分けフォルダ名：read
失敗時の振り分けフォルダ名：failed

3. IMAPを有効にする

【Redmine環境整備】
1. adminでログインして初期パスワードを変更する
http://18.178.181.33/
アカウント：admin
初期パスワード：admin
変更後パスワード：0155332200

2. ロールを作成する
名称：メール連携
権限：チケットの閲覧、チケットの追加、チケットの編集
チケットトラッキング：「すべてのトラッカー」すべてにチェックをつける

3. ステータスを追加する
名称：未着手、対応中、対応完了、終了（終了したチケット）

4. チケットの優先度を登録する
名称：通常
有効：チェック
デフォルト値：チェック

5. プロジェクトを追加する
プロジェクト名：メール連携
プロジェクト識別子：mail_renkei

6. トラッカーを作成する
名称：問い合せ
プロジェクト：メール連携にチェック

7. ユーザーを追加する
ログインID：任意
名：任意
性：任意
メールアドレス：※メール連携する送信元のアドレス
パスワード：password

8. ユーザーをプロジェクトに追加する
7で作成したユーザーと匿名ユーザーを選択し、「メール連携」のロールで登録する。

9. 共用メールボックスにメールを送信し、1分後にチケット連携されることを確認する。
 

【docker利用終了】
1. コンテナ停止
sudo docker-compose down
∟※コンテナが停止されない場合
　sudo docker ps
　sudo docker rm -f [CONTAINER ID]

【コンテナへのファイルコピー】
sudo docker cp /home/ec2-user/mail_renkei.sh CON1:/usr/src/redmine/mail_renkei.sh

【コンテナからのファイルコピー】
sudo docker cp CON1:/var/spool/cron/crontabs/root /home/ec2-user/download/root

【docker環境リセット】
1. コンテナ停止およびイメージ削除
sudo docker-compose down --rmi all
∟※イメージが削除されない場合
　sudo docker images
　sudo docker rmi -f [IMAGE ID]

2. dockerのゴミデータ削除
sudo docker system prune -a --volumes
sudo docker system df

3. ホームディレクトリのデータ削除
cd $HOME
sudo rm -r *