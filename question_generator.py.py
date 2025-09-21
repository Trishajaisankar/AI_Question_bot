import openai
import pandas as pd
OPENAI_API_KEY =#Your API
syllabus_df = pd.read_csv(r"C:\Users\user\Desktop\ai_question_bot\syllabus.csv.csv")
questions_df = pd.read_csv(r"C:\Users\user\Desktop\ai_question_bot\questions.csv.csv")

def get_topics(subject):
    return syllabus_df[syllabus_df['subject'].str.lower() == subject.lower()]['topic'].tolist()

def get_past_questions(subject):
    return questions_df[questions_df['subject'].str.lower() == subject.lower()]['question'].tolist()

def ask_gpt(prompt, model="gpt-3.5-turbo"):
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

def generate_questions(subject, num_questions=5):
    topics = get_topics(subject)
    past_questions = get_past_questions(subject)
    prompt = f"""
You are an exam paper generator bot.
Syllabus topics: {topics}
Past year questions: {past_questions[:5]}
Generate {num_questions} new, university-level exam questions for {subject}, mixing syllabus and similar style to past questions.
Return only the questions.
"""
    questions = ask_gpt(prompt)
    return questions

if __name__ == "__main__":
    subject = input("Enter subject (e.g., Artificial Intelligence): ")
    num_questions = int(input("How many questions?: "))
    print("Generating questions...")
    print(generate_questions(subject, num_questions))