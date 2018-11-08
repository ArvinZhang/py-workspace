# coding utf-8
import urllib
import re
from __builtin__ import str

path = "/Users/arvin.chang/Images/webCrawler/";


def getHTMLByURL(url):
    print url;
    page = urllib.urlopen(url);
    html = page.read();
    return html;


def getImg(html):
    #     print html;
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg);
    imgList = re.findall(imgre, html);
    print imgList;
    return imgList;


def wirteImg(imgList, x):
    y = 1;
    for imgurl in imgList:
        print imgurl
        z = str(x) + "-" + str(y);
        urllib.urlretrieve(imgurl, path + '%s.jpg' % z);
        y += 1;


def main():
    for index in range(1, 20):
        html = getHTMLByURL("http://www.dbmeinv.com/dbgroup/show.htm?cid=6&pager_offset=" + str(index));
        #         wirteImg(getImg(html),index);
        index += 1;


if __name__ == '__main__':
    main();