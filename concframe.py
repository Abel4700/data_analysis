from graphviz import Digraph

dot = Digraph(comment='Conceptual Framework for Trend Analysis of Social Work Professionalism')

# Contextual Considerations
dot.node('A', 'NASW Code of Ethics', shape='box', style='rounded,filled', fillcolor='lightblue')
dot.node('B', 'Humanitarian Context', shape='box', style='rounded,filled', fillcolor='lightblue')
dot.node('C', 'Capacity of Humanitarian Workers', shape='box', style='rounded,filled', fillcolor='lightblue')

# Core Concepts
dot.node('D', 'Types of Child-Focused Social Work Services', shape='ellipse', style='filled', fillcolor='lightyellow')

# Research Objectives
dot.node('E', 'Describing Social Work Services', shape='box', style='rounded,filled', fillcolor='lightgreen')
dot.node('F', 'Service Delivery Analysis', shape='box', style='rounded,filled', fillcolor='lightgreen')
dot.node('G', 'Trend Analysis', shape='box', style='rounded,filled', fillcolor='lightgreen')
dot.node('H', 'Influencing Factors', shape='box', style='rounded,filled', fillcolor='lightgreen')
dot.node('I', 'Implications of Trends', shape='box', style='rounded,filled', fillcolor='lightgreen')

# Expected Outcomes
dot.node('J', 'Understanding Application', shape='box', style='rounded,filled', fillcolor='lightpink')
dot.node('K', 'Identifying Service Trends', shape='box', style='rounded,filled', fillcolor='lightpink')
dot.node('L', 'Contributing Factors Analysis', shape='box', style='rounded,filled', fillcolor='lightpink')
dot.node('M', 'Impact Assessment', shape='box', style='rounded,filled', fillcolor='lightpink')

# Edges
dot.edge('A', 'D')
dot.edge('B', 'D')
dot.edge('C', 'D')
dot.edge('D', 'E')
dot.edge('D', 'F')
dot.edge('D', 'G')
dot.edge('D', 'H')
dot.edge('D', 'I')
dot.edge('E', 'J')
dot.edge('F', 'K')
dot.edge('G', 'L')
dot.edge('H', 'M')
dot.edge('I', 'M')

# Render the graph
dot.render('conceptual_framework', format='png', view=True)
