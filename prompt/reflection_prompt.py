REFLECTION_PROMPT = '''
Question: {question}

# solution in Python:
{generated_code}

You are a helpful assistant that is a multilingual expert and a Python code engineer.
Your task is to review the Python code above which intended to solve the `Question`. Identify and fix any potential errors, paying close attention to:
1.  **Context/Assumptions:** Did the code correctly capture all the conditions and implicit assumptions?
2.  **Language/Terminology:** Are chinese mathematical terms handled correctly? Are there ambiguous phrases in the question that could lead to different coded interpretations?
3.  **Units/Output Format:** Does the result match the question's required format/units? Does the code calculate the answer for the correct subject asked for in the question?
4.  **Python Implementation:** Are the Python syntax and logic correct when solve a question by setting up equations. Are variables used before they are defined?

Please only return the refined Python code without any explanation.
'''.strip() + '\n\n\n'