import flet as ft 
from assistant import Assistant 

class Message(): 
	def __init__(self, user: str, text: str, message_type: str): 
		self.user = user 
		self.text = text 
		self.message_type = message_type 

def main(page: ft.Page): 
	page.title = "Chat Client"

	chat = ft.Column() 
	new_message = ft.TextField() 

	# creating the object of Assistant class
	assistant = Assistant() 

	def join_click(e): 
		if not user_name.value: 
			user_name.error_text = "Name cannot be blank!"
			user_name.update() 
		else: 
			page.session.set("user_name", user_name.value)
			page.dialog.open = False 
			page.pubsub.send_all(Message(user=user_name.value, text=f"{user_name.value} has joined the chat.", message_type="login_message"))
			page.update() 

	def send_click(e):
		page.pubsub.send_all(Message(user=page.session.get('user_name'), text=new_message.value, message_type="chat_message"))

		# fetching the AI response
		ai_reply = assistant.AssistantResponse(str(new_message.value))
		page.pubsub.send_all(Message(user="Josh", text=str(ai_reply), message_type="chat_message"))

		new_message.value = ""
		page.update() 

	user_name = ft.TextField(label="Enter your name")

	def on_message(message: Message): 
		if message.message_type == "chat_message": 
			chat.controls.append(ft.Text(f"{message.user}: {message.text}")) 
		elif message.message_type == "login_message":
			chat.controls.append(ft.Text(message.text, italic=True, color=ft.colors.WHITE, size=12))
		page.update()

	page.pubsub.subscribe(on_message) 

	page.dialog = ft.AlertDialog(
        open=True,
        modal=True,
        title=ft.Text("Welcome!"),
        content=ft.Column([user_name], tight=True),
        actions=[ft.ElevatedButton(text="Join chat", on_click=join_click)],
        actions_alignment="end",
    )

	page.add( 
		chat,
		ft.Row(controls=[new_message, ft.ElevatedButton("Send", on_click=send_click)])

	)

ft.app(target=main)


