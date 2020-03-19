from django.shortcuts import render

def home(request):
   
    import json
    import requests

    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95131&distance=50&API_KEY=3A70E4E2-17A7-4E93-A9A9-5BE160C30DE3")
    
    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error..." 
    
    
    return render(request,'lookup/home.html',{'api':api})
    

def about(request):
    return render(request,'lookup/about.html',{})




#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=95131&distance=50&API_KEY=3A70E4E2-17A7-4E93-A9A9-5BE160C30DE3
    