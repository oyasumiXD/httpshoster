import http.server
import socketserver

print('''░▒█░▒█░▀█▀░▀█▀░▄▀▀▄░█▀▀░▒█░▒█░▄▀▀▄░█▀▀░▀█▀░█▀▀░█▀▀▄
░▒█▀▀█░░█░░░█░░█▄▄█░▀▀▄░▒█▀▀█░█░░█░▀▀▄░░█░░█▀▀░█▄▄▀
░▒█░▒█░░▀░░░▀░░█░░░░▀▀▀░▒█░▒█░░▀▀░░▀▀▀░░▀░░▀▀▀░▀░▀▀
''')
print("Https Website Hoster by oyasumiXD")
print("since the app is shit coded, put it in the folder you want to be hosted")
ip = input("Enter the IP address: ")

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((ip, 433), Handler) as httpd:
    print(f"Website started at {ip}:433")
    httpd.serve_forever()
