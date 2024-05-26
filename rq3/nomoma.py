from openai import OpenAI
from glob import glob
client = OpenAI(api_key="")

path = "P1"
for file in glob(path+"/*.txt"):
    splt = open(file, 'r').read().split('\n', 1)
    methodname = splt[0]
    classinfo = splt[1]

    prompt = classinfo + "\nPlease infer the intention of the " + methodname
    prompt2 = "You are a professional who writes Java test methods. Please write a test method for the " + methodname + " with the given Method intention."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    ).choices[0].message.content

    prompt2 = chat_completion + "\nYou are a professional who writes Java test methods. Please write a test method for the " + methodname + " with the given Method intention."


    chat_completion2 = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
            {
                "role": "assistant",
                "content": chat_completion,
            },
            {
                "role": "user",
                "content": prompt2,
            }
        ],
        model="gpt-3.5-turbo",
    ).choices[0].message.content

    f = open("Results/"+file, "a")
    f.write("Prompt:\n\n"+prompt+"\n\nCompletion:\n\n"+chat_completion+"\n\nPrompt 2:\n\n"+prompt2+"\n\nCompletion 2:\n\n" +chat_completion2)
    f.close()