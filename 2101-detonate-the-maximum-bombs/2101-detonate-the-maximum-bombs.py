class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        

        graph = defaultdict(list)

        for b in range(len(bombs)):

            x_bomb = bombs[b][0]
            y_bomb = bombs[b][1]
            r_bomb = bombs[b][2]

            for i in  range(len(bombs)):
                if b == i :
                    continue
                
                next_x_bomb = bombs[i][0]
                next_y_bomb = bombs[i][1]
                next_r_bomb = bombs[i][2]

                dis = sqrt((x_bomb - next_x_bomb) ** 2 + (y_bomb - next_y_bomb)**2)

                if dis <= r_bomb:
                    graph[b].append(i)
                
                if dis <= next_r_bomb:
                    graph[i].append(b)

        def dfs(i , seen):

                if i in seen:
                    return 0

                seen.add(i)
                for ner in graph[i]:
                    dfs(ner, seen)

                
                return len(seen)

        result = 0

        for i in range(len(bombs)):
            result = max(result ,dfs(i, set()))

        return result



                
                

