import pytest
import dog as d
import cat as c


class TestAnimals:
    def test_dog(self):
        expected = "Meow! Meow!"
        actual = d.makesound()
        assert actual == expected

    def test_cat(self):
        expected = "Meow! Meow!"
        actual = c.makesound()
        assert actual == expected
