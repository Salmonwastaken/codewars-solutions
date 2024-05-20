# https://www.codewars.com/kata/515bb423de843ea99400000a
import math


class PaginationHelper:
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection: list, items_per_page: int):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self) -> int:
        return len(self.collection)

    # returns the number of pages
    def page_count(self) -> int:
        return (math.ceil(self.item_count() / self.items_per_page))

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index: int) -> int:
        index_count = self.page_count() - 1

        if page_index < 0 or page_index > index_count:
            return -1

        start_range = self.items_per_page * page_index
        end_range = start_range + self.items_per_page

        return len(self.collection[start_range:end_range])

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index: int) -> int:
        item_count = self.item_count() - 1

        if item_index < 0 or item_index > item_count:
            return -1

        for page_index in range(self.page_count()):
            start_range = self.items_per_page * page_index
            end_range = start_range + self.items_per_page

            if item_index >= start_range and item_index < end_range:
                return page_index
