# Indexing Jabra KB Using the Generic REST API Connector

## Use Case
This shows how to index the KB articles from Jabra.

## Prerequisites
To fully understand how to use this example, you must:
1. Have a Coveo Platform organization.
2. Learn about [Coveo Connectivity](https://docs.coveo.com/en/1702/).
3. Learn [how to configure a Generic REST API source](https://docs.coveo.com/en/1896/).

## Background
The KB is working with a `groupid`, those `groupids` cannot be retrieved. It is a static list.
Popular groupid's:
Elite 65t: 1222
Elite 75t: 1489
Elite Active 75t: 1515
Elite 85h: 1391
Elite 85t: 1673
Evolve 65: 182
Evolve 75: 1155
Engage 65: 1240
Engage 75: 1243
Evolve2 65: 1576

### API calls
#### /v1/group/{id}/documents
Retrieves all documents assigned to the `groupid (id)`.
Fields: group (static), model (static), languageCode, languageTitleEn, languageTitleLocal, fileType, documentType, fileUrl (location to download the file)

#### /v1/group/{id}/frequentlyaskedquestions
Retrieves asked questions for the `groupid (id)`.
Fields: group (static), model (static), answer, categoryTitle, question, requiredSoftware[*].text, didYouKnow, types, documentType (static=FAQ)

#### /v1/group/{id}/videos
Retrieves related videos for the `groupid (id)`.
Fields: group (static), model (static), documentType (static=Videos), headline, description, videoId (add prefix: https://www.youtube.com/watch?v=), assign Youtube fields

#### /v1/group/{id}/bluetoothpairingguides
Retrieves bluetooth for the `groupid (id)`.
Fields: group (static), model (static), documentType (static=Pairing Guide), platform.label, platform.icon, title (Pairing guide for %[model] - %[platform.label])


## Instructions
1. [Create a API Key](https://developer.jabra.com/site/global/home/index.gsp).
2. Use the `Access Token` as `API Key` in your Generic Rest configuration.
3. [Create a Generic REST API Source](https://docs.coveo.com/en/1896/). 
4. Add the  [NormalConfig.json](https://github.com/coveooss/connectivity-library/blob/master/JabraKB/index/NormalConfig.json). 
5. Add the  [NormalConfigDocs.json](https://github.com/coveooss/connectivity-library/blob/master/JabraKB/index/NormalConfig.json) to another source. The `NormalConfigDocs` is being used to index the PDFs (this is a slower process to index because each pdf needs to be downloaded). 
5. Add the Extension script [FixHTML.py](https://github.com/coveooss/connectivity-library/blob/master/JabraKB/FixHTML.py) to your organization.
6. Assocatie the Extension script to the 2 `Sources`.
7. Make sure you've changed all placeholders in the configuration with your own values.
8. [Create the appropiate fields and mappings](https://docs.coveo.com/en/1896/#completion).

## Content indexed
* /documents
* /frequentlyaskedquestions
* /videos
* /bluetoothpairingguides


Documents are completely downloaded and full text indexed.



## Reference
https://knowledgebaseapi.jabra.com/swagger/ui/index#!/group/Group_GetDocuments


## Version
1.0 July 2021, Wim Nijmeijer

