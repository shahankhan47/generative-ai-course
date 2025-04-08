Create and activate the virtual environment:

pip install virtualenv
python -m virtualenv my_env OR virtualenv my_env
my_env\Scripts\activate OR source my_env/bin/activate

Install libraries in the virtual environment:

# installing required libraries in my_env

Create a file called requirements.txt and add the following dependencies:

langchain==0.1.11
gradio==5.23.2
transformers==4.38.2
bs4==0.0.2
requests==2.31.0
torch==2.2.1

Now in your terminal after your virtual env is activated, run the command:
pip3 install -r requirements.txt
