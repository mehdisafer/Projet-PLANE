FROM python:3.11

RUN useradd -m user

USER user

WORKDIR /home/user

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .
COPY components/ /home/user/components/
COPY data/ /home/user/data/
COPY models/ /home/user/models/
COPY catboost_info/ /home/user/catboost_info/


EXPOSE 8501

CMD ["/home/user/.local/bin/streamlit", "run", "main.py"]