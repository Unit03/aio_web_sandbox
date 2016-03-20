FROM python:3.5

ARG PIP_EXTRA_INDEX_URL
ARG PIP_TRUSTED_HOST

# Create user.
RUN useradd -m pythonapp

# Add application and install Python dependencies.
# TODO: virtual env.
RUN pip install --upgrade pip
ADD . /foo
RUN PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} \
    PIP_TRUSTED_HOST=${PIP_TRUSTED_HOST} \
    pip install --editable /foo

EXPOSE 8000

CMD ["foo"]
