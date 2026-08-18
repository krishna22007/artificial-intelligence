def is_valid(region, color, assignment, graph):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve_map_coloring(assignment, graph, colors, variables):
    if len(assignment) == len(variables):
        return assignment
    
    # Pick the next unassigned variable
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]
    
    for color in colors:
        if is_valid(var, color, assignment, graph):
            assignment[var] = color
            
            result = solve_map_coloring(assignment, graph, colors, variables)
            if result is not None:
                return result
            
            del assignment[var]  # Backtrack
            
    return None

# Map configuration (Australia Map Example)
regions = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors = ['Red', 'Green', 'Blue']

map_graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

solution = solve_map_coloring({}, map_graph, colors, regions)

if solution:
    print("Valid Map Coloring Solution Found:")
    for region, color in solution.items():
        print(f"{region:4} -> {color}")
else:
    print("No valid coloring solution found.")
