# Text-to-SQL-LLM

![image](https://github.com/user-attachments/assets/9001f224-3e14-4644-9b1c-c48043dcbb3f)

 Architecture Overview:
1️⃣ User: Sends natural language queries (e.g., "List all customers from New York").
2️⃣ Flask API:
	•	Accepts POST requests.
	•	Sends the query to GenAI (e.g., OpenAI, Ollama, Hugging Face model).
	•	GenAI converts NL → SQL.
3️⃣ SQL Executor:
	•	Flask safely runs the generated SQL against Postgres.

4️⃣ Response:
	•	Returns SQL + results (or error messages).

 Pre-requisites
 1. Posgress in local
 2. Setup ollama llama2 in local
 3. VS Code

1. Make sure that Ollama is running in your machine
2. ollama run llama2

![image](https://github.com/user-attachments/assets/3640bef7-236c-441c-bd79-5ea7c4079054)

3. Validate Postress and create 3 tables for testing purpose and load data
![image](https://github.com/user-attachments/assets/7b2fdb00-3419-41e1-8887-3353c9263283)

4. We will be using this flask api code ![image](https://github.com/user-attachments/assets/d32932bc-d0cc-48e7-883c-37c23b530415)
5. To run this file ![image](https://github.com/user-attachments/assets/0560f194-eaba-4087-9d9d-08ee16044f70)

6. Open another terminal in VScode
7. Now it is ready to test some queries
8. This is the query I passed to Flask API -  url -X POST http://127.0.0.1:5000/text-to-sql \                                                                                 
     -H "Content-Type: application/json" \
     -d '{"query": "List all customers who signed up after January 1, 2023."}'

9. I go the following result ![image](https://github.com/user-attachments/assets/90f74c3e-4c4d-4bc5-bbff-0520c5922907)
10. check the result and compare with DB values  ![image](https://github.com/user-attachments/assets/33ca26fc-12a4-4a6f-9190-8f262d374be6)
11. Check the next query and result ![image](https://github.com/user-attachments/assets/837a65db-2670-4f83-b824-3d8337282858)
12. Another example based on Weather table ![image](https://github.com/user-attachments/assets/65bdeeca-3a21-4e37-8bfd-807506de13b7)


Note:- I have attached SQL Scripts and few sample queries with this reposiroty for your reference



