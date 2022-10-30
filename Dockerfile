FROM python:3.9

RUN mkdir /opt/app
WORKDIR /opt/app
ADD requirements.txt /opt/app
RUN pip install -r requirements.txt
ADD src/ /opt/app

EXPOSE 8008
CMD ["uvicorn", "app:app", "--reload", "--host", "0.0.0.0", "--port", "8008"]
