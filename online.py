import pywhatkit
import requests
import wikipedia
from langchain.chat_models import ChatOpenAI
import os
from email.message import EmailMessage
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["WOLFRAM_ALPHA_APPID"] = os.getenv("WOLFRAM_ALPHA_APPID")

def find_my_ip():
    ip_address = requests.get("https://api.ipify.org?format=json").json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query,sentences = 2)
    return results

def youtube(video):
    pywhatkit.playonyt(video)

def search_on_google(query):
    pywhatkit.search(query)


def get_news(general):
    news_headlines = []
    results = requests.get("https://newsapi.org/v2/top-headlines?country=us&category=general&apiKey=4345e0f5784a4744b35dcd3c1c1a8a43").json()

    articles = results["articles"]

    for article in articles :
        news_headlines.append(article["title"])
        return news_headlines[:6]
    

from langchain.agents import (
    AgentExecutor, AgentType, initialize_agent, load_tools
)

def chatgpt(query):
    # client = ChatOpenAI()
    # completion = client.chat.completions.create(
    # model="gpt-3.5-turbo",
    # messages=[
    # {"role": "system", "content": "You are a helpful assistant, skilled in explaining complex concepts with creative flair."},
    # {"role": "user", "content": query}
    #     ]
    # )
    # # print(completion.choices[0].message.content)
    # return completion.choices[0].message.content

    def load_agent() -> AgentExecutor:
        llm = ChatOpenAI(temperature=0, streaming=True)
        # DuckDuckGoSearchRun, wolfram alpha, arxiv search, wikipedia # TODO: try wolfram-alpha!
        tools = load_tools(
                tool_names=["ddg-search", "wolfram-alpha", "arxiv", "wikipedia"],
        llm=llm )
        return initialize_agent(
                tools=tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True,
        verbose=True
            )
    
    chain = load_agent()
    response = chain.run(query)
    return response
