Bienvenue dans l'application Satisfaction Series X 360

pour lancer l'application veuillez executer :

- `streamlit run main.py`

pour utiliser l'application en version docker :

- `docker build -t satisfaction360:latest .`

cela va créer une image "satisfaction360"

pour lancer l'image docker :

- `docker run -d -p 8501:8501 --name satisfactiondocker satisfaction360`

vous pouvez changer le port externe selon vos besoin la première valeur après -p
vous pouvez changer le nom de votre docker ici nous avons utilisé "satisfactiondocker",
si vous avez utilisé un autre nom d'image lors de la création veuillez la changer aussi