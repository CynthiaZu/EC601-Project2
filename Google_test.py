# Imports the Google Cloud client library
import os 
from google.cloud import language_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/cynthiazu/Downloads/phonic-embassy-364516-337791661946.json"
# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = u"Hello, world!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))