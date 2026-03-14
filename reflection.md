# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
new game doesnt actually reset the game state.
the hint is not helpeful - says to go lower when the secret is higher
easy and hard mode have fewer attempts than normal mode. you would expect easy to have more attempts and hard to have fewer attempts than normal mode.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
I used Copilot for the project.
I provided to Copilot my suspects of what was causing issues in the reset game logic. It provided suggestions. I meticulously analyzed those suggestions. Then I asked it to generate pytest test case related to verifying game state reset. I verified it passed it.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I determined whether a bug was really fixed by running the app and running the tests.
Using pytests, I was able to determine whether AI was able to accurately refactor my code. I noticed with some tests I had written prior to refactoring the code no longer worked (due to name changes) and Copilot wasn't able to keep that context in mind while refactoring the code.
Copilot provided in depth analysis of my tests and helped explain the importance as well.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number was being regenerated every time the script ran. 

Every time you do something on the page (like typing in a box, clicking a button, or even just refreshing), it doesn't just update that one part; it reruns the entire Python script from top to bottom.

The fix was to save the number as part of the streamlit session state, more specifically 
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
    
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Asking AI to explain functionality.
Ask for it double check dependency functionality throughout the whole codebase. I noticed that after refactoring the codebase, it wasn't aware about updating the testing scripts, a critical aspect of functioanlity. I'll keep in mind to keep the dependency interactions for the future.
New perspective: AI geenerated is a great learning tool, but isn't perfect, especially with accoutnting for dependencies throughout the codebase.


