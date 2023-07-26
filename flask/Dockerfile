FROM python:3.9

#WORKDIR /flask

#COPY requirements.txt .
#RUN apt-get update &&  pip install --no-cache-dir -r requirements.txt

#RUN apt-get update && \
 #   apt-get install -y python3-pip  && \
  #  apt install python3 python3-pip && \
  #  pip3 install Flask && \
  #  apt-get install python3-pymysql -y && \
  #  pip install PyMySQL && \
  #  apt install gunicorn -y
WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


COPY . /usr/src/app/

COPY . .

EXPOSE 8000

CMD [“gunicorn",”app:app”,”--bind”, “0.0.0.0:8000”]
