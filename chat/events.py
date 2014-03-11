from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags
from django_socketio import events

from chat.models import ChatRoom


@login_required
@events.on_message(channel="^room-")
def message(request, socket, context, message):
    """
    Event handler for a room receiving a message. First validates a
    joining user's name and sends them the list of users.
    """
    room = get_object_or_404(ChatRoom, id=message["room"])
    name = strip_tags(message.get("name"))
    if not name:
        name = request.user.get_profile().get_pretty_name()
    user, created = room.users.get_or_create(name=name)
    context["user"] = user
    users = [u.name for u in room.users.all()] #exclude(id=user.id)]
    # if created:
    socket.send({"action": "started", "users": users})
    user.session = socket.session.session_id
    user.save()
    joined = {"action": "join", "name": user.name, "id": user.id}
    # socket.send_and_broadcast_channel(joined)

    message["message"] = strip_tags(message.get("message"))
    message["name"] = user.name
    socket.send_and_broadcast_channel(message)


@events.on_finish(channel="^room-")
def finish(request, socket, context):
    """
    Event handler for a socket session ending in a room. Broadcast
    the user leaving and delete them from the DB.
    """
    try:
        user = context["user"]
    except KeyError:
        return
    left = {"action": "leave", "name": user.name, "id": user.id}
    socket.broadcast_channel(left)
    user.delete()
