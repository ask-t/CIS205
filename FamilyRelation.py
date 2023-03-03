# Define the binary relation
family_relations = {
    ("John", "Tom"),   # John is Tom's father.
    ("Mary", "Tom"),   # Mary is Tom's mother
    ("Tom", "Emily"),  # Tom is Emily's father
    ("Tom", "Bob"),    # Tom is Bob's father
    ("Emily", "Sue"),  # Emily is Sue's mother
    ("Bob", "Mike"),   # Bob is Mike's father
    ("Sue", "Mike"),   # Sue is Mike's mother
}

# Define a function to get the children of a given person
def get_children(person):
    children = []
    for parent, child in family_relations:
        if parent == person:
            children.append(child)
    return children

# Define a function to get the descendants of a given person
def get_descendants(person):
    descendants = []
    children = get_children(person)
    descendants.extend(children)
    for child in children:
        descendants.extend(get_descendants(child))
    return descendants

# Test the functions
print("John's children:", get_children("John"))
print("Mary's children:", get_children("Mary"))
print("Tom's children:", get_children("Tom"))
print("Tom's descendants:", get_descendants("Tom"))

# Define a function to get the parents of a given person
def get_parents(person):
  parents = []
  for parent, children in family_relations:
    if children == person:
      parents.append(parent)
  return parents

# Test the functions
print("Tom's parents", get_parents("Tom"))
print("Emily's parents", get_parents("Emily"))
print("Mike's parents", get_parents("Mike"))
print("John's parents", get_parents("John")) # There is no Parents


# Define a function to get the ancestors of a given person
def get_ancestors(person):
    ancestors = []
    parents = get_parents(person)
    ancestors.extend(parents)
    for parent in parents:
        ancestors.extend(get_ancestors(parent))
    return ancestors

# Test the functions
print("Mike's acestors", list(set(get_ancestors("Mike"))))
