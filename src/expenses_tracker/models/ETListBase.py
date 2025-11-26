class ETListBase:
    def __init__(self):
        self._collection = []

    @property
    def collection(self):
        return self._collection
    
    def add_to_list(self, new_item):
        self._collection.append(new_item)

    def select_from_list(self, search_term, search_by="id"):
        target_item = []
        if search_by == 'id':
            target_item = [item for item in self._collection if search_term == item.id]
        
        if search_by == 'name':
            target_item = [item for item in self._collection if search_term == item.name]
        
        return target_item[0] if len(target_item) > 0 else None
    
    def print_list(self):
        if len(self._collection) == 0:
            print("No items in collection")
        else:
            for item in self._collection:
                item.show_detailed_info()

    def remove_from_list(self, item_to_remove):
        self._collection.remove(item_to_remove)
        