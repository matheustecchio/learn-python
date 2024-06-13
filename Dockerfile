FROM python:3.12
EXPOSE 5000
WORKDIR /app
COPY requiraments.txt .
RUN pip install -r requiraments.txt
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]