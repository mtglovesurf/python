@echo off

cd %~dp0

docker image build . -t nginx-img
docker images
docker run --name nginx-con --rm -d -p 8080:8080 nginx-img
docker ps
docker stop nginx-con
docker rmi nginx-img --force

pause
