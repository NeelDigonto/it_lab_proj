import crawler
import converter
import generator

if __name__ == "__main__":
    crawler.crawl()
    converter.convert()
    generator.parseAllFiles()
