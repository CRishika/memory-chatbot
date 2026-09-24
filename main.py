from ollama import chat

print("Synora - A chatbot hat Remembers")
messages = []
messages.append({
    "role":"system",
    "content":"Answer in a sentence of around 50 words max"
    })
    
while True:
    question = input("You: ").strip()
    if question.lower() == "exit":
        print("Good bye")
        break
    else:
        messages.append({
            "role":"user",
            "content":question
        })
        response = chat("gemma3:latest",messages=messages)
        answer = response.message.content
        messages.append({
            "role":"assistant",
            "content":answer
        })
        print("Bot: ",answer)