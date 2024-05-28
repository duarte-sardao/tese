from openai import OpenAI
from glob import glob
client = OpenAI(api_key="")

path = "P3"
for file in glob(path+"/*.txt"):
    splt = open(file, 'r').read().split('\n', 2)
    methodname = splt[0]
    classname = splt[1]
    classinfo = splt[2]

    prompt = "Please help me generate a whole JUnit test for a focal method in a focal class. I will provide the following information: \n1. Required dependencies to import.\n2. The focal class signature.\n3. Source code of the focal method.\n4. Signatures of other methods and fields in the class.\nI need you to create a whole unit test using JUnit 4 and Mockito 3, ensuring optimal branch and line coverage. The test should include necessary imports for JUnit 4 andMockito 3, compile without errors, and use reflection to invoke private methods. No additional explanations required.\n\nThe focal method is " + methodname + " in focal class " + classname + ", the information is " + classinfo

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        temperature=0.5
    ).choices[0].message.content


    f = open("Results/"+file, "a")
    #f.write("Prompt:\n"+prompt+"\nCompletion:\n"+chat_completion)
    f.write("\n\nCompletion:\n"+chat_completion)
    f.close()