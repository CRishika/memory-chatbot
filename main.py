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
    elif question.lower() == "history":
        print("\n----Chat history----")
        for message in messages:
            if message["role"] == "user":
                print("You: ",message["content"])
            elif message["role"] == "assistant":
                print("Bot: ",message["content"])
            print("--------------------\n")
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