FROM python:3.9

WORKDIR /app/

COPY ./db_app/ /app/

EXPOSE 5000

RUN python -m pip install --upgrade pip \
    && pip3 install -r requirements.txt --no-cache-dir \
    && python --version

CMD ["python", "app.py"]