FROM python:3.9.10-alpine3.14
ENV FLASK_APP=app
WORKDIR /python
COPY . /python
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python","app.py"]


