# blog/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from langchain_groq import ChatGroq

# Initialize the Groq model
llm = ChatGroq(
    temperature=0, 
    groq_api_key='YOUR_API_KEY', 
    model_name="llama3-70b-8192"
)

@csrf_exempt
def suggest_titles(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            blog_content = body.get('content', '')

            if not blog_content:
                return JsonResponse({"error": "No content provided."}, status=400)

            # Create a prompt for Groq
            prompt = f"""
Read the following blog content carefully and suggest exactly 3 suitable, catchy, and professional blog post titles:

Blog Content:
\"\"\"
{blog_content}
\"\"\"

Titles:
1.
2.
3.
"""

            response = llm.invoke(prompt)
            generated_text = response.content

            # Parse the 3 titles cleanly
            titles = parse_titles(generated_text)

            return JsonResponse({"titles": titles})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "POST request required."}, status=405)

def parse_titles(generated_text):
    """
    Parse the output text and extract clean 3 titles.
    """
    lines = generated_text.strip().split("\n")
    titles = []
    for line in lines:
        line = line.strip()
        if line and (line[0].isdigit() or line.startswith("-")):
            # Remove leading number/dash
            parts = line.split('.', 1)
            if len(parts) > 1:
                title = parts[1].strip()
                if title:
                    titles.append(title)
            else:
                titles.append(line.strip("-").strip())
    return titles[:3]  # Return first 3 titles
