import time
def hello():
    time.sleep(1)

def run():
    for i in range(5):
        hello()
        print(f"hello world:{time.time()}")

if __name__ == '__main__':
    run()
