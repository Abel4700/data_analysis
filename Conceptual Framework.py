from graphviz import Digraph

dot = Digraph(comment='Conceptual Framework for Trend Analysis of Social Work Professionalism')

# Contextual Considerations
dot.node('A', 'NASW Code of Ethics')
dot.node('B', 'Humanitarian Context')
dot.node('C', 'Capacity of Humanitarian Workers')

# Core Concepts
dot.node('D', 'Types of Child-Focused Social Work Services')

# Research Objectives
dot.node('E', 'Describing Social Work Services')
dot.node('F', 'Service Delivery Analysis')
dot.node('G', 'Trend Analysis')
dot.node('H', 'Influencing Factors')
dot.node('I', 'Implications of Trends')

# Expected Outcomes
dot.node('J', 'Understanding Application')
dot.node('K', 'Identifying Service Trends')
dot.node('L', 'Contributing Factors Analysis')
dot.node('M', 'Impact Assessment')

# Edges
dot.edges(['AD', 'BD', 'CD'])
dot.edges(['DE', 'DF', 'DG', 'DH', 'DI'])
dot.edges(['EJ', 'FK', 'GL', 'HM', 'IM'])

# Render the graph
dot.render('conceptual_framework', view=True)
