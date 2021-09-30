import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

class Transformer:
    def __init__(self, src="model/content/models/" , cuda = True, download_online = False):
        
        if(download_online == True):
            print("This function allows you to download transformers files online that are not available in your local.")
            src = "savasy/bert-base-turkish-sentiment-cased"
            
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        
        self.model = AutoModelForSequenceClassification.from_pretrained(src)
        self.tokenizer = AutoTokenizer.from_pretrained(src)
        self.pipeline = pipeline("sentiment-analysis", tokenizer=self.tokenizer, model=self.model,
                                 device=0 if device =="cuda:0" else -1)

    def analyse(self, text: str):
        return self.pipeline(text)[0]
    

model =  Transformer(cuda = False) 
model.analyse("Akif emre capoglu bugün okula mutlu bir şekilde gitti")
