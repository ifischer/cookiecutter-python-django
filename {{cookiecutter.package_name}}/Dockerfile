FROM python{%- if cookiecutter.python_version %}:{{ cookiecutter.python_version }}{%- endif %}
RUN pip install --upgrade setuptools pip

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONPATH=/code

WORKDIR /code
COPY requirements.txt .
COPY requirements-dev.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /code

# Allow overriding source files via volumes
RUN mkdir -p $(python -m site --user-site)
RUN cd $(python -m site --user-site) && python /code/setup.py develop

# Configure IPython
COPY config/ipython/ipython_config.py /root/.ipython/profile_default/
COPY config/ipython/startup.py /root/.ipython/profile_default/startup/

EXPOSE 8000

# Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    gunicorn --reload --bind 0.0.0.0:8000 --access-logfile - {{cookiecutter.app_name}}.wsgi:application
