#CALLS HUGGINGFACE MODELS 

from transformers import pipeline

classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

def classify_symptoms(text):
    candidate_labels = ["flu", "covid-19", "diabetes", "heart disease"]
    output = classifier(text, candidate_labels)
    return output
