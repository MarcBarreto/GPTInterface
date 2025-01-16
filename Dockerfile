FROM python:3.12

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt .

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]