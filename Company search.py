import tkinter
from csv import reader

def create_industry_filter(item_names):
     def check(row):
         result = []
 
         for item in item_names:
             result.append(item in row[1])
         
         return any(result)if len(result) != 0 else True
 
     return check
 
def create_sales_filter(item_names):
    def check(row):
        result = []

        for item in item_names:
            result.append(item in row[2])
        
        return any(result)if len(result) != 0 else True

    return check

def create_area_filter(item_names):
    def check(row):
        result = []

        for item in item_names:
            result.append(item in row[3])
        
        return any(result)if len(result) != 0 else True

    return check

def create_holiday_filter(item_names):
    def check(row):
        result = []

        for item in item_names:
            result.append(item in row[4])
        
        return any(result)if len(result) != 0 else True

    return check

def create_welfare_filter(item_names):
    def check(row):
        result = []

        for item in item_names:
            result.append(item in row[5])
        
        return any(result)if len(result) != 0 else True

    return check

def create_background_filter(item_names):
    def check(row):
        result = []

        for item in item_names:
            result.append(item in row[6])
        
        return any(result)if len(result) != 0 else True

    return check

tki_industry = tkinter.Tk()
tki_industry.geometry('600x400')    #画面サイズの設定

tki_industry.title('就活-業種')     #画面タイトル
chk_industry = ['製造','サービス','メーカー','食品']    #チェックボックスで選択するアイテム

#業種
industry = {}           #(ウィジェット変数によって)業種のチェックボックスのON,OFFのデータが分かる
industry_checked = []   #チェックされた文字を入れるための空の配列

# チェックボタンを動的に作成して配置
for i in range(len(chk_industry)):
    industry[i] = tkinter.StringVar()   #industry[i]をウィジェット変数にする

    chk = tkinter.Checkbutton(          #チェックボックスの作成
        tki_industry,
        variable=industry[i],           #チェックボックスのON,OFFの状態が変化したときに値を設定する変数を指定
        onvalue=chk_industry[i],        #チェック状態がONに変化した時に、この値がvariableオプションで指定した変数にセットされる
        offvalue='',                    #チェック状態がOFFに変化した時に、この値がvariableオプションで指定した変数にセットされる
        text=chk_industry[i],           #chk_industry内にある文字をチェックボックスの項目名にする
    )

    chk.place(x=50, y=30 + (i * 24))    #チェックボックスの場所指定

# text = '' tkinter.Labelにより文字を表示する。実際に動かすには必要のない動作確認用プログラム
# textでは途中で表示する文字列を変更するには向いていないので、textvariableでindustry[]の状態を表示
# 状態とはonvalue,offvalueによってindustry[]にセットされたもの　例）industry[0]の場合、onvalue➡製造,offvalue➡''

#製造
value_Manufacturing = tkinter.Label(tki_industry, text='',textvariable=industry[0]) #industryの0番目の状態を表示する
#value_Manufacturing.place(x = 100,y = 50)
#サービス
value_service = tkinter.Label(tki_industry, text='',textvariable=industry[1])       #industryの1番目の状態を表示する
#メーカー
value_maker = tkinter.Label(tki_industry, text='',textvariable=industry[2])         #industryの2番目の状態を表示する
#食品
value_food = tkinter.Label(tki_industry, text='',textvariable=industry[3])          #industryの3番目の状態を表示する


def on_window_move(_):
    global industry_checked #global 変数名　によって関数の外で設定した変数を宣言する

    industry_checked = [
        value_Manufacturing.cget('text'),       #変数名.cget('text')により、ラベルの中にある文字列を取得
        value_service.cget('text'),             
        value_maker.cget('text'),
        value_food.cget('text'),                
    ]
    industry_checked = list(filter(None, industry_checked)) #industry_checkedにある空文字列を除外する

#職種
sales = {}
sales_checked = []

#地域
area = {}
area_checked = []

#休日
holiday = {}
holiday_checked = []

#福利厚生
welfare = {}
welfare_checked = []

#学歴
background = {}
background_checked = []

