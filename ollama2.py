#GEN AI with OLLAMA LLAMA3.2 with dynamic user Prompt
import ollama


def stream_response(prompt):
    Role_Message=[]
    Role_Message = [{'role':'user','role':User_prompt}]
    Response_Data = ""
    Streams = ollama.chat(model = "llama3.2",messages= Role_Message,stream=True)
    for sent in Streams:
        Response_Data += sent["message"]["content"]
    Role_Message.append({'role':"assistant",'role':Response_Data})
    return Response_Data

def user_prompt():
    user_prompt=input("Enter the prompt: ")
    return user_prompt

while True:
    user_text=user_prompt()
    if user_text.lower() == "100":
        break
    response=stream_response(user_text)
    print("Response from ollama: ",response)