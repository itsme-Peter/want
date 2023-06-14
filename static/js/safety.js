function sideBar(){
    let side = document.getElementById("sideBar")
    side.style.display = 'block';
    // alert("Its called for!!")
  }
  function sideOptions(){
    let options = document.getElementById("options")
    if (options.style.display == "none"){
      options.style.display == "flex"
    }
    else{
      options.style.display = "none"
    }
  }
  
  $(document).ready(function() {
    $(window).on('resize', function() {
      let parents = document.getElementById("parents")
      if ($(window).width() < 700) {
        parents.classList.remove("grid-cols-4")
        parents.classList.add("grid-cols-2")
      }
       else {
        parents.classList.remove("grid-cols-2")
        parents.classList.add("grid-cols-4")
      }
    });
  });
  
  function allProducts(url){
      var parents = document.getElementById("parents")
  
      parents.innerHTML = "";
  
          $.ajax({
              url: url,
             type: "GET",
             success: function(response) {
              var pages=response["pages"]
              console.log(response)
              if (pages != null){
                  results = response["results"]
                  var next_url = response["next"]
                  var prev_url = response["previous"]
                  const pagesContainer = document.getElementById('pages');
  
                  if(pagesContainer != null) {
                      pagesContainer.innerHTML = "";
                  }
                  
                  for (let i = 0; i < response["results"].length; i++) {
                    results = response["results"][i]
                    let urls = results["image"].split("?")[0]
                    let main = document.createElement("div")
                    main.classList.add("max-w-sm" ,"rounded" ,"overflow-hidden" ,"shadow-lg" ,"hover:bg-gray-200")
                    let img_url= urls.replace('https://iwantmainbucket.s3.amazonaws.com', 'https://d3pvj3ro00vroz.cloudfront.net')
                    const img = document.createElement('img');
                    img.src = img_url;
                    img.classList.add('mx-auto',"w-full","h-40");
                    img.loading = "lazy";
                    main.appendChild(img)
  
                    let div2 = document.createElement("div")
                    div2.classList.add("px-6","py-2")
                    main.appendChild(div2)
  
                    n_ = document.createElement("div")
                    n_.classList.add("flex","justify-between","mx-1")
                    
                    const tag1 = document.createElement('span');
                    tag1.classList.add('inline-block', 'rounded', 'px-1','text-lg', 'font-semibold', 'text-blue-600');
                    tag1.textContent = results["name"];
  
                    // create second tag
                    const tag2 = document.createElement('span');
                    tag2.classList.add('inline-block', 'bg-gray-200', 'rounded', 'px-2', 'py-1', 'text-sm', 'font-light', 'text-gray-700',"h-20","overflow-auto","w-full","mt-1","text-center");
                    tag2.textContent = results["description"];
  
                    const tag3 = document.createElement('span');
                    tag3.classList.add('inline-block', 'bg-gray-100', 'rounded-full', 'px-1', 'text-sm','font-semibold', 'text-gray-700');
                    tag3.textContent = "Ksh " + results["price"];
  
                    let order = document.createElement("div")
                    order.classList.add("bg-green-400","text-lg","text-white","text-center","p-1")
                    order.textContent = results["phone_number"]
  
                    n_.appendChild(tag1)
                    n_.appendChild(tag3)
                    div2.appendChild(n_)
                    div2.appendChild(tag2)
                    main.append(order)
                    parents.appendChild(main)
                    
                }
                  // Create the <ul> element
                  const ul = document.createElement('ul');
                  ul.className = 'flex space-x-3 mb-5 items-center text-blue-600';
  
                  // Create the first <li> element with the left chevron icon
                  const li1 = document.createElement('li');
                  const pe = document.createElement('button');
                  pe.addEventListener("click", p_);
                  const svg1 = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                  svg1.setAttribute('width', '24');
                  svg1.setAttribute('height', '24');
                  svg1.setAttribute('fill', 'currentColor');
                  svg1.setAttribute('class', 'bi bi-chevron-compact-left');
                  svg1.setAttribute('viewBox', '0 0 16 16');
                  const path1 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                  path1.setAttribute('fill-rule', 'evenodd');
                  path1.setAttribute('d', 'M9.224 1.553a.5.5 0 0 1 .223.67L6.56 8l2.888 5.776a.5.5 0 1 1-.894.448l-3-6a.5.5 0 0 1 0-.448l3-6a.5.5 0 0 1 .67-.223z');
                  svg1.appendChild(path1);
                  pe.appendChild(svg1)
                  li1.appendChild(pe);
                  ul.appendChild(li1);
  
                  function handleClick(event) {
                      const pageNum = event.target.textContent;
                      console.log(`/safety/all?page=${pageNum}`);
                      url = `/safety/all?page=${pageNum}`
                      allProducts(url)
                  }
                  function n_(event) {
                      url = next_url
                      if (url == "null") {
                          url = `/safety/all?page=${pages}`
                      }
                      console.log(url = `/safety/all?page=${pages}`)
                      allProducts(url)
                  }
                  function p_(event) {
                      url = prev_url
  
                      if (url == "null") {
                          url = `/safety/all?page=${1}`
                      }
                      console.log(url = `/safety/all?page=${1}`)
                      allProducts(url)
                  }
  
                  // Create the second <li> element with the circle and number
                  for (i=1;i<=pages;i++){
                      const li2 = document.createElement('li');   
                      li2.className = 'h-7 w-7 flex items-center justify-center rounded-full border text-sm';
                      li2.id = 'pages';
                      const a2 = document.createElement('button');
                      a2.textContent = i;
                      li2.appendChild(a2);
                      ul.appendChild(li2);   
                      a2.addEventListener("click", handleClick);
  
                  }
  
                  // Create the third <li> element with the right chevron icon
                  const li3 = document.createElement('li');
                  const ne = document.createElement('button');
                  ne.addEventListener("click", n_);
                  const svg2 = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                  svg2.setAttribute('width', '24');
                  svg2.setAttribute('height', '24');
                  svg2.setAttribute('fill', 'currentColor');
                  svg2.setAttribute('class', 'bi bi-chevron-compact-right');
                  svg2.setAttribute('viewBox', '0 0 16 16');
                  const path2 = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                  path2.setAttribute('fill-rule', 'evenodd');
                  path2.setAttribute('d', 'M6.776 1.553a.5.5 0 0 1 .671.223l3 6a.5.5 0 0 1 0 .448l-3 6a.5.5 0 1 1-.894-.448L9.44 8 6.553 2.224a.5.5 0 0 1 .223-.671z');
                  svg2.appendChild(path2);
                  ne.appendChild(svg2)
                  li3.appendChild(ne);
                  ul.appendChild(li3);
  
                  // Append the <ul> element to the page
                  pagesContainer.appendChild(ul);
  
              }
              else{
                      results = response
                      let paren = document.getElementById("parents")
                      if (results.length > 1){
                        for (let i = 0; i < response.length-1; i++){
                          let urls = results["image"].split("?")[0]
                          let main = document.createElement("div")
                          main.classList.add("max-w-sm" ,"rounded" ,"overflow-hidden" ,"shadow-lg" ,"hover:bg-gray-200")
                          let img_url= urls.replace('https://iwantmainbucket.s3.amazonaws.com', 'https://d3pvj3ro00vroz.cloudfront.net')
                          const img = document.createElement('img');
                          img.src = img_url;
                          img.classList.add('mx-auto',"w-full","h-40");
                          img.loading = "lazy";
                          main.appendChild(img)
  
                          let div2 = document.createElement("div")
                          div2.classList.add("px-1","py-2")
                          main.appendChild(div2)
  
                          n_ = document.createElement("div")
                          n_.classList.add("flex","justify-between","mx-1")
                          
                          const tag1 = document.createElement('span');
                          tag1.classList.add('inline-block', 'rounded', 'px-1','text-lg', 'font-semibold', 'text-blue-600');
                          tag1.textContent = results["name"];
  
                          // create second tag
                          const tag2 = document.createElement('span');
                          tag2.classList.add('inline-block', 'bg-gray-200', 'rounded', 'px-2', 'py-1', 'text-sm', 'font-light', 'text-gray-700',"h-20","overflow-auto","w-full","mt-1","text-center");
                          tag2.textContent = results["description"];
  
                          const tag3 = document.createElement('span');
                          tag3.classList.add('inline-block', 'bg-gray-100', 'rounded-full', 'px-1', 'text-sm','font-semibold', 'text-gray-700');
                          tag3.textContent = "Ksh " + results["price"];
  
  
                          let order = document.createElement("div")
                          order.classList.add("bg-green-400","text-lg","text-white","text-center","p-1")
                          order.textContent = results["phone_number"]
  
                          n_.appendChild(tag1)
                          n_.appendChild(tag3)
                          div2.appendChild(n_)
                          div2.appendChild(tag2)
                          main.append(order)
                          paren.appendChild(main)
                        }
                        
                      }
                      let urls = results["image"].split("?")[0]
                      let main = document.createElement("div")
                      main.classList.add("max-w-sm" ,"rounded" ,"overflow-hidden" ,"shadow-lg" ,"hover:bg-gray-200")
                      let img_url= urls.replace('https://iwantmainbucket.s3.amazonaws.com', 'https://d3pvj3ro00vroz.cloudfront.net')
                      const img = document.createElement('img');
                      img.src = img_url;
                      img.classList.add('mx-auto',"w-full","h-40");
                      img.loading = "lazy";
                      main.appendChild(img)
  
                      let div2 = document.createElement("div")
                      div2.classList.add("px-6","py-2")
                      main.appendChild(div2)
  
                      n_ = document.createElement("div")
                      n_.classList.add("flex","justify-between","mx-1")
                      
                      const tag1 = document.createElement('span');
                      tag1.classList.add('inline-block', 'rounded', 'px-3','text-lg', 'font-bold', 'text-black', 'mr-2');
                      tag1.textContent = results["name"];
  
                      // create second tag
                      const tag2 = document.createElement('span');
                      tag2.classList.add('inline-block', 'bg-gray-200', 'rounded', 'px-2', 'py-1', 'text-sm', 'font-light', 'text-gray-700',"h-20","overflow-auto","w-full","mt-1","text-center");
                      tag2.textContent = results["description"];
  
                      const tag3 = document.createElement('span');
                      tag3.classList.add('inline-block', 'bg-gray-100', 'rounded-full', 'px-3', 'text-sm', 'font-semibold', 'text-gray-700');
                      tag3.textContent = results["price"];
  
                      let order = document.createElement("div")
                      order.classList.add("bg-green-400","text-lg","text-white","text-center","p-1")
                      order.textContent = "call to order:0712345678"
  
                      n_.appendChild(tag1)
                      n_.appendChild(tag3)
                      div2.appendChild(n_)
                      div2.appendChild(tag2)
                      main.append(order)
                      parents.appendChild(main)
                  }
              },
              error: function(xhr, status, error){
                error.log("Not found")
                alert("No products found")
              }
  
              
  
             }
      
          )
      
  }
  
  function rands(){
      $.ajax({
          url: "/safety/randoms",
          type: "GET",
          success: function(response) {
          results = response["results"]
  
          const parents = document.getElementById("parents")
          // const parents_phone = document.getElementById("parents_phone")
          for (let i = 0; i < response["results"].length; i++) {
              results = response["results"][i]
              let urls = results["image"].split("?")[0]
              let main = document.createElement("div")
              main.classList.add("max-w-sm" ,"rounded" ,"overflow-hidden" ,"shadow-lg" ,"hover:bg-gray-200")
              let img_url= urls.replace('https://iwantmainbucket.s3.amazonaws.com', 'https://d3pvj3ro00vroz.cloudfront.net')
              const img = document.createElement('img');
              img.src = img_url;
              img.classList.add('mx-auto',"w-full","h-40");
              img.loading = "lazy";
              main.appendChild(img)
  
              let div2 = document.createElement("div")
              div2.classList.add("px-6","py-2")
              main.appendChild(div2)
  
              n_ = document.createElement("div")
              n_.classList.add("flex","justify-between","items-center")
              
              const tag1 = document.createElement('span');
              tag1.classList.add('inline-block', 'rounded', 'px-1','text-lg', 'font-semibold', 'text-blue-600');
              tag1.textContent = results["name"];
  
              // create second tag
              const tag2 = document.createElement('span');
              tag2.classList.add('inline-block', 'bg-gray-200', 'rounded', 'px-2', 'py-1', 'text-sm', 'font-light', 'text-gray-700',"h-20","overflow-auto","w-full","mt-1","text-center");
              tag2.textContent = results["description"];
  
              const tag3 = document.createElement('span');
              tag3.classList.add('inline-block', 'bg-gray-100', 'rounded-full', 'px-1', 'text-sm','font-semibold', 'text-gray-700');
              tag3.textContent = "Ksh " + results["price"];
  
              let order = document.createElement("div")
              order.classList.add("bg-green-400","text-lg","text-white","text-center","p-1")
              order.textContent =results["phone_number"]
  
              n_.appendChild(tag1)
              n_.appendChild(tag3)
              div2.appendChild(n_)
              div2.appendChild(tag2)
              main.append(order)
              parents.appendChild(main)
              // parents_phone.appendChild(main)
              
          }
          }
  
      })
  }
  var k = 0;
  
  function searches() {
    var search_ = document.getElementById("searchbox");
    if (k == 0) {
      search_.style.width = "12rem";
      search_.style.borderBottom = "1px solid blue"
      document.getElementById("searchButton").style.display = 'none';
      document.getElementById("hits").style.display = 'block';
      k = 1;
    } else {
      search_.style.width = "0";
      search_.style.borderBottom = "none";
      document.getElementById("hits").style.display = 'none';
      k = 0;
    }
  }
  // function toggleHitsVisibility() {
  //   const searchBox = document.querySelector('.my-search-input');
  //   const hitsDiv = document.querySelector('#hits');
  
  //   if (searchBox.value !== '') {
  //     hitsDiv.style.display = 'block';
  //   } else {
  //     hitsDiv.style.display = 'none';
  //   }
  // }
  // const searchBox = document.querySelector('.my-search-input');
  // searchBox.addEventListener('input', toggleHitsVisibility);
  
  
  document.addEventListener('click', (event) => {
      if (event.target !== document.getElementsByClassName("my-search-input")) {
          // search_.style.display = 'none';
          document.getElementById("searchButton").style.display = 'block';
          // document.getElementById("hits").style.display = 'none';
      }
    });
  
  const feedback_form =  document.getElementById("feedback-form")
   feedback_form.addEventListener('submit', (event) => {
      event.preventDefault()
  
      const formData = new FormData(feedback_form);
      const url = "/safety/feedback"
      data = {
          message:formData.get('message'),
          email:formData.get('email'),
          number:formData.get('number')
      }
      console.log(data)
      data_ = JSON.stringify(data)
      
      // Send form data
      fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken'),
          },
          body: data_
        })
        .then(response => response.json())
        .then(data => {
          alert(JSON.stringify(data));
          feedback_form.reset()
        })
        .catch(error => {
          console.error(error); // handle any errors
        });
    })
  
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
  

    
      