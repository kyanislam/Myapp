[app]

title = Azkar App
package.name = azkarapp
package.domain = org.myapp
source.dir = .
source.include_exts = py,kv,ttf,png,jpg,atlas

requirements = python3,kivy,arabic_reshaper,python-bidi
orientation = portrait
fullscreen = 0

android.archs = armeabi-v7a, arm64-v8a
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_api = 21
android.gradle_dependencies = 

log_level = 2

# لو معاك خط عربي لازم تضيفه
android.presplash_color = #FFFFFF
