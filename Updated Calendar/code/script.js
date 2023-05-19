function func () {
  /* To remove classes of all elements */
  const allElements = document.querySelectorAll('*');
  allElements.forEach((element) => {
    element.classList.remove('Past');
    element.classList.remove('Available');
    element.classList.remove('Reserved');
    element.classList.remove('Unavailable');
    element.classList.remove('Restricted');
  })

  var roomOne = document.getElementsByClassName("desc-1");
  var roomTwo = document.getElementsByClassName("desc-2");
  var roomThree = document.getElementsByClassName("desc-3");

  if (document.getElementById("room-1").checked)
  {
    $("#08-row td:nth-child(2)").addClass("Past");
    $("#08-row td:nth-child(3)").addClass("Available");
    $("#08-row td:nth-child(4)").addClass("Reserved");
    $("#08-row td:nth-child(5)").addClass("Reserved");
    $("#08-row td:nth-child(6)").addClass("Reserved");
    $("#08-row td:nth-child(7)").addClass("Unavailable");
    $("#08-row td:nth-child(8)").addClass("Unavailable");

    $("#10-row td:nth-child(2)").addClass("Past");
    $("#10-row td:nth-child(3)").addClass("Reserved");
    $("#10-row td:nth-child(4)").addClass("Reserved");
    $("#10-row td:nth-child(5)").addClass("Reserved");
    $("#10-row td:nth-child(6)").addClass("Reserved");
    $("#10-row td:nth-child(7)").addClass("Unavailable");
    $("#10-row td:nth-child(8)").addClass("Unavailable");

    $("#12-row td:nth-child(2)").addClass("Past");
    $("#12-row td:nth-child(3)").addClass("Available");
    $("#12-row td:nth-child(4)").addClass("Reserved");
    $("#12-row td:nth-child(5)").addClass("Reserved");
    $("#12-row td:nth-child(6)").addClass("Available");
    $("#12-row td:nth-child(7)").addClass("Unavailable");
    $("#12-row td:nth-child(8)").addClass("Unavailable");
    
    $("#14-row td:nth-child(2)").addClass("Past");
    $("#14-row td:nth-child(3)").addClass("Reserved");
    $("#14-row td:nth-child(4)").addClass("Reserved");
    $("#14-row td:nth-child(5)").addClass("Reserved");
    $("#14-row td:nth-child(6)").addClass("Reserved");
    $("#14-row td:nth-child(7)").addClass("Unavailable");
    $("#14-row td:nth-child(8)").addClass("Unavailable");
    
    $("#16-row td:nth-child(2)").addClass("Past");
    $("#16-row td:nth-child(3)").addClass("Reserved");
    $("#16-row td:nth-child(4)").addClass("Available");
    $("#16-row td:nth-child(5)").addClass("Reserved");
    $("#16-row td:nth-child(6)").addClass("Reserved");
    $("#16-row td:nth-child(7)").addClass("Unavailable");
    $("#16-row td:nth-child(8)").addClass("Unavailable");

    $("#18-row td:nth-child(2)").addClass("Past");
    $("#18-row td:nth-child(3)").addClass("Available");
    $("#18-row td:nth-child(4)").addClass("Reserved");
    $("#18-row td:nth-child(5)").addClass("Available");
    $("#18-row td:nth-child(6)").addClass("Reserved");
    $("#18-row td:nth-child(7)").addClass("Unavailable");
    $("#18-row td:nth-child(8)").addClass("Unavailable");

    $("#20-row td:nth-child(2)").addClass("Past");
    $("#20-row td:nth-child(3)").addClass("Available");
    $("#20-row td:nth-child(4)").addClass("Reserved");
    $("#20-row td:nth-child(5)").addClass("Reserved");
    $("#20-row td:nth-child(6)").addClass("Available");
    $("#20-row td:nth-child(7)").addClass("Unavailable");
    $("#20-row td:nth-child(8)").addClass("Unavailable");

    $("#22-row td:nth-child(2)").addClass("Past");
    $("#22-row td:nth-child(3)").addClass("Available");
    $("#22-row td:nth-child(4)").addClass("Available");
    $("#22-row td:nth-child(5)").addClass("Available");
    $("#22-row td:nth-child(6)").addClass("Reserved");
    $("#22-row td:nth-child(7)").addClass("Unavailable");
    $("#22-row td:nth-child(8)").addClass("Unavailable");

    $(".desc-2").hide()
    $(".desc-3").hide()
    $(".desc-1").show()
  }

  if (document.getElementById("room-2").checked)
  {
    $("#08-row td:nth-child(2)").addClass("Past");
    $("#08-row td:nth-child(3)").addClass("Reserved");
    $("#08-row td:nth-child(4)").addClass("Available");
    $("#08-row td:nth-child(5)").addClass("Reserved");
    $("#08-row td:nth-child(6)").addClass("Available");
    $("#08-row td:nth-child(7)").addClass("Unavailable");
    $("#08-row td:nth-child(8)").addClass("Unavailable");

    $("#10-row td:nth-child(2)").addClass("Past");
    $("#10-row td:nth-child(3)").addClass("Available");
    $("#10-row td:nth-child(4)").addClass("Reserved");
    $("#10-row td:nth-child(5)").addClass("Available");
    $("#10-row td:nth-child(6)").addClass("Reserved");
    $("#10-row td:nth-child(7)").addClass("Unavailable");
    $("#10-row td:nth-child(8)").addClass("Unavailable");

    $("#12-row td:nth-child(2)").addClass("Past");
    $("#12-row td:nth-child(3)").addClass("Reserved");
    $("#12-row td:nth-child(4)").addClass("Reserved");
    $("#12-row td:nth-child(5)").addClass("Available");
    $("#12-row td:nth-child(6)").addClass("Available");
    $("#12-row td:nth-child(7)").addClass("Unavailable");
    $("#12-row td:nth-child(8)").addClass("Unavailable");
    
    $("#14-row td:nth-child(2)").addClass("Past");
    $("#14-row td:nth-child(3)").addClass("Available");
    $("#14-row td:nth-child(4)").addClass("Reserved");
    $("#14-row td:nth-child(5)").addClass("Available");
    $("#14-row td:nth-child(6)").addClass("Reserved");
    $("#14-row td:nth-child(7)").addClass("Unavailable");
    $("#14-row td:nth-child(8)").addClass("Unavailable");
    
    $("#16-row td:nth-child(2)").addClass("Past");
    $("#16-row td:nth-child(3)").addClass("Reserved");
    $("#16-row td:nth-child(4)").addClass("Reserved");
    $("#16-row td:nth-child(5)").addClass("Reserved");
    $("#16-row td:nth-child(6)").addClass("Available");
    $("#16-row td:nth-child(7)").addClass("Unavailable");
    $("#16-row td:nth-child(8)").addClass("Unavailable");

    $("#18-row td:nth-child(2)").addClass("Past");
    $("#18-row td:nth-child(3)").addClass("Available");
    $("#18-row td:nth-child(4)").addClass("Available");
    $("#18-row td:nth-child(5)").addClass("Reserved");
    $("#18-row td:nth-child(6)").addClass("Reserved");
    $("#18-row td:nth-child(7)").addClass("Unavailable");
    $("#18-row td:nth-child(8)").addClass("Unavailable");

    $("#20-row td:nth-child(2)").addClass("Past");
    $("#20-row td:nth-child(3)").addClass("Available");
    $("#20-row td:nth-child(4)").addClass("Reserved");
    $("#20-row td:nth-child(5)").addClass("Available");
    $("#20-row td:nth-child(6)").addClass("Reserved");
    $("#20-row td:nth-child(7)").addClass("Unavailable");
    $("#20-row td:nth-child(8)").addClass("Unavailable");

    $("#22-row td:nth-child(2)").addClass("Past");
    $("#22-row td:nth-child(3)").addClass("Reserved");
    $("#22-row td:nth-child(4)").addClass("Reserved");
    $("#22-row td:nth-child(5)").addClass("Reserved");
    $("#22-row td:nth-child(6)").addClass("Reserved");
    $("#22-row td:nth-child(7)").addClass("Unavailable");
    $("#22-row td:nth-child(8)").addClass("Unavailable");

    $(".desc-1").hide()
    $(".desc-3").hide()
    $(".desc-2").show()
  }

  if (document.getElementById("room-3").checked)
  {
    $("#08-row td:nth-child(2)").addClass("Past");
    $("#08-row td:nth-child(3)").addClass("Reserved");
    $("#08-row td:nth-child(4)").addClass("Available");
    $("#08-row td:nth-child(5)").addClass("Reserved");
    $("#08-row td:nth-child(6)").addClass("Available");
    $("#08-row td:nth-child(7)").addClass("Unavailable");
    $("#08-row td:nth-child(8)").addClass("Unavailable");

    $("#10-row td:nth-child(2)").addClass("Past");
    $("#10-row td:nth-child(3)").addClass("Available");
    $("#10-row td:nth-child(4)").addClass("Reserved");
    $("#10-row td:nth-child(5)").addClass("Available");
    $("#10-row td:nth-child(6)").addClass("Reserved");
    $("#10-row td:nth-child(7)").addClass("Unavailable");
    $("#10-row td:nth-child(8)").addClass("Unavailable");

    $("#12-row td:nth-child(2)").addClass("Past");
    $("#12-row td:nth-child(3)").addClass("Available");
    $("#12-row td:nth-child(4)").addClass("Reserved");
    $("#12-row td:nth-child(5)").addClass("Reserved");
    $("#12-row td:nth-child(6)").addClass("Available");
    $("#12-row td:nth-child(7)").addClass("Unavailable");
    $("#12-row td:nth-child(8)").addClass("Unavailable");
    
    $("#14-row td:nth-child(2)").addClass("Past");
    $("#14-row td:nth-child(3)").addClass("Available");
    $("#14-row td:nth-child(4)").addClass("Reserved");
    $("#14-row td:nth-child(5)").addClass("Available");
    $("#14-row td:nth-child(6)").addClass("Reserved");
    $("#14-row td:nth-child(7)").addClass("Unavailable");
    $("#14-row td:nth-child(8)").addClass("Unavailable");
    
    $("#16-row td:nth-child(2)").addClass("Past");
    $("#16-row td:nth-child(3)").addClass("Reserved");
    $("#16-row td:nth-child(4)").addClass("Reserved");
    $("#16-row td:nth-child(5)").addClass("Reserved");
    $("#16-row td:nth-child(6)").addClass("Available");
    $("#16-row td:nth-child(7)").addClass("Unavailable");
    $("#16-row td:nth-child(8)").addClass("Unavailable");

    $("#18-row td:nth-child(2)").addClass("Past");
    $("#18-row td:nth-child(3)").addClass("Available");
    $("#18-row td:nth-child(4)").addClass("Available");
    $("#18-row td:nth-child(5)").addClass("Reserved");
    $("#18-row td:nth-child(6)").addClass("Reserved");
    $("#18-row td:nth-child(7)").addClass("Unavailable");
    $("#18-row td:nth-child(8)").addClass("Unavailable");

    $("#20-row td:nth-child(2)").addClass("Past");
    $("#20-row td:nth-child(3)").addClass("Available");
    $("#20-row td:nth-child(4)").addClass("Reserved");
    $("#20-row td:nth-child(5)").addClass("Reserved");
    $("#20-row td:nth-child(6)").addClass("Available");
    $("#20-row td:nth-child(7)").addClass("Unavailable");
    $("#20-row td:nth-child(8)").addClass("Unavailable");

    $("#22-row td:nth-child(2)").addClass("Past");
    $("#22-row td:nth-child(3)").addClass("Reserved");
    $("#22-row td:nth-child(4)").addClass("Reserved");
    $("#22-row td:nth-child(5)").addClass("Reserved");
    $("#22-row td:nth-child(6)").addClass("Reserved");
    $("#22-row td:nth-child(7)").addClass("Unavailable");
    $("#22-row td:nth-child(8)").addClass("Unavailable");

    $(".desc-2").hide()
    $(".desc-1").hide()
    $(".desc-3").show()
  }
}