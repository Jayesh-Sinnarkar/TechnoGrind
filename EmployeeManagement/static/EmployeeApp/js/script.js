function fetchData(pageNumber, isPageSizeChange = false) {
    let csrf = $("input[name=csrfmiddlewaretoken]").val();
    let pageSize = $("#pageSize").val();
  
    if (isPageSizeChange) {
      pageNumber = 1; // Reset to first page when changing page size
    }
  
    $.ajax({
      url: "",
      method: "POST",
      data: {
        csrfmiddlewaretoken: csrf,
        pageNo: pageNumber,
        pageSize: pageSize,
      },
      beforeSend: function () {
        StartLoader();
      },
      success: function (data) {
        EndLoader();
  
        if (data.status) {
          let overViewTable = data.OverviewData.Table;
  
          let htmlString = "";
          for (let i = 0; i < overViewTable.length; i++) {
            let currentRow = `
              <tr>
              <td>${overViewTable[i].ID}</td>
              <td>${overViewTable[i].first_name}</td>
              <td>${overViewTable[i].last_name}</td>
              <td>${overViewTable[i].email}</td>
              <td>${overViewTable[i].position}</td>
              <td>${overViewTable[i].salary}</td>
              <td>${overViewTable[i].date_hired}</td>
            `;
            htmlString += currentRow;
          }
  
          let paginationHtmlString = `<button class="btn btn-dark 
            ${data.OverviewData.CurrenPageNo == 1 ? "disabled" : ""}
            btn-sm pgnbtn col-md-1 col-lg-1" data-value="1">First</button>`;
  
          for (
            let i = data.OverviewData.StartPaginationNo;
            i < data.OverviewData.EndPaginationNo;
            i++
          ) {
            let disabled = data.OverviewData.CurrenPageNo == i ? "disabled" : "";
            paginationHtmlString += `<button class="btn btn-dark btn-sm pgnbtn ${disabled} col-md-1 col-lg-1" data-value="${i}">${i}</button>`;
          }
  
          if (!isPageSizeChange && data.OverviewData.IsLastPageNo) {
            paginationHtmlString += `<button class="btn btn-dark 
              ${data.OverviewData.CurrenPageNo == data.OverviewData.LastPageNo ? "disabled" : ""}
              btn-sm pgnbtn col-md-1 col-lg-1" data-value="${data.OverviewData.LastPageNo}">Last</button>`;
          }
  
          $("#paginationDiv").html(paginationHtmlString);
          $("#tableBody").html(htmlString);
        }
      },
      error: function (jqXHR, textStatus, errorThrown) {
        EndLoader();
        console.error("Error:", textStatus, errorThrown);
      },
    });
  }
  
  $(document).ready(function () {
    fetchData(1); // Initial fetch on page load
  
    $(document).on("click", ".pgnbtn", function () {
      event.preventDefault();
      var pageNumber = this.attributes["data-value"].value;
      fetchData(pageNumber);
    });
  
    $("#pageSize").change(function () {
      fetchData(1, true); // Page size change, reset to page 1
    });
  });
  