#!/usr/bin/env python3
"""Module that demonstrates mixins with a Dragon class."""


class SwimMixin:
    """siwm"""
    def swim(self):
        """swim function"""
        print("The creature swims!")


class FlyMixin:
    """Fly"""
    def fly(self):
        """Fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Drafon mixin class"""
    def roar(self):
        """Self"""
        print("The dragon roars!")
