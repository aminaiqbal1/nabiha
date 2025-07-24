from langchain_core.prompts import PromptTemplate


def prompt_template_func(topic):
    """
    Generates a prompt template for a given topic.
    
    Args:
        topic (str): The topic to generate a prompt for.
        
    Returns:
        str: The generated prompt.
    """
    prompt_template = PromptTemplate.from_template("Tell me a joke about {topic}")
    generated_prompt = prompt_template.invoke({"topic": topic})
    return generated_prompt