#業種→職種
def btn_click_Sales():
        print(industry_checked) #ページが切り替わる時にターミナル上で抽出された文字列を表示
        #最初の画面に戻る
        def return_view():
            tki_sales.destroy()

        tki_sales = tkinter.Tk()
        # 画面サイズ
        tki_sales.geometry('600x400')
        #画面タイトル
        tki_sales.title("就活-職種")
        # ラベル
        chk_Sales = ['営業','企画','エンジニア']

        # チェックボタンを動的に作成して配置
        for i in range(len(chk_Sales)):
            sales[i] = tkinter.StringVar()

            chk = tkinter.Checkbutton(
                tki_sales,
                variable=sales[i],
                onvalue=chk_Sales[i],
                offvalue='',
                text=chk_Sales[i],
            )

            chk.place(x=50, y=30 + (i * 24))

        
        # StringVar 中身の確認
        value_Sales = tkinter.Label(tki_sales, text='')
        value_Sales.config(textvariable=sales[0])

        value_plan = tkinter.Label(tki_sales, text='')
        value_plan.config(textvariable=sales[1])

        value_engineer = tkinter.Label(tki_sales, text='')
        value_engineer.config(textvariable=sales[2])
        
        def on_window_move(_):
            global sales_checked

            sales_checked = [
                value_Sales.cget('text'),
                value_plan.cget('text'),
                value_engineer.cget('text'),
            ]
            sales_checked = list(filter(None, sales_checked))

        # ボタン
        btn_next = tkinter.Button(tki_sales, text='次へ', command=btn_click_area)   #次へボタンの生成とボタンを押したときにcommandによって特定の関数(btn_click_area)を呼び出す
        btn_next.bind('<ButtonPress>', on_window_move)  #btn_nextに対してbind()メソッドでbtn_click_areaが実行中にon_window_moveが実行されるように紐づける
        btn_next.place(x = 150 ,y = 340)        #ボタンの位置決め
        
        btn_return = tkinter.Button(tki_sales, text='戻る', command=return_view)    #戻るボタンの生成とボタンを押したときにcommandによって特定の関数を呼び出す
        btn_return.place(x = 80 ,y = 340)
        tki_sales.mainloop()

#職種→地域
def btn_click_area():
    print(sales_checked)

    #前の画面に戻る
    def return_view():
        tki_area.destroy()

    tki_area = tkinter.Tk()
    # 画面サイズ
    tki_area.geometry('600x400')
    #画面タイトル
    tki_area.title("就活-地域")
    # ラベル
    chk_area = ['北海道','東北','関東','中部','近畿','四国','中国','九州・沖縄']

    # チェックボタンを動的に作成して配置
    for i in range(len(chk_area)):
        area[i] = tkinter.StringVar()

        chk = tkinter.Checkbutton(
            tki_area,
            variable=area[i],
            onvalue=chk_area[i],
            offvalue='',
            text=chk_area[i],
        )

        chk.place(x=50, y=30 + (i * 24))
    
    # StringVar 中身の確認
    #北海道
    value_Hokkaido = tkinter.Label(tki_area, text='')
    value_Hokkaido.config(textvariable=area[0])
    #東北
    value_Tohoku = tkinter.Label(tki_area, text='')
    value_Tohoku.config(textvariable=area[1])
    #関東
    value_Kanto = tkinter.Label(tki_area, text='')
    value_Kanto.config(textvariable=area[2])
    #中部
    value_Chubu = tkinter.Label(tki_area, text='')
    value_Chubu.config(textvariable=area[3])
    #近畿
    value_Kinki = tkinter.Label(tki_area, text='')
    value_Kinki.config(textvariable=area[4])
    #四国
    value_Shikoku = tkinter.Label(tki_area, text='')
    value_Shikoku.config(textvariable=area[5])
    #中国
    value_Chugoku = tkinter.Label(tki_area, text='')
    value_Chugoku.config(textvariable=area[6])
    #九州・沖縄
    value_Kyushu_Okinawa = tkinter.Label(tki_area, text='')
    value_Kyushu_Okinawa.config(textvariable=area[7])

    def on_window_move(_):
        global area_checked

        area_checked = [
            value_Hokkaido.cget('text'),
            value_Tohoku.cget('text'),
            value_Kanto.cget('text'),
            value_Chubu.cget('text'),
            value_Kinki.cget('text'),
            value_Shikoku.cget('text'),
            value_Chugoku.cget('text'),
            value_Kyushu_Okinawa.cget('text'),
        ]
        area_checked = list(filter(None, area_checked))
    
    # ボタン
    btn_next = tkinter.Button(tki_area, text = '次へ', command = btn_click_holiday)
    btn_next.bind('<ButtonPress>', on_window_move)
    btn_next.place(x = 150 ,y = 340)
    
    btn_return = tkinter.Button(tki_area, text='戻る', command=return_view)
    btn_return.place(x = 80 ,y = 340)
    tki_area.mainloop()

