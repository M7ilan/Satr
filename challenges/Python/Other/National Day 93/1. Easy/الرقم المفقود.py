def find_missing_number(n: int, numbers: list[int]) -> int:
    total_sum = (n * (n + 1)) // 2
    array_sum = sum(numbers)
    missing_number = total_sum - array_sum

    return missing_number

"""
وصف التحدي
اكتب دالة function تستقبل عددًا صحيحًا integer و مصفوفة أعداد صحيحة ، تحتوي المصفوفة على جميع الأرقام من 1 إلى n باستثناء رقم واحد .

مهمتك هي العثور على العدد المفقود وإعادته.

المخرجات المتوقعة
الاختبار 1

المدخلات (Inputs)
n = 5
numbers = [3,5,4,2]
المخرجات (Outputs)
1
الاختبار 2

المدخلات (Inputs)
n = 3
numbers = [1,3]
المخرجات (Outputs)
2
الاختبار 3

المدخلات (Inputs)
n = 7
numbers = [1,7,5,4,2,6]
المخرجات (Outputs)
3
الاختبار 4

المدخلات (Inputs)
n = 10
numbers = [2,9,8,4,1,7,10,3,6]
المخرجات (Outputs)
5
"""