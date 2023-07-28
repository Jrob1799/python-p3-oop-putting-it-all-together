#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        if brand == str:
            self._brand = brand
    
    brand = property(get_brand, set_brand)
    
    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if size == int:
            self._size = size
        else:
            print("size must be an integer")
            
    size = property(get_size, set_size)
    
    def cobble(shoe):
        print("Your shoe is as good as new!")
        shoe.condition = "New"
        