#地域→休日
def btn_click_holiday():
    print(area_checked)
    #前の画面に戻る
    def return_view():
        tki_holiday.destroy()

    tki_holiday = tkinter.Tk()
    # 画面サイズ
    tki_holiday.geometry('600x400')
    #画面タイトル
    tki_holiday.title("就活-休日")
    # ラベル
    chk_holiday = ['105日','120日','125日以上']
    
    # チェックボタンを動的に作成して配置
    for i in range(len(chk_holiday)):
        holiday[i] = tkinter.StringVar()

        chk = tkinter.Checkbutton(
            tki_holiday,
            variable=holiday[i],
            onvalue=chk_holiday[i],
            offvalue='',
            text=chk_holiday[i],
        )

        chk.place(x=50, y=30 + (i * 24))

    # StringVar 中身の確認
    #105日
    value_105niti = tkinter.Label(tki_holiday, text='')
    value_105niti.config(textvariable=holiday[0])
    #120日
    value_120niti = tkinter.Label(tki_holiday, text='')
    value_120niti.config(textvariable=holiday[1])
    #125日以上
    value_125nitiizyou = tkinter.Label(tki_holiday, text='')
    value_125nitiizyou.config(textvariable=holiday[2])

    def on_window_move(_):#コピペポイント
        global holiday_checked

        holiday_checked = [
            value_105niti.cget('text'),
            value_120niti.cget('text'),
            value_125nitiizyou.cget('text'),
        ]
        holiday_checked = list(filter(None, holiday_checked))

    # ボタン
    btn_next = tkinter.Button(tki_holiday, text = '次へ', command = btn_click_welfare)
    btn_next.bind('<ButtonPress>', on_window_move)
    btn_next.place(x = 150 ,y = 340)
    
    btn_return = tkinter.Button(tki_holiday, text='戻る', command=return_view)
    btn_return.place(x = 80 ,y = 340)
    tki_holiday.mainloop()

#休日→福利厚生
def btn_click_welfare():
    print(holiday_checked)

    #前の画面に戻る
    def return_view():
        tki_welfare.destroy()

    tki_welfare = tkinter.Tk()
    # 画面サイズ
    tki_welfare.geometry('600x400')
    #画面タイトル
    tki_welfare.title("就活-福利厚生")
    # ラベル
    chk_welfare = ['産休・育児休暇','社会保険完備','資格取得支援','社宅・家賃補助']
    
    # チェックボタンを動的に作成して配置
    for i in range(len(chk_welfare)):
        welfare[i] = tkinter.StringVar()

        chk = tkinter.Checkbutton(
            tki_welfare,
            variable=welfare[i],
            onvalue=chk_welfare[i],
            offvalue='',
            text=chk_welfare[i],
        )

        chk.place(x=50, y=30 + (i * 24))

    # StringVar 中身の確認
    #産休・育児休暇
    value_Childcare = tkinter.Label(tki_welfare, text='')
    value_Childcare.config(textvariable=welfare[0])
    #社会保険完備
    value_insurance = tkinter.Label(tki_welfare, text='')
    value_insurance.config(textvariable=welfare[1])
    #資格取得支援
    value_Qualification = tkinter.Label(tki_welfare, text='')
    value_Qualification.config(textvariable=welfare[2])
    #社宅・家賃補助
    value_rent = tkinter.Label(tki_welfare, text='')
    value_rent.config(textvariable=welfare[3])
    
    def on_window_move(_):#コピペポイント
        global welfare_checked

        welfare_checked = [
            value_Childcare.cget('text'),
            value_insurance.cget('text'),
            value_Qualification.cget('text'),
            value_rent.cget('text'),
        ]
        welfare_checked = list(filter(None, welfare_checked))

    # ボタン
    btn_next = tkinter.Button(tki_welfare, text = '次へ', command = btn_click_background)
    btn_next.bind('<ButtonPress>', on_window_move)
    btn_next.place(x = 150 ,y = 340)
    
    btn_return = tkinter.Button(tki_welfare, text='戻る', command=return_view)
    btn_return.place(x = 80 ,y = 340)
    tki_welfare.mainloop()

