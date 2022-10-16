import os 
from google.cloud import language_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/cynthiazu/Downloads/phonic-embassy-364516-337791661946.json"

client = language_v1.LanguageServiceClient()

text = u"test"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))