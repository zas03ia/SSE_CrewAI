import asyncio
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .crew import CustomCrew


event=''
crew_executes = False
crew_started= False

# Task Callback Function
def task_callback(task):
    global event
    """Callback function to log task-agent mapping and send real-time updates."""
    task_info = f"agent: {task.agent}, description: {task.description}, task name: {task.name}"
    event= task_info


async def async_crew_execution():
    global event, crew_executes, crew_started
    candidate = "candy"
    user_input = "hi"
    inputs = {"candidate": candidate, "position": "Intern Software Engineer", "inquiry": user_input}
    crew = CustomCrew(task_callback).create_crew()
    result = await crew.kickoff_async(inputs=inputs)
    event = f"Final Response: {result}"
    await asyncio.sleep(1)
    crew_executes = False


async def sse_stream(request):
    """
    Sends server-sent events to the client.
    """
    global event, crew_executes, crew_started
    if not crew_started:
        crew_started = True
        crew_executes = True
        asyncio.create_task(async_crew_execution())
    async def event_stream():
        while crew_executes:
            yield f'data: {event}\n\n'
            await asyncio.sleep(0.2)

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def index(request):
    return render(request, 'index.html')
