import requests
from bs4 import BeautifulSoup

download_links = {
    2017: [ #"https://aclanthology.org/volumes/I17-1/", #104
            #"https://aclanthology.org/volumes/I17-2/", #77
            #"https://aclanthology.org/volumes/I17-3/", #18
            #"https://aclanthology.org/volumes/I17-4/", #37
            "https://aclanthology.org/volumes/I17-5/", #7
            ],
    2019: [ #"https://aclanthology.org/volumes/D19-1/", #682
            #"https://aclanthology.org/volumes/D19-2/", #7
            #"https://aclanthology.org/volumes/D19-3/", #45
            ]
}

files_to_download = []

for conference_page_link in (download_links[2017] + download_links[2019]):

        page = requests.get(conference_page_link)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find_all("a", class_="badge badge-primary align-middle mr-1", href=True)

        for pdf_element in results:
                files_to_download.append(pdf_element["href"])


for index, pub_pdf_link in enumerate(files_to_download):
        response = requests.get(pub_pdf_link)
        with open(f"./assets/papers/IJCNLP/pdf/doc{index}.pdf", 'wb') as f:
                f.write(response.content)




