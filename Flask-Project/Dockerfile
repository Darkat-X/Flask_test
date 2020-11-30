FROM python:3.8
WORKDIR /clothes

COPY test.txt ./
RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt install -y libgl1-mesa-glx
RUN pip install -r test.txt

COPY . .

CMD ["gunicorn","classification_images_clothing:app","./gunicorn.conf.py"]

