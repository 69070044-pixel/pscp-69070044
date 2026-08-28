"""BigFrame"""
text, frame_len = [], 0
for _ in range(5):
    try:
        TEXT_INPUT = input().strip()
    except EOFError: #ดัก EOFError
        TEXT_INPUT = ""
    frame_len = max(frame_len, len(TEXT_INPUT) + 4)
    text.append(TEXT_INPUT)
print("*"*frame_len)
for t in text:
    print(f"* {t}{" "*((frame_len) - (len(t) + 3))}*")
print("*"*frame_len)
