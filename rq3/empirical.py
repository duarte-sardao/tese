from openai import OpenAI
from glob import glob
client = OpenAI(api_key="")


path = "P2"
for file in glob(path+"/*.txt"):
    prompt = open(file, 'r').read()

    chat_completion = client.chat.completions.create(
        messages=[
            { 
                "role": "system",
                "content": "You are a coding assistant. You generate only source code.",
            },
            { 
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.0
    ).choices[0].message.content


    f = open("Results/"+file, "a")
    f.write("Prompt:\n"+prompt+"\nCompletion:\n"+chat_completion)
    f.close()