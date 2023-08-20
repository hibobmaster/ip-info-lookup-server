FROM python:3.11-alpine as base

FROM base as pybuilder
# RUN sed -i 's|v3\.\d*|edge|' /etc/apk/repositories
COPY requirements.txt /requirements.txt
RUN pip install --user -r /requirements.txt && rm /requirements.txt

FROM base as runner
COPY --from=pybuilder /root/.local /usr/local
COPY . /app

FROM runner
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--proxy-headers", "--forwarded-allow-ips", "*"]