import sqlite3

connection = sqlite3.connect('d1093fe7-995d-44c9-8728-673af8914cf8.db')
cursor = connection.cursor()

cursor.execute('SELECT first_name AS "First Name", last_name AS "Last Name" FROM employees')
results1 = cursor.fetchall()
cursor.execute('SELECT DISTINCT department_id FROM employees')
results2 = cursor.fetchall()
cursor.execute('SELECT * FROM employees ORDER BY first_name DESC')
results3 = cursor.fetchall()
cursor.execute('SELECT first_name, last_name, salary, ROUND(salary * 0.12, 2) AS PF FROM employees')
results4 = cursor.fetchall()
cursor.execute('SELECT MAX(salary) AS "Maximum Salary", MIN(salary) AS "Minimum Salary" FROM employees')
results5 = cursor.fetchall()
cursor.execute('SELECT first_name, last_name, ROUND(salary / 12, 2) AS "Monthly Salary" FROM employees')
results6 = cursor.fetchall()


print(results1, results2, results3, results4, results5, results6, sep='\n')

connection.commit()
connection.close()
