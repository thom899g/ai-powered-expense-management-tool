import spacy

class NLPCategorizer:
    """Handles categorization of expenses using NLP techniques."""
    
    def __init__(self, model_name='en_core_web_sm'):
        """Initialize with a spaCy model for processing."""
        self.nlp = spacy.load(model_name)
        
    def process_description(self, text):
        """Process expense description to extract entities and keywords."""
        doc = self.nlp(text.lower())
        categories = []
        for ent in doc.ents:
            if ent.label_ in ['ORG', 'GPE']:
                categories.append(ent.text)
        return categories[:1]  # Return only the most relevant category
    
    def categorize_expense(self, description):
        """Categorize an expense based on its description."""
        try:
            cats = self.process_description(description)
            if not cats:
                raise ValueError("No category identified.")
            return cats[0]
        except Exception as e:
            print(f"Categorization failed: {e}")
            return "uncategorized"