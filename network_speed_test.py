# pip install speedtest-cli
import speedtest

test = speedtest.Speedtest()

print("Loading server list ......")
test.get_servers() # -> get list of servers
print("Choosing best server .........")
best = test.get_best_server() # -> Choose best server

print(f"Found {best['host']} located in {best['country']}")
print('Performing download test.....')
dwnld_result = test.download()
print("Performing  upload test.....")
upld_result = test.upload()
ping_result = test.results.ping

print(f"Download speed: {dwnld_result / 1024 / 1024:.2f} Mb/s")
print(f"Upload speed: {upld_result / 1024 / 1024:.2f} Mb/s")
print(f"Ping speed: {ping_result:.2f} ms")