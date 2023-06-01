from elevenlabs import generate, play, set_api_key
import openai 

set_api_key("XXX") # add your ElevenLabs API key 
OPENAI_API_KEY = "XXX" # add your OpenAPI key 
openai.api_key = OPENAI_API_KEY 

def generate_reply(message: str): 

    messages = [ {"role": "user", "content": "XXX"},
    {"role": "user", "content": message} ] # in the first array object content, i.e. "XXX", add prompt for model, e.g. "Reply like a helpful assistant"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=messages 
    )

    return response.choices[0].message.content 

def play_audio(message: str): 

    audio = generate(
    text=generate_reply(message), 
    voice="Josh",
    model="eleven_monolingual_v1"
    )

    play(audio)

while True:
    user_input = input("Enter your text (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Exiting...")
        break

    print(generate_reply(user_input)) # print reply 

    play_audio(user_input) # play reply 
