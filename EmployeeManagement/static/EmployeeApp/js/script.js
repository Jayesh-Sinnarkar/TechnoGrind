
function ChangePage(event, nextPage){
    event.preventDefault();

    let csrf = $("input[name=csrfmiddlewaretoken]").val()
    let pageSize = $('#pageSize').val()
    $.ajax({
        url: '',
        method: 'POST',
        data: {
            csrfmiddlewaretoken : csrf,
            pageNo: nextPage,
            pageSize: pageSize
        },
        beforeSend: function (){
            StartLoader()
        },
        success: function(data) {
            
            EndLoader();

            if(data.status)
            {
                htmlString = ""
                for(let i=0; i<data.data.length; i++)
                    {
                        let currentRow = `
                        <tr>
                        <td>${data.data[i].ID}</td>
                        <td>${data.data[i].first_name}</td>
                        <td>${data.data[i].last_name}</td>
                        <td>${data.data[i].email}</td>
                        <td>${data.data[i].position}</td>
                        <td>${data.data[i].salary}</td>
                        <td>${data.data[i].date_hired}</td>
                        `
                        htmlString += currentRow
                    }
                
                let paginationHtmlString = `<button class="btn btn-dark btn-sm pgnbtn col-md-1 col-lg-1" data-value="1">First</button>`
                
                for(let i=data.startPageNo; i<data.endPageNo; i++)
                {
                    let disabled = "";
                    if(data.currentpageNo == i)
                        {
                            disabled = "disabled";
                        }
                    paginationHtmlString += `<button class="btn btn-dark btn-sm pgnbtn ${disabled} col-md-1 col-lg-1" data-value="${i}">${i}</button>`
                }                
                
                paginationHtmlString += `<button class="btn btn-dark btn-sm pgnbtn col-md-1 col-lg-1" data-value="${data.lastPageNo}">Last</button>`
                
                $('#paginationDiv').html(paginationHtmlString)
                $('#tableBody').html(htmlString)
                
            }

            
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error:', textStatus, errorThrown);
        }
    });

}


function OnPageSizeChange(){

    let csrf = $("input[name=csrfmiddlewaretoken]").val()
    let pageSize = $('#pageSize').val()
    $.ajax({
        url: '',
        method: 'POST',
        data: {
            csrfmiddlewaretoken : csrf,
            pageNo: 1,
            pageSize: pageSize
        },
        beforeSend: function (){
            StartLoader()
        },
        success: function(data) {
            
            EndLoader()

            if(data.status)
            {
                htmlString = ""
                for(let i=0; i<data.data.length; i++)
                    {
                        let currentRow = `
                        <tr>
                        <td>${data.data[i].ID}</td>
                        <td>${data.data[i].first_name}</td>
                        <td>${data.data[i].last_name}</td>
                        <td>${data.data[i].email}</td>
                        <td>${data.data[i].position}</td>
                        <td>${data.data[i].salary}</td>
                        <td>${data.data[i].date_hired}</td>
                        `
                        htmlString += currentRow
                    }
                
                let paginationHtmlString = `<button class="btn btn-dark btn-sm pgnbtn col-md-1 col-lg-1" data-value="1">First</button>`
                
                for(let i=data.startPageNo; i<data.endPageNo; i++)
                {
                    if(data.currentpageNo == i)
                        {
                            paginationHtmlString += `<button class="btn btn-dark btn-sm disabled pgnbtn col-md-1 col-lg-1" data-value="${i}">${i}</button>`
                        }
                    else{
                        paginationHtmlString += `<button class="btn btn-dark btn-sm pgnbtn col-md-1 col-lg-1" data-value="${i}">${i}</button>`
                    }
                }                
                
                paginationHtmlString += `<button class="btn btn-dark btn-sm pgnbtn col-md-1 col-lg-1" data-value="${data.lastPageNo}">Last</button>`
                
                console.log(paginationHtmlString);

                $('#paginationDiv').html(paginationHtmlString)
                $('#tableBody').html(htmlString)
                
            }

            
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error:', textStatus, errorThrown);
        }
    });

}




$(document).ready(function() {
    $(document).on("click",".pgnbtn",function()
    {
      event.preventDefault();
      var pageNumber = this.attributes['data-value'].value;
      ChangePage(event,pageNumber);
    });
});