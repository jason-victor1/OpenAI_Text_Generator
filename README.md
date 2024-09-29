# ChatGPT Text Generator with OpenAI API

### Project Overview
I created a Python script that interacts with OpenAI's API to generate text using the **ChatGPT** model. The script was designed to generate catchy YouTube titles for email marketing topics. This README outlines how I set up the project along with the issues and the solutions.

### Step by Step Outline

1. **Signed into OpenAI**:
   I logged into the [OpenAI platform](https://platform.openai.com/), navigated to the **API section**, and created my unique **Project API Key**. This key allowed me to authenticate my requests to OpenAI's API.

2. **Note on OpenAI API Costs**:
   OpenAI’s API is not free. Every time I asked OpenAI to generate text, it counted the number of tokens (which include words, spaces, and punctuation). The more tokens used, the higher the cost. Please keep this in mind when using the API.

3. **Set Up the Python Script**:
   I created an empty Python script file called `chatgpt.py` in **VS Code**. This script would contain the code that interacts with OpenAI’s API.

4. **Installed the OpenAI Python Package**:
   Using the terminal, I installed the **OpenAI** Python package by running the following command:
   ```bash
   python3.12 -m pip install openai
   ```

5. **Developed the Python Script**:
   I wrote a Python script to generate text using ChatGPT. The script sends a request to the OpenAI API, asking it to generate 5 catchy YouTube titles about email marketing tricks. You can find the attached script in the repository: [chatgpt.py](./chatgpt.py).

   Here's the prompt I used in the script:
   ```
   Generate 5 catchy YouTube titles about [email marketing tricks]
   ```

### Issues and Solutions

I encountered several issues throughout the process. Please see the following errors:

#### **1. Import Error**:
When I first tried to import the OpenAI package, I encountered an `ImportError`. This was because the OpenAI package wasn’t installed properly or was missing.

**Error**:
```bash
Traceback (most recent call last):
  File "chatgpt.py", line 1, in <module>
    import openai
ModuleNotFoundError: No module named 'openai'
```

**Solution**:
I installed the OpenAI package using pip with the following command:
```bash
python3.12 -m pip install openai
```
Once the installation was successful, the error was resolved.

---

#### **2. NameError: `OpenAI` Not Defined**:
While trying to instantiate the OpenAI client, I mistakenly used `OpenAI` instead of `openai`, which resulted in a `NameError`.

**Error**:
```bash
Traceback (most recent call last):
  File "chatgpt.py", line 13, in <module>
    client = OpenAI(
             ^^^^^^
NameError: name 'OpenAI' is not defined. Did you mean: 'openai'?
```

**Solution**:
I corrected the usage by switching from `OpenAI` to `openai`, which is the correct way to use the OpenAI Python package. Here's the updated code:
```python
import openai

openai.api_key = "your-api-key-here"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_prompt}]
)
```

---

#### **3. Model Not Found Error**:
Initially, I tried using the `gpt-4o` model, which resulted in a `model not found` error. This happened because my API key didn’t have access to that specific model.

**Error**:
```bash
openai.NotFoundError: Error code: 404 - {'error': {'message': 'The model `gpt-4o` does not exist or you do not have access to it.'}}
```

**Solution**:
After checking my API key permissions on the OpenAI dashboard, I updated the model to **gpt-3.5-turbo**, which resolved the issue:
```python
completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": user_prompt}]
)
```

---

#### **4. Quota Exceeded Error (Rate Limit)**:
After running the script multiple times, I encountered an `insufficient_quota` error due to exceeding my API usage limit for the month.

**Error**:
```bash
openai.RateLimitError: Error code: 429 - {'error': {'message': 'You exceeded your current quota, please check your plan and billing details.'}}
```

**Solution**:
I resolved this by reviewing my usage limits in the [OpenAI billing section](https://platform.openai.com/account/usage) and making sure my billing information was up to date. Once I upgraded my plan, the issue was resolved.

---

### Script Output

Once everything was set up correctly, the script ran successfully and generated the following catchy YouTube titles:

```
1. "Unlock the Secrets of Email Marketing: 5 Expert Tricks Revealed!"
2. "Boost Your Email Marketing ROI with These 5 Game-Changing Tricks!"
3. "Email Marketing Mastery: 5 Proven Tricks for Success"
4. "Get More Opens and Clicks with These 5 Email Marketing Tricks!"
5. "Maximize Your Email Campaigns: 5 Creative Tricks to Try Today!"
```

### Conclusion
This project was a great learning experience for working with OpenAI’s API to generate text. While I encountered a few challenges, I was able to resolve them by troubleshooting API access, fixing errors, and ensuring proper usage of the OpenAI Python library.

Feel free to check out the attached script: [chatgpt.py](./chatgpt.py)




