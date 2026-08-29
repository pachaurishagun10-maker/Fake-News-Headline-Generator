import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client=Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

command='''
[19:30 , 10/5/2025] rio:Hello! kaisa hai?
[19:30 , 10/5/2025] juhu:Badhiya tu bata kaise yaad kia
[19:30 , 10/5/2025] rio:I'm also good,Mujhe kuch books suggest kar as a beginner
[19:30 , 10/5/2025] juhu:Achaa!!Try reading , The Alchemist,Subtle Art of not giving a f*ck,Gone Girl 
[19:30 , 10/5/2025] rio:Acha great yaar, i'm trying to build reading habit
[19:30 , 10/5/2025] juhu:Great!! That's really good let me know kaisi lagi, I'd love to listen
[19:30 , 10/5/2025] rio:sure!!Thank you so much
[19:30 , 10/5/2025] juhu:No worries!!Most Welcome.
'''
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system","content": "You are a person named Juhu who speaks hindi and english.He is from India and is a engineer.You analyze chat history and respond like Juhu"},
            
            {"role": "user","content":Command}
        ]
    )

    return completion.choices[0].message.content