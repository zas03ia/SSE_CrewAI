import asyncio
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .crew import CustomCrew


async def sse_stream(request):
    """
    Sends server-sent events to the client.
    """
    process = {
        "event": "Process Initialized....",
        "crew_executes": False,
    }

    # Task Callback Function
    def task_callback(task):
        """Callback function to log task-agent mapping and send real-time updates."""
        task_info = f"agent: {task.agent}, description: {task.description}, task name: {task.name}"
        process["event"] = task_info

    async def async_crew_execution():
        candidate = "candy"
        user_input = "hi"
        inputs = {
            "candidate": candidate,
            "position": "Intern Software Engineer",
            "inquiry": user_input,
        }
        crew = CustomCrew(task_callback).create_crew()
        result = await crew.kickoff_async(inputs=inputs)
        process["event"] = f"Final Response: {result}"
        await asyncio.sleep(1)
        process['crew_executes'] = False

    process['crew_executes'] = True
    asyncio.create_task(async_crew_execution())

    async def event_stream():
        while process['crew_executes']:
            yield f"data: {process['event']}\n\n"
            await asyncio.sleep(0.2)

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


def index(request):
    return render(request, "index.html")
