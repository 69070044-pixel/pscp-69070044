# บันทึกการแก้โจทย์

---

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
3011/Colors
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
543109
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
30-60 minutes
```

---

## 2. ความเข้าใจโจทย์ของฉัน

```text
Input คือ แม่สีทั้ง 3 สีในรูปแบบของข้อความ string
Output คือ ข้อความที่บอกสีที่ผสมได้และ Error เมื่อสีที่ Input ไม่ใช่ Red, Yellow, Blue
```

---

## 3. แผนแรกของฉัน

```text
Step 1:สร้าง function main เพื่อจะใช้ return ในกรณีที่เกิด Error เพื่อให้หยุดทำงานทันที
Step 2:รับ Input คือแม่สีทั้ง 2 และสร้าง color_set ที่เป็น Dict เพื่อแปลงค่าเป็นตัวเลข
Step 3:check ว่าสีที่รับเข้ามาอยู่ในแม่สีทั้ง 3 มั้ยด้วยการใช้ Keys จาก color_set
Step 4:ถ้าไม่ Error ให้ไปอ่านเงื่อนไขต่อว่าผสมกันได้สีอะไร เช่น Orange, Violet, Green
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
Step 1: รับ Input ของสีทั้งสอง
Step 2: นำสีที่รับค่ามาไปเก็บเป็นคู่ใน Tuple
Step 3: นำไปตรวจสอบค่าและทำตามเงื่อนไขจากนั้นแสดงผล
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
Test เมื่อ Input เป็นค่าว่าง
```

Input:

```text


```

Expected output:

```text
Error
```

Actual output:

```text
Error
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ทดสอบใส่สีที่ไม่ใช่แม่สี 1 สี
```

Input:

```text
Red
Pink
```

Expected output:

```text
Error
```

Actual output:

```text
Error
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ทดสอบเมื่อใส่แม่สีผสมสีซ้ำ
```

Input:

```text
Red
Red
```

Expected output:

```text
Red
```

Actual output:

```text
Red
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
