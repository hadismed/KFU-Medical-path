# تحلیلگر فشار خون - حدیث معصومی
def check_pressure():
    print("\n" + "="*30)
    print("برنامه تحلیل فشار خون برای دانشگاه کازان")
    print("="*30 + "\n")
    
    systolic = int(input("فشار سیستولیک (عدد بالا): "))
    diastolic = int(input("فشار دیاستولیک (عدد پایین): "))
    
    if systolic < 90 and diastolic < 60:
        return "⚠️ فشار خون پایین"
    elif 90 <= systolic < 120 and 60 <= diastolic < 80:
        return "✅ فشار خون طبیعی"
    else:
        return "🔴 نیاز به بررسی پزشکی"

# اجرای برنامه
result = check_pressure()
print("\nنتیجه:", result)
