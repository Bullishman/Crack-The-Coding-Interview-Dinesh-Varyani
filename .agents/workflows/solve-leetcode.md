---
description: Automates the process of finding, selecting, and explaining a LeetCode solution from the Excel tracker.
---

# LeetCode Auto-Solver Workflow

Follow these steps exactly when the user triggers this workflow with a problem number (e.g., `009`):

1. **Find the Problem URL:**
   - Execute a Python command to read `Crack The Coding Interview.xlsx` and find the row where the `Number` matches the requested problem number (ignoring leading zeros).
   - Extract the LeetCode URL from the `Question` column.
   - Extract the problem name from the URL (e.g., `container-with-most-water` from `https://leetcode.com/problems/container-with-most-water`).

2. **Analyze and Find Solutions:**
   - Use your internal knowledge or web search to find the best Python approaches for the problem (e.g., Brute Force, optimal O(N) Two Pointers, etc.).
   - Present 2-3 good code options to the user, explaining the time/space complexity and the reasoning behind each approach.

3. **Wait for Selection:**
   - Ask the user which code option they prefer. Wait for their choice. (Use `notify_user` if in a task boundary).

4. **Save the Code:**
   - Once the user selects an option, create the directory if it doesn't exist: `Must Do Questions (1 - 500)\<padded-number>-<problem-name>\`.
   - Write the Python code to the file at `C:\Projects2\Crack-The-Coding-Interview-Dinesh-Varyani\Must Do Questions (1 - 500)\<padded-number>-<problem-name>\<problem-name>.py`.

5. **Demonstrate and Trace:**
   - Provide a final response that demonstrates the written code line-by-line using an example.
   - Include a **live trace table map** showing the state of variables at each step of the loop/iteration for the example.

