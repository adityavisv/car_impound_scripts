md impoundsrv
cd impoundsrv
wget "https://raw.githubusercontent.com/adityavisv/car_impound_service/main/Dockerfile" -outfile "Dockerfile"
docker build --no-cache -t impoundsrv-tomcat .
docker run --name impoundsrv-container --restart always -d -p 8080:8080 impoundsrv-tomcat

cd ..
md impoundui
cd impoundui
wget "https://github.com/adityavisv/car_impound_ui/archive/refs/heads/main.zip" -outfile "impoundui.zip"
Expand-Archive -Path impoundui.zip -DestinationPath ./impoundui
cd impoundui
docker build --no-cache -t impoundui-node .
docker run --name impoundui-container --restart always -d -p 3000:3000 impoundui-node
