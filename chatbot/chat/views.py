from django.shortcuts import render
import pickle
import pandas as pd
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Query_Storage

data = pd.read_csv("Python codes.csv") 
data["original_code"] = data["code"] 

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("chatbot_model.pkl", "rb") as f:
    knn = pickle.load(f)

Query_Storage.objects.all().delete()
def home(request):
	query_result = "Ask a question!!"
	enumerated_top3 = None
	if request.method == "POST":
		action= request.POST.get("action", "")
		question = request.POST.get("question", "").strip() 
		if question: 
			query_vector = vectorizer.transform([question])
			distances, indices = knn.kneighbors(query_vector)
			closest_indices = indices[0]
			closest_codes = data.iloc[closest_indices]["original_code"].tolist()
			if closest_codes:
				query_result = closest_codes[0]
				enumerated_top3 = list(enumerate(closest_codes[:3], start=1))
		Query_Storage.objects.create(question=question, answer=query_result)
		if action=="clear":
			Query_Storage.objects.all().delete()	
	show=Query_Storage.objects.all()
	return render(request, "home.html", {"query": query_result,"display":show,"top3_queries":enumerated_top3})

def connect(request):
	template=loader.get_template("contact.html")
	return HttpResponse(template.render())

def about(request):
	template=loader.get_template("about.html")
	return HttpResponse(template.render()) 
