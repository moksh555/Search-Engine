class invertedIndex:
    def __init__(self):
        self.index = {}
    
    def add_document(self, document_id, document):
        terms = document.split()
        for position, term in enumerate(terms):
            if term not in self.index:
                self.index[term] = {}
            if document_id not in self.index[term]:
                self.index[term][document_id] = []
            
            self.index[term][document_id].append(position)
    
    def search(self, query):
        terms = query.split()
        results = None
        for term in terms:
            if term in self.index:
                if results is None:
                    results = set(self.index[term].keys())
                else:
                    results.intersection_update(self.index[term].keys())
        if results is None:
            return []
        else:
            search_results = []
            for document_id in results:
                position = [self.index[term][document_id] for term in terms]
                search_results.append((document_id, position))
            return search_results


index = invertedIndex()
index.add_document(1, 'apple banana apple')
index.add_document(2, 'banana cherry')
index.add_document(3, 'apple cherry')

query = "apple"
search_results = index.search(query)
print(search_results)
print(index.index)