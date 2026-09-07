"""สมดุลย์ชีวิต"""
n, working_time = int(input()), []
for _ in range(n):
    working_time.append(int(input()))

max_value = working_time.index(max(working_time))
working_list = [working_time.pop(max_value)]

while working_time:
    if working_list[-1] > 18:
        for i, h in enumerate(working_time):
            if h < 18:
                working_list.append(working_time.pop(i))
                break
        else:
            working_list.append(0) # ไม่มีงานที่ได้นอนก่อนเที่ยงคืนแล้ว 0 คือวันพัก
    else:
        work = working_time.pop(0)
        working_list.append(work)
print(len(working_list))
