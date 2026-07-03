# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
3017/Bill
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
542248
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
15-30 minutes
```

---

## 2. ความเข้าใจโจทย์ของฉัน

```text
Input คือ จำนวนเงินรวมเฉพาะค่าอาหารและเครื่องดื่ม
Output คือ จำนวนทั้งหมดที่ต้องจ่ายทั้งหมดกำหนดทศนิยม 2 หลัก
```

---

## 3. แผนแรกของฉัน

```text
Step 1:รับ input ของค่าอาหารและเครื่องดื่ม
Step 2:นำไปคำนวนค่าบริการ 10% ถ้าน้อยกว่า 50 บาท ให้บวกเพิ่ม 50 บาทเป็นขั้นต่ำ และจำกัดไว้ไม่เกิน 1000 บาท
Step 3:นำผลรวมทั้งหมดคือ ค่าอาหารเตรื่องดื่มและบริการ ไปคำนวน VAT 7%
Step 4:แสดงผลลัพธ์ที่คำนวนได้เป็นจำนวนจริงทศนิยม 2 หลัก
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
ใช้วิธีเดียวกันกับแผนแรก
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
เพื่อดูกรณีที่ค่าบริการต่ำกว่า 50 
```

Input:

```text
1
```

Expected output:

```text
54.57
```

Actual output:

```text
54.57
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เพื่อดูกรณีที่ค่าบริการเกิน 1000 
```

Input:

```text
15000
```

Expected output:

```text
17120.00
```

Actual output:

```text
17120.00
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ทดลอง case ที่ค่าบริการอยู่ระหว่าง 50-1000
```

Input:

```text
2000
```

Expected output:

```text
2354.00
```

Actual output:

```text
2354.00
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

ใช้ AI กับโจทย์นี้หรือไม่

```text
No
```

ถ้าใช้ AI ต้องทำไฟล์นี้ด้วย:

```text
ai_reflection.md
```

ถ้าถามเฉพาะเพื่อน TA หรือผู้สอน และไม่ได้ใช้ AI ไม่ต้องทำ `ai_reflection.md`

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

คุณคัดลอก code จากคนอื่นหรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. |`Yes`|
| I understand my final code. |`Yes`|
| I recorded the real OJ status. |`Yes`|
| I did not copy AI-generated text directly into this file. |`Yes`|
| I did not copy code from another person. |`Yes`|
| If I received human help, I disclosed it in this file. |`Yes`|
| I submitted the final code to the OJ by myself. |`Yes`|
