from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

def generate_outline(topic, references):
    # Gabungkan referensi menjadi satu string
    context = "\n".join(references)
    
    # Buat prompt untuk GPT
    prompt = f"""
Topik: {topic}
Referensi:
{context}

Buatlah kerangka topik yang terstruktur dengan baik berdasarkan topik dan referensi di atas.
"""
    
    # Inisialisasi model GPT
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
    
    # Dapatkan respons dari model
    response = chat([HumanMessage(content=prompt)])
    
    # Kembalikan hasil sebagai string
    return response.content
