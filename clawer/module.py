# 三井住友カードの明細とポイントをmoneytree経由で取得
import os
import requests
import pandas as pd
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# n月1日のときだけ実行
now_month = datetime.date.today().month
now_day = datetime.date.today().day
# now_day = 1

# select_month = 2
# select_month = page_date_month
select_month = now_month-1
if select_month == 0:
    select_month = 12


def execute_login(driver, MSC_USERNAME: str, MSC_PASSWORD: str) -> None:
    """
    ログインする
    """
    login_form_container = driver.find_element(by=By.CLASS_NAME, value="login-form-container")
    # メールアドレスを入力する場所を指定
    logint_form_first_input = login_form_container.find_element(by=By.CSS_SELECTOR, value=".text-input.login-form-input.login-form-input-first")
    username_input_space = logint_form_first_input.find_element(by=By.CSS_SELECTOR, value=".text-input-element.text-input-element-input")
    # 入力
    username_input_space.send_keys(MSC_USERNAME)
    # パスワードを入力する場所を指定
    username_input_space.send_keys(Keys.TAB)
    password_input_space = driver.switch_to.active_element
    # 入力
    password_input_space.send_keys(MSC_PASSWORD)
    # ログイン
    login_button = login_form_container.find_element(by=By.CSS_SELECTOR, value=".button.text-button.big.login-form-button.primary")
    login_button.click()


def click_tab_account_balance(driver) -> None:
    """
    口座残高タブを選択
    """
    # 口座残高タブを指定
    driver.refresh  # seleniumにログイン後のページを読み込ませるために再読み込み
    app = driver.find_element(by=By.ID, value="app")
    mt_webapp = app.find_element(by=By.ID, value="mt-webapp")
    ng_scope_ng_isolate_scope = mt_webapp.find_element(by=By.CSS_SELECTOR, value=".ng-scope.ng-isolate-scope")
    ng_isolate_scope = ng_scope_ng_isolate_scope.find_element(by=By.CLASS_NAME, value="ng-isolate-scope")
    right_text_center = ng_isolate_scope.find_element(by=By.CSS_SELECTOR, value=".col-xs-4.self-no-gutter-left.self-no-gutter-right.text-center")
    navigation_items = right_text_center.find_element(by=By.CLASS_NAME, value="navigation-items")
    list_unstyled_list_inline = navigation_items.find_element(by=By.CSS_SELECTOR, value=".list-unstyled.list-inline")
    ng_scope_classes = list_unstyled_list_inline.find_elements(by=By.CLASS_NAME, value="ng-scope")
    secondary_ng_scope = ng_scope_classes[1]

    # 口座残高をクリック
    secondary_ng_scope.click()


def click_calendar_element_at_selectd_month(driver) -> None:
    # ページがどの年のどの月か確認する
    driver.refresh  # seleniumにログイン後のページを読み込ませるために再読み込み

    page_date = driver.find_element(By.XPATH, value="/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-personal/div/mt-link-vault/div/mt-two-column-layout/div/div[2]/mt-awesome-layout/div/div/div[1]/awesome-body/div/right-column-body/div[2]/div[6]/div[1]/div/div[1]/date-navigation/div/div[2]/div[1]")
    # page_date_text = page_date.text
    # page_data_split_output = page_date_text.split("年")
    # page_date_year = page_data_split_output[0] + "年"
    # page_date_month = page_data_split_output[1]

    page_date.click()
    x_path_base = "/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-personal/div/mt-link-vault/div/mt-two-column-layout/div/div[2]/mt-awesome-layout/div/div/div[1]/awesome-body/div/right-column-body/div[2]/div[6]/div[1]/div/div[1]/date-navigation/div/div[2]/div[2]/ul/li/div/div/div/table/tbody/"
    select_of_January = driver.find_element(by=By.XPATH, value=x_path_base+"tr[1]/td[1]/button/span")
    select_of_February = driver.find_element(by=By.XPATH, value=x_path_base+"tr[1]/td[2]/button")
    select_of_March = driver.find_element(by=By.XPATH, value=x_path_base+"tr[1]/td[3]/button")
    select_of_April = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[2]/td[1]/button")
    select_of_May = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[2]/td[2]/button")
    select_of_June = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[2]/td[3]/button")
    select_of_July = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[3]/td[1]/button")
    select_of_August = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[3]/td[2]/button")
    select_of_September = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[3]/td[3]/button")
    select_of_October = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[4]/td[1]/button")
    select_of_November = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[4]/td[2]/button")
    select_of_December = driver.find_element(by=By.XPATH, value=x_path_base+"/tr[4]/td[3]/button")

    if select_month == 1:
        page_date.click()
        select_of_January.click()
        driver.refresh

    elif select_month == 2:
        page_date.click()
        select_of_February.click()
        driver.refresh

    elif select_month == 3:
        page_date.click()
        select_of_March.click()
        driver.refresh

    elif select_month == 4:
        page_date.click()
        select_of_April.click()
        driver.refresh

    elif select_month == 5:
        page_date.click()
        select_of_May.click()
        driver.refresh

    elif select_month == 6:
        page_date.click()
        select_of_June.click()
        driver.refresh

    elif select_month == 7:
        page_date.click()
        select_of_July.click()
        driver.refresh

    elif select_month == 8:
        page_date.click()
        select_of_August.click()
        driver.refresh

    elif select_month == 9:
        page_date.click()
        select_of_September.click()
        driver.refresh

    elif select_month == 10:
        page_date.click()
        select_of_October.click()
        driver.refresh

    elif select_month == 11:
        page_date.click()
        select_of_November.click()
        driver.refresh

    elif select_month == 12:
        page_date.click()
        select_of_December.click()
        driver.refresh


