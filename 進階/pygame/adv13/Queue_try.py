from collections import deque


snack_queue = deque()


snack_queue.append("小明")
snack_queue.append("小華")
snack_queue.append("小強")
print(f"初始隊列:{snack_queue}")

first_student = snack_queue.popleft()
print(f"{first_student}已經購買點心並離開隊列")

print(f"現在的隊列:{snack_queue}")

snack_queue.append("小美")
print(f"小美加入隊列")
print(f"最終隊列:{snack_queue}")