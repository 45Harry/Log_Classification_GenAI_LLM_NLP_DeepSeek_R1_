from dotenv import load_dotenv
from groq import Groq
load_dotenv()


groq = Groq()

def classify_with_llm(log_msg):


    prompt = f"""Classify the log message into one of these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    if you can't figure out a category, return 'Unclassified.'.
    Only return the category name. No preamble.
    Log message: {log_msg}"""
    chat_completion = groq.chat.completions.create(
        model = 'llama-3.3-70b-versatile',
       # model = 'meta-llama/llama-4-maverick-17b-128e-instruct' , # we can also use 'deepseek-r1-distill-llama-70b'
        messages=[{
            'role':'user',
            'content':prompt
        }]
    )

    return chat_completion.choices[0].message.content


if __name__ == '__main__':
    print(classify_with_llm(
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."))
    print(classify_with_llm(
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"))
    print(classify_with_llm("System reboot initiated by user 12345."))