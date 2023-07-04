class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        indegree = defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients):
            indegree[recipe] =  len(ingredient)

            for ing in ingredient:
                graph[ing].append(recipe)

        q = deque(supplies)

        recipes = set(recipes)

        ans = []

        while q:
             
            supply = q.popleft()

            if supply in recipes:
                ans.append(supply)

            for ingredient in graph[supply]:
                
                indegree[ingredient] -= 1

                if indegree[ingredient] == 0:
                    q.append(ingredient)


        return ans

      
