
def get_response(question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": f"""
Use the SOP below to answer.

SOP:
{SOP_TEXT}

QUESTION:
{question}
"""
                }
            ]
        )

        answer = response.choices[0].message.content

        # ✅ fallback if AI gives weak answer
        if "not found" in answer.lower() or len(answer.strip()) < 20:
            return mock_ai_engine(question)

        return answer

    except Exception as e:
        # ✅ fallback if API fails (SSL, timeout, etc.)
        return mock_ai_engine(question)
def get_section(section_name):
    with open("SOP_data.txt", "r") as file:
        data = file.read()

    sections = data.split("[")

    for sec in sections:
        if sec.startswith(section_name):
            return "[" + sec.strip()

    return "SOP section not found."
