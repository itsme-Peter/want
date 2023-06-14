function feedback(){
    console.log(document.getElementById("feedback").style.width)
    
    if (document.getElementById("feedback").style.width == "0px"){
        document.getElementById("feedback").style.width = "50%"
    } 
    else{
      document.getElementById("feedback").style.width = 0
    }
      
  }
 
 
  const sendTimeDivs = document.querySelectorAll("#send-time");
 
  // Add a click event listener to each of the "send-time" divs
  sendTimeDivs.forEach(function(sendTimeDiv) {
  sendTimeDiv.addEventListener("click", function() {
      const hiddenParagraphs = sendTimeDiv.querySelectorAll(".hidden");
      hiddenParagraphs.forEach(function(hiddenParagraph) {
      hiddenParagraph.classList.remove("hidden");
      });
  });
  });
 
 const message = document.getElementById("messages")
 const orders = document.getElementById("orders")
 const myDetails = document.getElementById("myDetails")
 function dash(i){
 
    switch (i) {
        case 1:
            myDetails.style.display = "block"
            myDetails.style.width= "100%"
            orders.style.display = "none"
            message.style.display = "none"
            break;
        
        case 2:
 
            myDetails.style.display = "none"
            orders.style.display="block"
            orders.style.width = "100%"
            message.style.display = "none"
            break;
        case 3:
            console.log(10)
 
            myDetails.style.display = "none"
            orders.style.display = "none"
            message.style.width = "100%"
            message.style.display = "flex"
            break;
    }
 }
 