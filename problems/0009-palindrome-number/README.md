# 0009. Palindrome Number

## 題目

判斷一個整數是否為回文數（正著讀與反著讀相同）。

---

## 類型

* String
* Math

---

## 思路（目前解法）

將整數轉成字串，然後用 slicing 反轉：

```python
x = str(x)
return x[::-1] == x
```

👉 核心概念：

* Python 字串支援反轉（`[::-1]`）
* 直接比較即可判斷是否回文

---

## 為什麼這樣做

把數字轉成字串後：

```text
121 → "121"
```

反轉：

```text
"121"[::-1] → "121"
```

如果相同 → 就是回文

---

## 複雜度

* Time: O(n)
* Space: O(n)

（因為建立了新字串）

---

## 卡點 / 觀察

* 一開始沒有想到可以用 slicing 快速反轉
* 忘記 Python 字串是 immutable（會建立新物件）

---

## 更好的解法（進階）

👉 不使用字串，直接用數學方法（LeetCode 期望）

核心：

* 取出最後一位數字
* 組成反轉的一半數字

關鍵想法：

```text
12321 → 比較前半與後半
```

👉 可以做到：

* Time: O(log n)
* Space: O(1)

---

## Pattern

* Reverse & Compare
* Digit manipulation（進階）