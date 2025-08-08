from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = {}
        supply = set(supplies)

        for i in range(len(recipes)):
            recipe = recipes[i]
            indegree[recipe] = 0
            for ingredient in ingredients[i]:
                if ingredient not in supply:
                    adj[ingredient].append(recipe)
                    indegree[recipe] += 1

        q = deque([recipe for recipe, deg in indegree.items() if deg == 0])

        res = []
        while q:
            curr_recipe = q.popleft()
            res.append(curr_recipe)

            for next_recipe in adj.get(curr_recipe, []):
                indegree[next_recipe] -= 1
                if indegree[next_recipe] == 0:
                    q.append(next_recipe)

        return res

if __name__ == "__main__":
    recipes = ["cake", "frosting", "birthdaycake"]
    ingredients= [["flour", "eggs"], ["sugar", "butter"], ["cake", "frosting"]]
    supplies = ["flour", "eggs", "sugar", "butter"]

    sol = Solution()
    result = sol.findAllRecipes(recipes, ingredients, supplies)
    print(result)
