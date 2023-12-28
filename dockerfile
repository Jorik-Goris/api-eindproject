FROM python:3.10.0-alpine

WORKDIR /code

EXPOSE 8000

# Debugging: Print contents of the app directory before copy
RUN ls -R ./app

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code

# Debugging: Print contents of the /code directory after copy
RUN ls -R /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