def get_point_value(driver) -> str:
    point_page = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/div[1]/ul/li[2]")
    point_page.click()
    driver.refresh
    point_value: str = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-points/div/mt-link-vault/div/mt-two-column-layout/div/div[1]/div[2]/left-column-body/mt-credentials/div/ul/li/mt-credential/div/mt-credential-template/div/div[3]/div[2]/mt-list-secondary/div/ul/li/div/item-content/mt-account/div/span[2]").text

    return point_value


def get_value_clawer(driver, select_month, MSC_USERNAME, MSC_PASSWORD) -> str:
    execute_login(driver, MSC_USERNAME, MSC_PASSWORD)
    click_tab_account_balance(driver)
    click_calendar_element_at_selectd_month(driver)

    data_list = []
    counter = 0
    is_error = False
    while is_error is False:
        counter += 1
        if counter == 0:
            print("0番目")
        try:
            table_date_value = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-personal/div/mt-link-vault/div/mt-two-column-layout/div/div[2]/mt-awesome-layout/div/div/div[1]/awesome-body/div/right-column-body/div[2]/div[6]/div[2]/mt-transactions/div[2]/div/div/div[2]/div[{counter}]/div[1]/mt-transaction/div/div[1]/div[1]").text
        except NoSuchElementException:
            print(f"{counter}番目 要素なし")
            is_error = True
        try:
            table_content_value = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-personal/div/mt-link-vault/div/mt-two-column-layout/div/div[2]/mt-awesome-layout/div/div/div[1]/awesome-body/div/right-column-body/div[2]/div[6]/div[2]/mt-transactions/div[2]/div/div/div[2]/div[{counter}]/div[1]/mt-transaction/div/div[1]/div[2]").text
        except NoSuchElementException:
            pass
        try:
            table_price_value = driver.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[1]/div/div/section/mt-webapp-layout/div/div[2]/mt-accounts/div/mt-accounts-personal/div/mt-link-vault/div/mt-two-column-layout/div/div[2]/mt-awesome-layout/div/div/div[1]/awesome-body/div/right-column-body/div[2]/div[6]/div[2]/mt-transactions/div[2]/div/div/div[2]/div[{counter}]/div[1]/mt-transaction/div/div[1]/div[5]").text
        except NoSuchElementException:
            pass

        table_title_date_select_month_included = str(select_month)+"/"+str(table_date_value)
        removed_table_price_value = table_price_value.replace("¥", "")
        price_value_for_calculate = removed_table_price_value.replace(",", "")

        data_dcit = {
            "日付": table_title_date_select_month_included,
            "内容": table_content_value,
            "金額": removed_table_price_value,
            "id": counter,
            "calc_price": price_value_for_calculate
        }
        data_dcit.append(data_list)
        print(f"{counter} 番目")

    # ポイント情報取得
    point_value = get_point_value(driver)

    df = pd.DataFrame(data_list)
    descending_order_sorted_df = df.sort_values("id", ascending=False)
    descending_order_sorted_df.to_csv("./msc_ax1.csv", encoding="utf_8_sig")

    driver.quit()
    return point_value


def selenium_driver_settings():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from webdriver_manager.chrome import ChromeDriverManager

    options = Options()
    options.add_argument('--incognito')
    options.headless = True  # ブラウザ非表示で実行
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver


def connect_string(*args):
    connected_send_datas = '\n'.join(args)
    return connected_send_datas


def send_line_notify_message(notification_message):
    """
    LINEにメッセージを送る
    """
    # herokuに設定した環境変数"LINE_NOTIFY_TOKEN"からアクセストークンを持ってくる 今回は確認用BOT
    LINE_TOKEN = os.getenv("LINE_NOTIFY_TOKEN_HISTORY_CHECK_BOT")
    line_notify_api = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": f"{notification_message}"}
    requests.post(line_notify_api, headers=headers, data=data)


def send_gmail(subject, bodyText, sendAddress='xingsantianzhong460@gmail.com', password='nlhuuwhwcygwyaro', fromAddress='xingsantianzhong460@gmail.com', toAddress='xingsantianzhong460@gmail.com'):
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formatdate

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()
