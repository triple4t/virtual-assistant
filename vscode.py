import os
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


client = OpenAI()

def get_completion(prompt , model = "gpt-3.5-turbo"):
    messages = [
        {"role": "user", "content" : prompt},
    ]
    response = client.chat.completions.create(
        messages = messages,
        model = model,
        temperature = 0.5
    )
    return response.choices[0].message.content

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def createfile(audio):
    content = audio.lower()
    if "python" in audio.lower():

        
        with open("pytho" + "." + "py", "w") as f:        
            f.write(get_completion(content))

    elif "c plus plus" in audio.lower():
        with open("c plus plus" + "." + "cpp", "w") as f:        
            f.write(get_completion(content))
    
    elif "java" in audio.lower():
        with open("javafile" + "." + "java", "w") as f:        
            f.write(get_completion(content))
    
    elif "c program" in audio.lower():
        with open("cfile" + "." + "c", "w") as f:        
            f.write(get_completion(content))
    
    elif "javascript" in audio.lower():
        with open("javascriptfile" + "." + "js" , "w") as f:
            f.write(get_completion(content))

    else :
        with open("textfile" +"." +"txt", "w") as f:
            f.write(get_completion(content))