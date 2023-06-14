const search = instantsearch({
  indexName: 'products_safety',
  searchClient: algoliasearch('RN3F3U9YUA', '325153a7678bc858da89d2406dc0ad59'),
});

search.addWidgets([
  instantsearch.widgets.searchBox({
    container: '#searchbox',
    placeholder: 'Search...',
    cssClasses: {
      input: 'my-search-input'
    },
  }),


  instantsearch.widgets.hits({
    container: '#hits',
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

search.start();
