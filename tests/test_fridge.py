
from unittest import TestCase

from sources.fridge import (Fridge, ALL_INGREDIENTS, UnknownIngredientException,
                            NotEnoughException)


class TestFridge(TestCase):

    def test_valid_exchanges(self):
        fridge = Fridge()
        ingredient = ALL_INGREDIENTS[0]
        self.assertTrue(fridge.is_empty)
        fridge.add_ingredient(ingredient, 10)
        self.assertFalse(fridge.is_empty)
        fridge.use_ingredient(ingredient, 5)
        self.assertFalse(fridge.is_empty)
        fridge.use_ingredient(ingredient, 5)
        self.assertTrue(fridge.is_empty)

    def test_valid_multiple_exchanges(self):
        fridge = Fridge()
        exchanges = {ALL_INGREDIENTS[0]: 2, ALL_INGREDIENTS[1]: 5}
        self.assertTrue(fridge.is_empty)
        fridge.add_multiple_ingredients(exchanges)
        self.assertFalse(fridge.is_empty)
        fridge.use_multiple_ingredients(exchanges)
        self.assertTrue(fridge.is_empty)

    def test_add_invalid(self):
        fridge = Fridge()
        self.assertRaises(
            UnknownIngredientException,
            lambda: fridge.add_ingredient('Invalid ingredient name', 1)
        )
        self.assertRaises(
            ValueError,
            lambda: fridge.add_ingredient(ALL_INGREDIENTS[0], -5),
        )
        self.assertRaises(
            ValueError,
            lambda: fridge.add_ingredient(ALL_INGREDIENTS[0], 0),
        )

    def test_not_enough(self):
        fridge = Fridge()
        ingredient = ALL_INGREDIENTS[0]
        self.assertTrue(fridge.is_empty)
        self.assertRaises(
            NotEnoughException,
            lambda: fridge.use_ingredient(ingredient, 2)
        )
        fridge.add_ingredient(ingredient, 1)
        self.assertFalse(fridge.is_empty)
        self.assertRaises(
            NotEnoughException,
            lambda: fridge.use_ingredient(ingredient, 2)
        )

    def test_invalid_use(self):
        fridge = Fridge()
        self.assertTrue(fridge.is_empty)
        self.assertRaises(
            ValueError,
            lambda: fridge.add_ingredient(ALL_INGREDIENTS[0], -1),
        )
        self.assertTrue(fridge.is_empty)
        self.assertRaises(
            ValueError,
            lambda: fridge.add_ingredient(ALL_INGREDIENTS[0], 0),
        )
        self.assertTrue(fridge.is_empty)

    def test_multiple_usage(self):
        fridge = Fridge()
        first, second = ALL_INGREDIENTS[:2]
        ingredients = {first: 2, second: 4}
        self.assertTrue(fridge.is_empty)
        fridge.add_multiple_ingredients(ingredients)
        self.assertFalse(fridge.is_empty)
        ingredients[second] += 4
        self.assertRaises(
            NotEnoughException,
            lambda: fridge.use_multiple_ingredients(ingredients)
        )
        ingredients[second] -= 4
        self.assertFalse(fridge.is_empty)
        fridge.use_multiple_ingredients(ingredients)
        self.assertTrue(fridge.is_empty)
