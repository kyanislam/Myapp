[app]

# اسم التطبيق اللي هيظهر للمستخدم
title = MyKivyApp

# اسم الحزمة (Package name)
package.name = mykivyapp

# الدومين الخاص بالحزمة
package.domain = org.test

# مكان الكود (ملفات py و kv)
source.dir = .

# الامتدادات المسموح بيها
source.include_exts = py, kv

# نسخة التطبيق
version = 1.0.0

# المكتبات المطلوبة
requirements = python3, kivy==2.3.0, kivymd==1.2.0

# اتجاه الشاشة
orientation = portrait

# تشغيل ملء الشاشة (0 = لا)
fullscreen = 0

# أقل نسخة Android مدعومة
android.minapi = 21

# نسخة Android API المستهدفة
android.api = 31

# نسخة الـ NDK
android.ndk = 25b

# bootstrap المستخدم
android.bootstrap = sdl2

# دعم AndroidX (مطلوب للإصدارات الحديثة)
android.enable_androidx = True


[buildozer]

# مستوى اللوج (تفصيلي عشان الأخطاء تبان)
log_level = 2

# تحذير عند استخدام root
warn_on_root = 1
