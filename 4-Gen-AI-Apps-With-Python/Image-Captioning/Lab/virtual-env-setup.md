Create and activate the virtual environment:

    pip install virtualenv
    python -m virtualenv my_env # create a virtual environment my_env
    my_env\Scripts\activate # activate my_env

    Install libraries in the virtual environment:

    # installing required libraries in my_env

    pip install langchain==0.1.11 gradio==5.23.2 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1
