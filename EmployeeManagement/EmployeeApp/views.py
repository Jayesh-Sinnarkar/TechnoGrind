from django.shortcuts import render
import pdb
from .models import Employee
from Helper import DatabaseHelper as dbHelper
from django.http import JsonResponse


def GetPageInfo(totalPageCount, pageSize, currentpageNo):
    totalPages = totalPageCount//pageSize
    firstPageNo = 1
    startPageNo = 1
    endPageNo = totalPages
    lastPageNo = totalPages 
    
    if (currentpageNo-2) > 0:
        startPageNo = currentpageNo-2
    
    if currentpageNo + 2 < totalPages:
        endPageNo = currentpageNo + 2        

    pageRange = range(startPageNo, endPageNo + 1)

    pageInfo = {
        "firstPageNo" : firstPageNo,
        "pageRange": pageRange,
        "lastPageNo": lastPageNo,
        "currentpageNo" : currentpageNo
    }
    
    return pageInfo

def GetPageInfoJS(totalPageCount, pageSize, currentpageNo):
    totalPages = totalPageCount//pageSize
    firstPageNo = 1
    startPageNo = 1
    endPageNo = totalPages
    lastPageNo = totalPages 
    
    if (currentpageNo-2) > 0:
        startPageNo = currentpageNo-2
    
    if currentpageNo + 2 < totalPages:
        endPageNo = currentpageNo + 2        

    pageInfo = {
        "firstPageNo" : firstPageNo,
        "startPageNo": startPageNo,
        "endPageNo": endPageNo + 1,
        "lastPageNo": lastPageNo,
        "currentpageNo" : currentpageNo
    }
    
    return pageInfo


    

def Overview(request):    


    if request.method == "GET":
        pageSize = 10
        pageNo = 1
        
        query = f"CALL GetEmployeesByPage({pageNo}, {pageSize});"
        
        success, result = dbHelper.SelectQueryListDict(query)
        
        totalPages = Employee.objects.count()
        
        pageInfo = GetPageInfo(totalPages, pageSize, pageNo)

        if success:
            context = {'data': result}
            return render(request, template_name="EmployeeApp/index.html", context={
                'data':result,
                'pageInfo': pageInfo
            })    
        else:
            return render(request, template_name="EmployeeApp/index.html", context={
            'data':[{}]
            })
    else:
        pageNo = int(request.POST["pageNo"])
        pageSize = int(request.POST["pageSize"])

        query = f"CALL GetEmployeesByPage({pageNo}, {pageSize});"
        
        success, result = dbHelper.SelectQueryListDict(query)
        
        totalPages = Employee.objects.count()
        
        pageInfo = GetPageInfo(totalPages, pageSize, pageNo)
        
        totalPages = totalPages//pageSize
        firstPageNo = 1
        startPageNo = 1
        endPageNo = totalPages
        lastPageNo = totalPages 
        
        if (pageNo-2) > 0:
            startPageNo = pageNo-2
        
        if pageNo + 2 < totalPages:
            endPageNo = pageNo + 2        
        
        return JsonResponse({
            "status": success,
            "data" : result,
            "firstPageNo" : firstPageNo,
            "startPageNo": startPageNo,
            "endPageNo": endPageNo + 1,
            "lastPageNo": lastPageNo,
            "currentpageNo" : pageNo
        })

    
    
        
        
        