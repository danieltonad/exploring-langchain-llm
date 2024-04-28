from langchain_community.llms import openai
from langchain_core.prompts import PromptTemplate
# from langchain_community.cha
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type):
    llm = openai.OpenAI(temperature=0.7)
    
    prompt_template_name = PromptTemplate(
        input_variables=['animal_type'],
        template=f"i have a cat and an {animal_type}, suggest names for my {animal_type} that blends with my cat name `benny` "
    )
    
    # name = llm("i have a cat and an octopus, suggest names for my octopus that blends with my cat name `benny` ")
    
    return prompt_template_name

if __name__ == "__main__":
    print(generate_pet_name())