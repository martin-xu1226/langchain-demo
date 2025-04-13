from langchain_ollama import ChatOllama

llm = ChatOllama(model="deepseek-r1:7b", )

message = "Hello,who are you?"
response = llm.invoke(message)
print(response.content)

# ----------------------------------  Content  -----------------------------------
#
# Hello! I'm DeepSeek-R1, an artificial intelligence assistant created by DeepSeek. I'm at your service and would be delighted to assist you with any inquiries or tasks you may have.
#
# ----------------------------------  Content  -----------------------------------
