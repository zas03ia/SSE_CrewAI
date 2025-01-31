# Django Streaming Server-Sent Events (SSE) with CrewAI

This project demonstrates **Server-Sent Events (SSE)** in Django using **CrewAI** and **Daphne** as the ASGI server. The system simulates an AI-powered HR assistant that communicates with candidates through streamed responses.

## 🚀 Features
- **ASGI-Based SSE Streaming**
- **CrewAI Integration for AI-Powered Conversations**
- **Django & Daphne Setup for ASGI Support**
- **Environment Variables Handling with `python-dotenv`**

---

## 🛠 Installation & Setup
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/django-sse-crewai.git
cd django-sse-crewai
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3️⃣ Create a `.env` File & Add API Key**
Create a `.env` file in the root directory:
```ini
GEMINI_API_KEY=your-google-gemini-api-key
```

🚨 **Don't commit `.env` to Git.** Add it to `.gitignore`.

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Run the ASGI Server with Daphne**
```sh
python manage.py runserver
```
Daphne is used because it supports **ASGI** (for SSE).

---

## 🏗 ASGI Configuration
### **Modify `settings.py`**
Ensure ASGI is properly configured:
```python
ASGI_APPLICATION = "sse_demo.asgi.application"
```

---

## 🔄 Streaming Server-Sent Events (SSE)
### **SSE View (`views.py`)**
```python
from django.http import StreamingHttpResponse
from django.shortcuts import render
import asyncio

async def sse_stream(request):
    async def event_stream():
        while True:
            yield "data: Hello from SSE!\n\n"
            await asyncio.sleep(1)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
```

### **Configure URL Routing (`urls.py`)**
```python
from django.urls import path
from .views import sse_stream

urlpatterns = [
    path("sse/", sse_stream, name="sse_stream"),
]
```


---

## 🎉 Conclusion
This project showcases how to integrate **CrewAI** with Django and **SSE streaming** using an **ASGI-compatible** setup with **Daphne**. 🚀

Feel free to contribute and improve the project! 😊

