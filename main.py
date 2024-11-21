from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Set of guards and walls for fast lookups
        guards_set = set(tuple(guard) for guard in guards)
        walls_set = set(tuple(wall) for wall in walls)

        # Directions for north, south, east, west
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Create a set to keep track of all the cells that are guarded
        guarded = set()

        # For each guard, mark all cells they can see
        for guard in guards:
            for direction in directions:
                r, c = guard
                while True:
                    r += direction[0]
                    c += direction[1]
                    
                    # Check if we are out of bounds
                    if r < 0 or r >= m or c < 0 or c >= n:
                        break
                    
                    # If the cell is a wall or guard, stop marking cells
                    if (r, c) in walls_set or (r, c) in guards_set:
                        break
                    
                    # Mark the cell as guarded
                    guarded.add((r, c))

        # Now count unguarded cells that are not walls or guards
        unguarded_cells = 0
        for r in range(m):
            for c in range(n):
                if (r, c) not in guards_set and (r, c) not in walls_set and (r, c) not in guarded:
                    unguarded_cells += 1

        return unguarded_cells
