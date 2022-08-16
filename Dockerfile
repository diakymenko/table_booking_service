FROM python:latest
WORKDIR /booking_service
COPY . .
RUN pip install -r requirements.txt
ENV TZ=America/Los_Angeles
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]