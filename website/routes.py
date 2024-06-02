from flask import Blueprint, render_template, request
from openai import OpenAI

client = OpenAI(api_key='sk-chatbot-wCAWYUoRkTpsO2F66561T3BlbkFJq4ypl1aGBkfwMkoWTlc8')
routes = Blueprint('routes', __name__)
history_list = []


@routes.route('/', methods=['GET', 'POST'])
def home():
    from website.models import Result

    if request.method == "GET":
        query = request.args.get('query')
        if query == "" or query is None:
            return render_template("response_view.html")

        if query:
            answer = ask(query)

            data_list = []
            history = Result.query.all()
            query_message = Result(time="12:00", message=query, message_type="query")
            response_message = Result(time="12:01", message=answer, message_type="response")
            data_list.append(query_message)
            data_list.append(response_message)
            for item in history:
                history_list.append(item)
        return render_template("response_view.html", results=data_list)
    else:
        return render_template("history.html", results=history_list)


def ask(question, chat_log=None):
    prompt = f'{chat_log}Human: {question}\nAI:'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    answer = response.choices[0].message.content
    return answer
