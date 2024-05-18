
function ChangePage(event, nextPage){
    event.preventDefault();

    let csrf = $("input[name=csrfmiddlewaretoken]").val()

    $.ajax({
        url: '',
        method: 'POST',
        data: {
            csrfmiddlewaretoken : csrf,
            pageNo: nextPage
        },
        success: function(data) {
            console.log('Success:', data);
            
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
      debugger;
      var pageNumber = this.attributes['data-value'].value;
      ChangePage(event,pageNumber);
    });
});