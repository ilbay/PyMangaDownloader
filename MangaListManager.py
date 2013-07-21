import os
from lxml import etree

class MangaListManager:
        def __init__(self):
                self._filename = "manga.xml"

                if not os.path.isfile(self._filename):
                        mangaXML = open(self._filename, "w")
                        mangaXML.write("<mangaList></mangaList>")
                        mangaXML.close()

        def getMangaList(self):
                return self._mangaList

        def update(self, manga):
                tree = etree.parse(self._filename)
                mangaXmlList = tree.xpath("/mangaList/manga")
                for mangaXml in mangaXmlList:
                        mangaName = mangaXml.xpath("name")[0].text
                        if mangaName == manga["name"]:
                                mangaXml.xpath("status")[0].text = manga["status"]
                                mangaXml.xpath("latestChapter")[0].text = manga["latestChapter"]
                                mangaXml.xpath("link")[0].text = magan["link"]
                                break

                mangaFile = open(self._filename, "w")
                mangaFile.write(etree.tostring(tree.getroot()))
                mangaFile.close()

        def add(self,manga):
                tree = etree.parse(self._filename)
                root = tree.getroot()

                mangaElement = etree.SubElement(root,"manga")

                nameElement = etree.SubElement(mangaElement,"name")
                nameElement.text = manga["name"]

                statusElement = etree.SubElement(mangaElement, "status")
                statusElement.text = manga["status"]

                latestChapterElement = etree.SubElement(mangaElement, "latestChapter")
                latestChapterElement.text = manga["latestChapter"]

                linkElement = etree.SubElement(mangaElement, "link")
                linkElement.text = manga["link"]

                mangaFile = open(self._filename, "w")
                mangaFile.write(etree.tostring(root))
                mangaFile.close()

        def read(self):
                mangaList = []
                tree = etree.parse(self._filename)
                mangaXmlList = tree.xpath("/mangaList/manga")
                for manga in mangaXmlList:
                        dic = {}
                        dic["name"] = manga.xpath("name")[0].text
                        dic["status"] = manga.xpath("status")[0].text
                        dic["latestChapter"] = manga.xpath("latestChapter")[0].text
                        dic["link"] = manga.xpath("link")[0].text
                        mangaList.append(dic)
                return mangaList
