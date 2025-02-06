from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import JobPosting
from .pipeline import TextPreprocessing
import pickle
from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize.regexp import RegexpTokenizer
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import pandas as pd
from .transformer import get_text_from_document, get_pdf
import numpy as np

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES.get('document'):
        document = request.FILES['document']
        JobPosting.objects.create(document = document)
        return  redirect('/job')
    return render(request, 'upload.html')

def job_list(request):
    try:
        df = pd.DataFrame(list(JobPosting.objects.all().values()))
        df = df[["id", "document", "uploaded_at"]]
        df["id"] = df["id"].astype(str)
        df["uploaded_at"] = df["uploaded_at"].dt.strftime('%Y-%m-%d')
    except Exception:
        df = pd.DataFrame(columns=["id", "document", "uploaded_at"])
    df.rename(columns={"id": "ID", "document": "Job Posting", "uploaded_at": "Date"}, inplace=True)

    def add_url(data):
        output = "<a href='"
        output = output + data
        output = output + "'>"
        output = output + data
        output = output + "</a"
        return output

    df["ID"] = df["ID"].apply(add_url)

    html_table = df.to_html(
        escape=False,
        index=False,
        border=1,
        classes="table table-striped table-hover"
    )
    params = {"html_table": html_table}
    return render(request, 'job_list.html', params)

def predict(request, job_posting_id):
    ### Read trained pipeline
    model = pickle.load(open("predict_salary/model.pkl", 'rb'))
    filename = JobPosting.objects.values_list(
        "document",
        flat=True
    ).get(id=job_posting_id)
    print(filename)
    print(job_posting_id)
    if ".docx" in filename:
        clean_text = get_text_from_document(filename)
    elif ".pdf" in filename:
        clean_text = get_pdf(filename)

    df = pd.DataFrame(
        [clean_text],
        columns = ["Job Description"]
    )

    prediction = np.round(model.predict(df)[0],2)
    prediction = str(prediction) + " K / year"
    params = {"prediction": prediction}

    return render(request, 'predict.html', params)


