"""
A collection of n activities S = {a1,..., an} is given. Each activity has a start time and a finish time, ai = (si,fi). Assume that only one machine is available for performing activities, so only one activity can be executed at a time on this machine. Write a program to find maximum number of activities that can be scheduled in a single time frame using one machine. Sample data is given below, however, create a generalized program which can run on any other input data.

Ex, Input:
-------------------------------------------------
| Activity, ai    | a1 | a2 | a3 | a4 | a5 | a6 |
| Start time, si  |  1 |  2 |  3 |  4 |  7 |  8 |
| Finish time, fi |  3 |  5 |  4 |  7 | 10 |  9 |
-------------------------------------------------
Then output will be {a1,a3,a4,a6}.
"""

def activity_selection(activities):
    # Sort the list by the third item (finish time) in each tuple
    sorted_activities = sorted(activities, key=lambda x: x[2])  
    
    
    selected = []
    last_finish_time = 0

    for act in sorted_activities:
        if act[1] >= last_finish_time:
            selected.append(act[0])
            last_finish_time = act[2]
    
    return selected

# Input format: (activity_name, start_time, finish_time)
activities = [
    ("a1", 1, 3),
    ("a2", 2, 5),
    ("a3", 3, 4),
    ("a4", 4, 7),
    ("a5", 7, 10),
    ("a6", 8, 9)
]

result = activity_selection(activities)
print("Selected Activities:", result)



"""
📝 Problem Explanation:

You are given a list of activities.
Each activity has:

* a start time (when it begins), and
* a finish time (when it ends).

You have only one machine, so only one activity can run at a time.
You need to find the maximum number of non-overlapping activities that can be done on the machine.

🎯 Goal:
Find the maximum number of activities that can be scheduled without overlapping.

💡 What's the logic to solve it? (Greedy Algorithm)
We want to select activities that finish earliest so we can do more activities after them.

✅ Steps:
* Sort all activities by their finish time.
* Always choose the activity with the earliest finish time that doesn't overlap with the previously selected activity.
* Repeat until all activities are checked.

Now pick activities one by one:
* Pick a1 → finish at 3
* Next, pick a3 (starts at 3 ≥ 3) → finish at 4
* Next, pick a4 (starts at 4 ≥ 4) → finish at 7
* Next, pick a6 (starts at 8 ≥ 7) → finish at 9
⚠️ Cannot pick a2 (starts at 2 < 3) → overlaps
⚠️ Cannot pick a5 (starts at 7 < 9) → overlaps with a6

✅ Final Answer:
The activities that can be selected are:
{a1, a3, a4, a6}
"""