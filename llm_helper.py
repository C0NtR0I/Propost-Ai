from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-11b-vision-preview")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingredient in samosa are ")
    print(response.content)




