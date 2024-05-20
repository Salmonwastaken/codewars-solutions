from PaginationHelper import PaginationHelper


def tests():
    collection = ['a', 'b', 'c', 'd', 'e', 'f']
    helper = PaginationHelper(collection, 4)

    def test_page_count():
        assert helper.page_count() == 2

    def test_item_count():
        assert helper.item_count() == 6

    def test_page_item_count():
        assert helper.page_item_count(0) == 4
        assert helper.page_item_count(1) == 2
        assert helper.page_item_count(2) == -1

    def test_page_index():
        assert helper.page_index(5) == 1
        assert helper.page_index(2) == 0
        assert helper.page_index(20) == -1
        assert helper.page_index(-10) == -1

    def test_empty():
        empty = PaginationHelper([], 10)

        assert empty.item_count() == 0

        assert empty.page_count() == 0

        assert empty.page_index(0) == -1
        assert empty.page_index(1) == -1
        assert empty.page_index(-1) == -1

        assert empty.page_item_count(0) == -1
        assert empty.page_item_count(1) == -1
        assert empty.page_item_count(-1) == -1

    test_page_count()
    test_item_count()
    test_page_item_count()
    test_page_index()
    test_empty()
