FROM python

MAINTAINER Mike Terekhov 'mike_terekhov@gmail.com'

RUN mkdir -p /usr/src/app/flask_blog_test/
WORKDIR /usr/src/app/flask_blog_test/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 4200
EXPOSE $PORT


CMD ["python", "run.py"]