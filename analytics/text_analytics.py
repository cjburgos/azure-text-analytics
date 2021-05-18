from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

import yaml

with open('config/secret.yaml') as f:
    secret = yaml.load(f,Loader=yaml.FullLoader)
    Credentials = secret['secret']

def authenticate_client(credentials):
    ta_credential = AzureKeyCredential(credentials['key'])
    text_analytics_client = TextAnalyticsClient(
        endpoint=credentials['endpoint'],
        credential=ta_credential
    )
    return text_analytics_client

class AzureTextAnalytics():
    def __init__(self):
        self.client = authenticate_client(Credentials)
        
    def sentiment_analysis(self,list_of_documents: list ):     
        
        response = self.client.analyze_sentiment(list_of_documents)

        for res in response:
           [ d.update({'sentiment':res.sentiment}) for d in list_of_documents if d['id'] == res['id'] ]
           [ d.update({'confidence_positive':res.confidence_scores.positive}) for d in list_of_documents if d['id'] == res['id']  ]
           [ d.update({'confidence_neutral,':res.confidence_scores.neutral}) for d in list_of_documents if d['id'] == res['id']  ]
           [ d.update({'confidence_negative,':res.confidence_scores.negative}) for d in list_of_documents if d['id'] == res['id'] ]
        
        return list_of_documents

    def entity_recognition(self,list_of_documents):
        try:
            response = self.client.recognize_entities(documents=list_of_documents)

            list_of_results = []
            for res in response:
                for entity in res.entities:
                    report_template = {
                                "id":res.id,
                                "text":entity.text,
                                "category":entity.category,
                                "subcategory":entity.subcategory,
                                "confidence_score":entity.confidence_score
                            }
                    list_of_results.append(report_template)
            
            return list_of_results

        except Exception as err:
            print("Encountered exception. {}".format(err)) 
    
