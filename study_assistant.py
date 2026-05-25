import csv
from typing import List
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

# --- 1. DEFINE THE EXACT SCHEMA WE WANT ---
class Flashcard(BaseModel):
    word: str = Field(description="The foreign word or phrase from the text")
    pronunciation: str = Field(description="The pronunciation guide (e.g., Romaji or Pinyin)")
    meaning: str = Field(description="The accurate English translation")

class VocabularyList(BaseModel):
    cards: List[Flashcard] = Field(description="A list of exactly 3 key vocabulary flashcards")

# --- 2. CONFIGURING THE MODEL WITH STRUCTURED OUTPUT ---
llm = ChatOllama(model="llama3.1", temperature=0.1)
# This forces Llama 3.1 to return data matching our schema perfectly
structured_llm = llm.with_structured_output(VocabularyList)

# --- 3. THE PROMPT ---
system_instruction = (
    "You are an expert language translation assistant. Analyze the provided text "
    "and extract exactly 3 key vocabulary words or phrases present in the input text."
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_instruction),
    ("user", "Analyze this text and extract 3 cards:\n\n{text_input}")
])

processing_pipeline = prompt | structured_llm

def generate_flashcards(input_text):
    print("🤖 Streaming structured data from local Llama 3.1...")
    
    # The response here isn't raw text—it's a clean Python object!
    result = processing_pipeline.invoke({"text_input": input_text})
    
    print("\n--- Model Structured Output ---")
    output_csv = "anki_cards.csv"
    
    with open(output_csv, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")  # Tab-separated for Anki
        
        for card in result.cards:
            print(f"🔹 {card.word} | {card.pronunciation} | {card.meaning}")
            writer.writerow([card.word, card.pronunciation, card.meaning])
            
    print("--------------------------------\n")
    print(f"✅ Pristine compilation complete! Saved to: {output_csv}")

if __name__ == "__main__":
    sample_text = "すみません、駅はどこですか？"
    generate_flashcards(sample_text)