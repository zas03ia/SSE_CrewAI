import asyncio
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

event=1

@require_GET
async def sse_view(request):
    global event
    # Set the proper content type and cache control headers for SSE
    response = HttpResponse(content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    response['Connection'] = 'keep-alive'

    # Simulate sending events asynchronously
    response.write(f"data: Event {event}\n\n")
    event+=1
    # await asyncio.sleep(1)  # Use asyncio sleep for non-blocking delay

    return response
