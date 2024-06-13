import os
import re
import json
from langchain_community.document_loaders import AsyncChromiumLoader, AsyncHtmlLoader
from langchain_community.document_transformers import BeautifulSoupTransformer, Html2TextTransformer


URLS_PATH = "output/urls_filtered.json"


with open(URLS_PATH) as f:
    urls = json.load(f)
urls = [url['url'] for url in urls]


## Download documents
docs = AsyncChromiumLoader(urls[:]).load()
# docs2 = AsyncHtmlLoader(urls[:]).load()

## Extract texts
bs_transformer = BeautifulSoupTransformer()
texts = bs_transformer.transform_documents(
    docs,
    remove_comments=True,
)


def clean_text(text: str):
    url_pattern = re.compile(r'\(?(http[s]?://\S+)\)?')
    cleaned_text = re.sub(url_pattern, '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text


def get_filename(url: str):
    website = url.split('/')[2].replace('www.', '')
    other = '_'.join(url.split('/')[3:])
    file_name = f"{website}_{other}.txt"
    return file_name


## Write texts to files
metainfo = {}
url2id = {url: i for i, url in enumerate(urls)}
os.makedirs("output/texts", exist_ok=True)
for text in texts:
    url = text.metadata['source']
    id = url2id[url]
    file_name = f"{id:05d}.txt"
    text = clean_text(text.page_content)
    metainfo[id] = {
        'url': url,
        'file_name': file_name,
        'character_count': len(text),
    }
    with open(f"output/texts/{file_name}", "w") as f:
        f.write(text)

with open("output/texts_metainfo.json", "w") as f:
    json.dump(metainfo, f)