#勤務体制→学歴
def btn_click_background():
    print(welfare_checked)
    #前の画面に戻る
    def return_view():
        tki_background.destroy()

    tki_background = tkinter.Tk()
    # 画面サイズ
    tki_background.geometry('600x400')
    #画面タイトル
    tki_background.title("就活-学歴")
    # ラベル
    chk_background = ['大学院','大学','短大','専門','高専']
    
    # チェックボタンを動的に作成して配置
    for i in range(len(chk_background)):
        background[i] = tkinter.StringVar()

        chk = tkinter.Checkbutton(
            tki_background,
            variable=background[i],
            onvalue=chk_background[i],
            offvalue='',
            text=chk_background[i],
        )

        chk.place(x=50, y=30 + (i * 24))
    
    # StringVar 中身の確認
    #大学院
    value_grad_student = tkinter.Label(tki_background, text='')
    value_grad_student.config(textvariable=background[0])
    #大学
    value_University = tkinter.Label(tki_background, text='')
    value_University.config(textvariable=background[1])
    #短大
    value_Junior_college = tkinter.Label(tki_background, text='')
    value_Junior_college.config(textvariable=background[2])
    #専門
    value_Specialty = tkinter.Label(tki_background, text='')
    value_Specialty.config(textvariable=background[3])
    #高専
    value_Technical_college = tkinter.Label(tki_background, text='')
    value_Technical_college.config(textvariable=background[4])

    def on_window_move(_):
        global background_checked

        background_checked = [
            value_grad_student.cget('text'),
            value_University.cget('text'),
            value_Junior_college.cget('text'),
            value_Specialty.cget('text'),
            value_Technical_college.cget('text'),
        ]
        background_checked = list(filter(None, background_checked))
    
    def search():
        global rows

        filterrows0 = filter(create_industry_filter(industry_checked),rows) #処理の結果Tureと判断される要素(企業情報)を抽出、表示する
        filterrows1 = filter(create_sales_filter(sales_checked),filterrows0)
        filterrows2 = filter(create_area_filter(area_checked) ,filterrows1)
        filterrows3 = filter(create_holiday_filter(holiday_checked), filterrows2)
        filterrows4 = filter(create_welfare_filter(welfare_checked), filterrows3)
        filterrows5 = filter(create_background_filter(background_checked), filterrows4)

        print(list(filterrows5))

    # ボタン
    btn_next = tkinter.Button(tki_background, text = '検索', command=search) #commandによって関数searchの呼び出し
    btn_next.bind('<ButtonPress>', on_window_move)
    btn_next.place(x = 150 ,y = 340)
    
    btn_return = tkinter.Button(tki_background, text='戻る', command=return_view)
    btn_return.place(x = 80 ,y = 340)
    tki_background.mainloop()    

# chk_industryのボタン作成 
btn_next = tkinter.Button(tki_industry, text = '次へ', command=btn_click_Sales)
btn_next.bind('<ButtonPress>', on_window_move)
btn_next.place(x = 150 ,y = 340)

# csv読み込み
rows = []   #空のリストを用意

with open('csv_file/企業情報 - シート1.csv', 'r',encoding='utf-8') as csv_file:     #open()で指定したファイルを開く。日本語を使用しているのでencoding='utf-8'がある
    csv_reader = reader(csv_file)   #open()で開いたファイルを指定
    
    for row in csv_reader:  #指定したデータをfor文で行ごとのデータを取得できる
        rows.append(row)    #リストrowsにrowを追加。    

rows = rows[1:] #0行目は今回つかわないので0行目を削る

input()
