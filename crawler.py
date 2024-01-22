class Author():
    def __init__(self, account, nickname, followNewArticle, followNewUpvote):
        self.account = account
        self.nickname = nickname
        self.followNewArticle = followNewArticle
        self.followNewUpvote = followNewUpvote

class Board():
    def __init__(self, name, url, followedAuthorList):
        self.name = name
        self.url = url
        self.followedAuthorList = []
        self.AddFollowedAuthors(followedAuthorList)
    
    def AddFollowedAuthors(self, followedAuthorList):
        try:
            if followedAuthorList is not None:
                if isinstance(followedAuthorList, list):
                    if len(followedAuthorList) > 0:
                        for author in followedAuthorList:
                            if ("account" in author and author["account"] is not None)\
                                and ("nickname" in author)\
                                and ("followNewArticle" in author and author["followNewArticle"] is not None)\
                                and ("followNewUpvote" in author and author["followNewUpvote"] is not None):
                                    nickname = author["nickname"].strip() if isinstance(author["nickname"], str) else ""
                                    self.followedAuthorList.append(Author(author["account"], nickname, author["followNewArticle"], author["followNewUpvote"]))
        except Exception as e:
            raise Exception(f"追蹤作者的設定不符合格式: {e}")

class Crawler():
    def __init__(self, crawlBoardList=None):
        self.results = []
        self.crawlBoardList = []
        self.AddCrawlBoard(crawlBoardList)

    def AddCrawlBoard(self, crawlBoardList):
        try:
            if crawlBoardList is None:
                print("未設定任何欲追蹤的看板")
            else:
                if isinstance(crawlBoardList, list):
                    if len(crawlBoardList) > 0:
                        for board in crawlBoardList:
                            if ("name" in board and board["name"] is not None)\
                                and ("url" in board and board["url"] is not None)\
                                and ("followedAuthors" in board and board["followedAuthors"] is not None):
                                    self.crawlBoardList.append(Board(board["name"], board["url"], board["followedAuthors"]))
        except Exception as e:
            raise Exception(f"追蹤看板的設定不符合格式: {e}")

    def Start(self):
        print('start to crawl')
        
        #print(self.crawlBoardList)
        for board in self.crawlBoardList:
            # print(f"name: {board.name}")
            # print(f"url: {board.url}")
            # print(f"author List:")
            for a in board.followedAuthorList:
                # print(f" account: {a.account}")
                # print(f" nickname: {a.nickname}")
                # print(f" followNewArticle: {a.followNewArticle}" )
                # print(f" followNewUpvote: {a.followNewUpvote}" )
                self.results.append(a.account)

        return self.results