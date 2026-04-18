import pytest

from database import Database
from bun import Bun
from ingredient import Ingredient


class TestDatabase:

    @pytest.fixture
    def database(self):
        return Database()

    def test_available_buns_returns_list_of_bun_instances(self, database):
        assert all(isinstance(b, Bun) for b in database.available_buns())

    def test_available_buns_returns_three_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_returns_list_of_ingredient_instances(self, database):
        assert all(isinstance(i, Ingredient) for i in database.available_ingredients())

    def test_available_ingredients_returns_six_ingredients(self, database):
        assert len(database.available_ingredients()) == 6
