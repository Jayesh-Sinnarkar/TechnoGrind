from django.shortcuts import render
import pdb
from .models import Employee
from Helper import DatabaseHelper as dbHelper
from django.http import JsonResponse
from PaginationModels.OverviewModel import OverviewModel

def GetPageInfo(totalRecordsCount, pageSize, currentpageNo):
    
    totalPages = totalRecordsCount//pageSize
    firstPageNo = 1
    startPaginationNo = 1
    endPaginationNo = totalPages
    lastPageNo = totalPages 
    
    if (currentpageNo-1) > 0:
        startPaginationNo = currentpageNo-1
    
    if currentpageNo + 1 <= totalPages:
        endPaginationNo = currentpageNo + 2        

    pageRange = range(startPaginationNo, endPaginationNo)

    pageInfo = {
        "firstPageNo" : firstPageNo,
        "pageRange": pageRange,
        "startPaginationNo": startPaginationNo,
        "endPaginationNo": endPaginationNo,
        "isLastPage" : lastPageNo > 0, 
        "lastPageNo": lastPageNo,
        "currentpageNo" : currentpageNo,
        "totalRecordsCount" : totalRecordsCount
    }
    
    return pageInfo    

def Overview(request):    
    if request.method == "GET":
        pageNo = 1
        pageSize = 10

        query = f"CALL GetEmployeesByPage({pageNo}, {pageSize});"        
        success, result = dbHelper.SelectQueryListDict(query)
        
        columns = list(result[0].keys())
        
        totalRecordsCount = Employee.objects.count()

        pageInfo = GetPageInfo(totalRecordsCount, pageSize, pageNo)

        overviewModel = OverviewModel(
        IsFirstPageNo=totalRecordsCount>0,
        CurrenPageNo=pageNo,
        IsLastPageNo=pageInfo["isLastPage"],
        LastPageNo=pageInfo["lastPageNo"],
        Table=result,
        PageSize=pageSize,
        PageRange=pageInfo["pageRange"],
        TotalRecordCount=totalRecordsCount,
        Columns=columns
        )
        
        OverviewData = overviewModel.GetPaginationInfo()
        
        if success:
            return render(request, template_name="EmployeeApp/index.html", context={
                'OverviewData':OverviewData,
            })    
    else:
        pageNo = int(request.POST["pageNo"])
        pageSize = int(request.POST["pageSize"])

        query = f"CALL GetEmployeesByPage({pageNo}, {pageSize});"
        
        success, result = dbHelper.SelectQueryListDict(query)
        
        columns = list(result[0].keys())
        
        totalRecordsCount = Employee.objects.count()
        
        pageInfo = GetPageInfo(totalRecordsCount, pageSize, pageNo)
        
        overviewModel = OverviewModel(
        IsFirstPageNo=totalRecordsCount>0,
        CurrenPageNo=pageNo,
        IsLastPageNo=pageInfo["isLastPage"],
        LastPageNo=pageInfo["lastPageNo"],
        Table=result,
        PageSize=pageSize,
        StartPaginationNo=pageInfo["startPaginationNo"],
        EndPaginationNo=pageInfo["endPaginationNo"],
        TotalRecordCount=totalRecordsCount,
        Columns=columns
        )
        
        OverviewData = overviewModel.GetPaginationInfo()
        
        return JsonResponse({
            "status": success,
            "OverviewData" : OverviewData
        })

    
    
        
        
        