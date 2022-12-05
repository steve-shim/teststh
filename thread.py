import threading
import time

def each_thread_task(value):
    local = threading.local()  # TLD object 생성
    print(local)
    local.value = value        # 각 TLD별로 값 할당
    time.sleep(1)
    print(f"Stored value: {local.value}")
    

# 메인 thread가 새로운 thread들을 생성하여 each_thread_task 함수 실행
threading.Thread(target=each_thread_task, args=(1,)).start()
time.sleep(0.5)
threading.Thread(target=each_thread_task, args=(2,)).start()

# def shared_global_thread_task(value):
#     global local
#     print(f"Input value: {local}")
#     local.value = value        # 각 TLD별로 값 할당
#     time.sleep(1)
#     print(f"Stored value: {local.value}")
    
    
# local = threading.local()
# threading.Thread(target=shared_global_thread_task, args=(1,)).start()
# time.sleep(0.5)
# threading.Thread(target=shared_global_thread_task, args=(2,)).start()