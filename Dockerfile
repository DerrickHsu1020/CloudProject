FROM python:3.7-alpine
WORKDIR /myapp
COPY . /myapp
RUN pip install -U -r requirement.txt
EXPOSE 8080
CMD ["python", "app.py"]
