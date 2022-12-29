FROM python:3.9.10-alpine3.14
COPY . /python
RUN pip install --upgrade pip
WORKDIR /python
RUN pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["python","app.py"]
#ENTRYPOINT ["python"]

