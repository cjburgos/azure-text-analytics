from analytics.text_analytics import AzureTextAnalytics

import pandas as pd
import uuid
import yaml

# Loads the configuration from APP.YAML located on the CONFIG folder
with open('config/app.yaml') as f:
    Config = yaml.load(f,Loader=yaml.FullLoader)

TextAnalyticsService = AzureTextAnalytics()

# Reads excel input file and converts it to Dataframe
Data = pd.read_excel(Config['input_filename'])

document_list = []

# Generates "document" objects for further processing
for i,d in Data.iterrows():
    report_id = uuid.uuid4()
    report_template = {
        "id": str(report_id),
        "text": d[Config['target_column']],
        "language": "en"
    }

    document_list.append(report_template)

#SR_Final_Report_List = []
ER_Final_Report_List = []

# For each "document" object, prepare a sentiment analysis report and an entity recognition report
for document in document_list:
    # SentimentResponse = TextAnalyticsService.sentiment_analysis([document])
    EntityReport = TextAnalyticsService.entity_recognition([document])
    
    # [ SR_Final_Report_List.append(SR) for SR in SentimentResponse ] 
    [ ER_Final_Report_List.append(ER) for ER in EntityReport ]

# SR_DF = pd.DataFrame(SR_Final_Report_List)
ER_DF = pd.DataFrame(ER_Final_Report_List)
