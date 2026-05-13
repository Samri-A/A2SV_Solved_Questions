from collections import deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        n = len(recipes)

        indegree = {}
        graph = defaultdict(list)

        recipe = set(recipes)

        for i in range(n):
            for ingred in ingredients[i]:
                graph[ingred].append(recipes[i])
                if recipes[i] in indegree :
                    indegree[recipes[i]] += 1
                else:
                    indegree[recipes[i]] = 1


        queue = deque()
        for sup in supplies:
            queue.append(sup)

        result = []
        while queue:
            current = queue.popleft()

            if current in recipe:
                result.append(current)

            for neb in graph[current]:
                indegree[neb] -= 1

                if indegree[neb] == 0:
                    queue.append(neb)

        return result

            



        
        