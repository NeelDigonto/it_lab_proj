import crawler
import converter

if __name__ == "__main__" :
    print("Crawling the website and downloading the Papers....")
    crawler.crawl()
    print("Papers Downloaded\n")

    print("Converting the downloaded Reseach Papers....")
    converter.convert()
    print("Papers Converted")