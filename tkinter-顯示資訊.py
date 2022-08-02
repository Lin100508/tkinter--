import tkinter as tk                             # 在Python 3.x 匯入該tkinter 函式庫
win = tk.Tk()                                    # 步驟2：建立GUI 應用程式的主視窗
win.wm_title("背心資訊")                           #設定主視窗
win.resizable(width=False,height=True)
win.minsize(width=300,height=200)                #最小尺寸
win.maxsize(width=300,height=300)                #最大尺寸


class commodity(object):  # 繼承Python 最上層的object 類別
   commodity_name = "背心"
   commodity_color = "黑色"
   commodity_size = "M"
   commodity_length = 40
   commodity_width = 60
   commodity_quantity = 10
   commodity_price = 250

   def __init__(self, name, color ,size,length,width,quantity,price):  # 類別初始化的函數 initialize 一開始要做的函數
       self.commodity_name = name
       self.commodity_color = color
       self.commodity_size = size
       self.commodity_length = length
       self.commodity_width = width
       self.commodity_quantity = quantity
       self.commodity_price = price

   def info(self):                              #  Method 方法
       print("商品類別:",self.commodity_name)
       print("商品顏色:", self.commodity_color)
       print("商品尺寸:", self.commodity_size)
       print("商品長度:", self.commodity_length)
       print("商品寬度:", self.commodity_width )
       print("商品數量:", self.commodity_quantity)
       print("商品價格:", self.commodity_price)

commodity1=commodity(name="背心",color="黑色",size="M",length=40,width=60,quantity=10,price=250)
commodity1.info()

label22=tk.Label(win,text="商品名稱:背心")      #建立文字
label22.place(x=20,y=50)                      #指定元件位置

label22=tk.Label(win,text="商品顏色:黑色")       #建立文字
label22.place(x=20,y=70)                      #指定元件位置

label22=tk.Label(win,text="商品尺寸:M")         #建立文件
label22.place(x=20,y=90)                     #指定元件位置

label22=tk.Label(win,text="商品長度:40")         #建立文字
label22.place(x=20,y=110)                      #指定元件位置

label22=tk.Label(win,text="商品寬度:60")         #建立文字
label22.place(x=20,y=130)                      #指定元件位置

label22=tk.Label(win,text="商品數量:10")         #建立文字
label22.place(x=20,y=150)                      #指定元件位置

label22=tk.Label(win,text="商品價格:250")         #建立文字
label22.place(x=20,y=170)                      #指定元件位置

win.mainloop()                               # 最後步驟：程式做無限循環
