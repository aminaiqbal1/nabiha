from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from servises.llms import gemini_llm

def call_chain(user_input=None): 
    prompt = ChatPromptTemplate.from_template("tell me five lines about {topic}")
    if user_input == StrOutputParser:  # Incorrect way to check

        chain = prompt | gemini_llm | StrOutputParser()
        result = chain.invoke({"topic": "python"})
        return result 
    else:
        chain = prompt | gemini_llm
        result = chain.invoke({"topic": "python"})
        return result.content  
# user_input = StrOutputParser()  
# print(call_chain(user_input))

print(call_chain())  
