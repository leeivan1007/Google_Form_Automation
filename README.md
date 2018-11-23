# Google_Form_Automation

[已開發功能] 自動登入-填寫表單-簡易提醒

[尚未開發] 退回上一步，更多的警告跟提醒

[config.txt] 內容第1.2行為登入帳號需要填寫的帳密。第3行為表單的url。第4行為填寫表單人的名稱[作者自己的業務需求]，可另外根據自己得需求修正config.txt檔跟程式碼。



元素的操作可以參考「selenium」：
https://selenium-python-zh.readthedocs.io/en/latest/locating-elements.html

如果要結合自己的按鈕操作，可以針對xpath的邏輯做修改，

或直接進入開發人員工具，點選 html 點元素按右鍵找xpath的值。

<img width='500px' src="https://github.com/leeivan1007/Google_Form_Automation/blob/master/demo.png"/>

'
import time
time.sleep(10)
'
