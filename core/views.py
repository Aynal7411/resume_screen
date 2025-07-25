from django.shortcuts import render, redirect
from .forms import ResumeForm
from .models import Resume
from .utils import extract_text_from_pdf, extract_text_from_docx, clean_text, calculate_score

import os



def home(request):
    return render(request, 'home.html')
# কীওয়ার্ড লিস্ট (পরবর্তীতে ডাটাবেস থেকেও আনতে পারেন)
JOB_KEYWORDS = [
    'python',
    'django',
    'flask',
    'fastapi',
    'rest',
    'graphql',
    'api',
    'sql',
    'postgresql',
    'mysql',
    'sqlite',
    'mongodb',
    'html',
    'css',
    'bootstrap',
    'tailwind',
    'javascript',
    'typescript',
    'react',
    'next.js',
    'vue',
    'node.js',
    'express',
    'git',
    'github',
    'docker',
    'kubernetes',
    'linux',
    'bash',
    'aws',
    'azure',
    'gcp',
    'machine learning',
    'deep learning',
    'tensorflow',
    'pytorch',
    'scikit-learn',
    'pandas',
    'numpy',
    'opencv',
    'nlp',
    'spaCy',
    'transformers',
    'llm',
    'data analysis',
    'data visualization',
    'matplotlib',
    'seaborn',
    'plotly',
    'powerbi',
    'excel',
    'etl',
    'big data',
    'hadoop',
    'spark',
    'airflow',
    'celery',
    'rabbitmq',
    'redis',
    'unit testing',
    'pytest',
    'selenium',
    'cypress',
    'ci/cd',
    'devops',
    'scrum',
    'agile'
]


def score_resume(text, keywords):
    score = 0
    for word in keywords:
        if word.lower() in text.lower():
            score += 1
    return score

def resume_upload(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            ext = os.path.splitext(resume.file.name)[1]

            if ext == '.pdf':
                text = extract_text_from_pdf(resume.file)
            elif ext == '.docx':
                text = extract_text_from_docx(resume.file)
            else:
                text = ""

            result = calculate_score(text, JOB_KEYWORDS)
            resume.score = result['percentage']
            resume.matched_keywords = ', '.join(result['matched']) 
            resume.save()
            return redirect('resume_list')
    else:
        form = ResumeForm()
    return render(request, 'upload.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all().order_by('-score')
    return render(request, 'list.html', {'resumes': resumes})
