let search2 = instantsearch({
    indexName: 'products_safety',
    searchClient: algoliasearch('RN3F3U9YUA', '325153a7678bc858da89d2406dc0ad59'),
  });
  
  search2.addWidgets([
    instantsearch.widgets.searchBox({
      container: '#SearchBox2',
      placeholder: 'Search...',
      cssClasses: {
        input: 'search2'
      },
    }),
    instantsearch.widgets.hits({
      container: '#hits2',
      templates: {
        item: `
          <div class="mt-1">
            
            <div class="hit-name m-2 hover:text-blue-400">
              <a href="/safety/product/{{name}}" >{{#helpers.highlight}}{ "attribute": "name" }{{/helpers.highlight}}</a>
            </div>
        
          </div>
        `,
      },
    }),
    
  
  ]);
  
  search2.start();

const searchInput = document.querySelector('.search2');
const hitsElement = document.getElementById('hits2');
let hitsbtn = document.getElementById("hitsbtn")
searchInput.addEventListener("input", function() {
  // Do something when the user starts typing.
  hitsElement.style.display = "block";
  hitsbtn.style.display = "block";
});

function hideHits(){
  hitsbtn.style.display = "none";
  hitsElement.style.display = "none"
}