## Getting Started

In an empty folder open cmd and enter

```bash
git clone https://github.com/fanthomless/it_lab_proj.git
```

Then install the following packages:

```bash
pip install requests
pip install beautifulsoup4
pip install pymupdf
```

Then run main.py by invoking the following command

```bash
python main.py #script to run all code
```

To run the crawler and converter scripts seperately run the following commands in succession.

```bash
python crawler.py   #script to download the pdf files
python converter.py #script to convert all the pdf files to .txt and .xml
```

Check the folder for the generated files
