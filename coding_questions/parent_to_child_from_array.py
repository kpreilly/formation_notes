'''
❓ PROMPT
Given an array of arrays representing relations  *child, parent1,
and parent2* in each row, print a string representing all children
of each parent.

For example: *Ben is the parent of James, Jen*. The formatting
doesn't matter as long as all children are represented in the
final output. You will need to return the entire result as
strings separated by newlines to match against the strings
in these comparisons accurately.

return parentRelationships.join("\n") //javascript
return "\n".join(parentRelationships) #python

Example(s)
Input: []
Output: 'No family relations'

Input: [
  ["James", "Ben", "Lisa"],
  ["George", "Taylor", "Fred"],
  ["Jen", "Ben", "Gloria"]
]
Output:
'Ben is the parent of James, Jen'
'Lisa is the parent of James'
'Taylor is the parent of George'
'Fred is the parent of George'
'Gloria is the parent of Jen'

🔎 EXPLORE
List your assumptions & discoveries:
A single array from the matrix will be of length <= 3
Key: Parent, Value: Child
What if a child has no parents? This should probably throw an error

Insightful & revealing test cases:


🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #:
- Iterate through each element in the input array.
- for each element, indices 1 and 2 will be treated as keys.
Index 1 will be added to the hashmap
- after parsing the input matrix, print the results "{key} is the parent of {value1}, {value2}, ..."

🛠️ IMPLEMENT
function parentToChild(relations) {
def parentToChild(relations: list[list[str]]) -> str:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
import config as config

from collections import defaultdict

def parentToChild(relations: list[list[str]]) -> str:
    if not relations or len(relations) == 0:
        return "No family relations"
    result = defaultdict(list)
    # Parse relations
    for relation in relations:
        if 1 < len(relation):
            result[relation[1]].append(relation[0])
        if 2 < len(relation):
            result[relation[2]].append(relation[0])

    # Print child list for each parent
    message = []
    for key, values in result.items():
        message.append(f"{key} is the parent of ")
        message.append(', '.join(values))
        message.append("\n")
    return ''.join(message)

def my_tests():
    print("-- Test 1 --")
    print("Expect:\nBen is the parent of James\nLisa is the parent of James")
    print("Result:")
    print(parentToChild([["James", "Ben", "Lisa"]]))

    print("-- Test 2 --")
    print("Expect:\nBen is the parent of James, Tim\nLisa is the parent of James")
    print("Result:")
    print(parentToChild([["James", "Ben", "Lisa"], ["Tim", "Ben"]]))
    
    print("-- Test 3 --")
    print("Expect:\nNo family relations")
    print("Result:")
    print(parentToChild([]))

def formation_tests():
    relations = []
    print(parentToChild(relations) == "No family relations")

    relations = [["James", "Ben", "Lisa"]]
    print(parentToChild(relations) ==
    "\
    Ben is the parent of James\n\
    Lisa is the parent of James"
    )

    relations = [
        ["James", "Ben", "Lisa"],
        ["George", "Taylor", "Fred"],
        ["Jen", "Ben", "Gloria"]
    ]
    print(parentToChild(relations) ==
    "\
    Ben is the parent of James,Jen\n\
    Lisa is the parent of James\n\
    Taylor is the parent of George\n\
    Fred is the parent of George\n\
    Gloria is the parent of Jen"
    )

    relations = [
        ["Justine", "Tony", "Jessica"],
        ["Paavo", "Jessica", "Tony"],
        ["Zoe", "Jessica", "Tony"],
        ["Benana", "Ben", "Ana"],
        ["Egg", "Rooster", "Hen"],
        ["Eggart", "Duck", "Hen"],
        ["Mule", "Horse", "Donkey"],
    ]
    print(parentToChild(relations) ==
    "\
    Tony is the parent of Justine,Paavo,Zoe\n\
    Jessica is the parent of Justine,Paavo,Zoe\n\
    Ben is the parent of Benana\n\
    Ana is the parent of Benana\n\
    Rooster is the parent of Egg\n\
    Hen is the parent of Egg,Eggart\n\
    Duck is the parent of Eggart\n\
    Horse is the parent of Mule\n\
    Donkey is the parent of Mule"
    )

if __name__ == "__main__":
    
    if config.my_tests:
        print("\n~~ Running my_tests ~~")
        my_tests()
        print("~~ End my_tests ~~")
    if config.formation_tests:
        print("\n~~ Running formation_tests ~~")
        formation_tests()
        print("~~ End formation_tests ~~")