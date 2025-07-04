### Oauthbreaker解题思路

1. **从官网下载APK文件**  

2. **使用JADX-GUI反编译APK**  
   ```bash
   jadx-gui oauth.apk
￼

3. **检查AndroidManifest.xml**

4. **定位到 com.hacker101.oauth.MainActivity

<activity android:name="com.hacker101.oauth.MainActivity">

5. **查看源代码，发现存在特殊网址路径



6. **首次访问，发现跳转的链接


7. **访问，发现显示 Bad Request.果断开F12

8. **发现flag



