#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self._title = title
        self._page_count = page_count
        
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if title == str:
            self._title = title
    
    title = property(get_title, set_title)
    
    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if page_count == int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")    
        
    page_count = property(get_page_count, set_page_count)
        
    def turn_page(page):
        print("Flipping the page...wow, you read fast!")
        return page