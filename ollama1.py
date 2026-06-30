#GEN AI with OLLAMA LLAMA3.2
#pip install ollama
#ollama run llama3.2
import ollama
#User prompt
User_prompt = "How to create a Table in MYSQL?"
#Create the role and message for the ollama
Role_Message=[]
Role_Message = [{'role':'user','role':User_prompt}]
#to call the Ollama Chat()
Response_Data = ""
Streams = ollama.chat(model = "llama3.2",messages= Role_Message,stream=True)
for sent in Streams:
    Response_Data += sent["message"]["content"]
Role_Message.append({'role':"assistant",'role':Response_Data})
print("User Prompt: ",User_prompt)
print("Response from Ollama: ",Response_Data)