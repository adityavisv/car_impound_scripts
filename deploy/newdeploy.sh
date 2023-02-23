mkdir impoundsrv
cd impoundsrv
wget "https://raw.githubusercontent.com/adityavisv/car_impound_service/main/Dockerfile"
docker build -t impoundsrv-tomcat .
docker run --name impoundsrv-container --restart always -d -p 8080:8080 impoundsrv-tomcat

cd ..
mkdir impoundui
cd impoundui
wget "https://github.com/adityavisv/car_impound_ui/archive?refs/head/main.zip"
unzip main.zip
cd car_impound_ui
docker build -t impoundui-node .
docker run --name impoundui-container --restart always -d -p 3000:3000 impoundui-node
