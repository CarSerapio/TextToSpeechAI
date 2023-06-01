from elevenlabs import generate, play, set_api_key
import openai 

set_api_key("e4e86b6ed2c835295abb2df1d12ad231") 
OPENAI_API_KEY = "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" 
openai.api_key = OPENAI_API_KEY 

def generate_reply(message: str): 

    messages = [ {"role": "user", "content": "Reply like you are a 19 year old college male and the user's best friend."},
    {"role": "user", "content": message} ]

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