from flask import Blueprint, render_template, request
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)
routes = Blueprint('routes', __name__)
history_list = []


@routes.route('/', methods=['GET', 'POST'])
def home():
    from website.models import Result

    if request.method == "GET":
        query = request.args.get('query')
        if query == "" or query is None:
            return render_template("response_view.html")
        answer = ask(query)
        data_list = []
        query_message = Result(time="12:00", message=query, message_type="query")
        response_message = Result(time="12:01", message=answer, message_type="response")
        data_list.append(query_message)
        data_list.append(response_message)
        history_list.append(query_message)
        history_list.append(response_message)
        return render_template("response_view.html", results=data_list)
    else:
        return render_template("history.html", results=history_list)


def ask(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message.content
    return answer
