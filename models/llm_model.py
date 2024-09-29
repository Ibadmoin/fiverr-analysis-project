# llm model file
# llm_model.py
from transformers import pipeline

def get_service_suggestions(subcategory):
    generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
    prompt = f"Suggest popular services for the subcategory {subcategory}."
    
    response = generator(prompt, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == '__main__':
    subcategory = "logo design"
    suggestions = get_service_suggestions(subcategory)
    print(suggestions)
