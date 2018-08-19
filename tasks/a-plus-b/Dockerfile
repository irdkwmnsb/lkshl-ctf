FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /service/
WORKDIR /service/

COPY ./requirements.txt /service/
RUN pip install --no-cache-dir -r ./requirements.txt

COPY ./ ./

EXPOSE 71

CMD ["./serve.py", "71"]
