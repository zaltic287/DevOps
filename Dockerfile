# Text file

#########################################################
#    AUTEUR : Serigne Saliou NDIAYE
#    VERSION:
#    MODIFIE:
#
#    DESCRIPTION
#########################################################


# Fonctions #############################################



# Variables ############################################


FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]

