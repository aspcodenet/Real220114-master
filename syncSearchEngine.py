import os
from models import Company

from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import ( 
    ComplexField, 
    CorsOptions, 
    SearchIndex, 
    ScoringProfile, 
    SearchFieldDataType, 
    SimpleField, 
    SearchableField 
)

index_name = "company0208"
# Get the service endpoint and API key from the environment
endpoint = "https://stefanpersonsearch.search.windows.net"
key = "F4B85AB85B8662E8B66EACDF1B98E581"

# Create a client
credential = AzureKeyCredential(key)


client = SearchClient(endpoint=endpoint,
                      index_name=index_name,
                      credential=credential)

def createIndex():
    return
    searchIndexClient = SearchIndexClient(endpoint=endpoint,
                        index_name=index_name,
                        credential=credential)

    fields = [
            SimpleField(name="id", type=SearchFieldDataType.String, key=True),
            SearchableField(name="name", type=SearchFieldDataType.String, sortable=True),
            SearchableField(name="city", type=SearchFieldDataType.String,sortable=True),
            SearchableField(name="street", type=SearchFieldDataType.String,sortable=True)
        ]
    cors_options = CorsOptions(allowed_origins=["*"], max_age_in_seconds=60)
    scoring_profiles = []

    index = SearchIndex(
        name=index_name,
        fields=fields,
        scoring_profiles=scoring_profiles,
        cors_options=cors_options)

    result = searchIndexClient.create_index(index)                      


def addDocuments():
    return
    docs = []
    for company in Company.query.all():
        d = {
               "id" : str(company.id),
               "name": company.namn,
               "city": company.city,
               "street": company.street
        }
        docs.append(d)
    result = client.upload_documents(documents=docs)
    

