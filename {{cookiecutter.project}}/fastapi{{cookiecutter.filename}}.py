from fastapi import FastAPI

app = FastAPI()


{%- if cookiecutter.name=="sample" -%}

@app.get('/')
def baseurl():
    return "welcome to the base fastapi template for {{cookiecutter.filename}}"


{%- elif cookiecutter.name=="others" -%}

@app.get('/')
def baseurl():
    return "This is the not the app you are looking for"

{% endif %}