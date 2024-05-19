class OverviewModel:
    
    def __init__(self, 
                 IsFirstPageNo=None, 
                 CurrenPageNo = None, 
                 IsLastPageNo = None,
                 LastPageNo=None,
                 Table = None,
                 PageSize = None,
                 PageRange = None,
                 StartPaginationNo = None,
                 EndPaginationNo = None,
                 TotalRecordCount = None
                 ):

        self.IsFirstPageNo = IsFirstPageNo if IsFirstPageNo is not None else False      
        self.CurrenPageNo = CurrenPageNo if CurrenPageNo is not None else 1
        self.IsLastPageNo = IsLastPageNo if IsLastPageNo is not None else False
        self.LastPageNo = LastPageNo if LastPageNo is not None else 1
        self.Table = Table if Table is not None else []
        self.PageSize = PageSize if PageSize is not None else 10
        self.PageRange = PageRange
        self.StartPaginationNo = StartPaginationNo if StartPaginationNo is not None else 1
        self.EndPaginationNo = EndPaginationNo if EndPaginationNo is not None else 1
        self.TotalRecordCount = TotalRecordCount if TotalRecordCount is not None else 0    
    
    def GetPaginationInfo(self):
        return  {
            "IsFirstPageNo" : self.IsFirstPageNo,
            "CurrenPageNo" : self.CurrenPageNo,
            "IsLastPageNo" : self.IsLastPageNo,
            "LastPageNo" : self.LastPageNo,
            "Table" : self.Table,
            "PageSize" : self.PageSize,
            "PageRange" : self.PageRange,
            "StartPaginationNo" : self.StartPaginationNo,
            "EndPaginationNo" : self.EndPaginationNo,
            "TotalRecordCount" : self.TotalRecordCount,
        }
    
            
    