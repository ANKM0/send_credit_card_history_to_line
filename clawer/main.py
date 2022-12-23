import os
import pandas as pd
import datetime


from module import send_gmail, get_value_clawer, selenium_driver_settings, connect_string, send_line_notify_message


# n月1日のときだけ実行
now_month = datetime.date.today().month
now_day = datetime.date.today().day
# now_day = 1

# select_month = 2
# select_month = page_date_month
select_month = now_month-1
if select_month == 0:
    select_month = 12


def execute_task(driver, select_month, MSC_USERNAME, MSC_PASSWORD):
    point_value = get_value_clawer(driver, select_month, MSC_USERNAME, MSC_PASSWORD)

    file_path = ("./msc_ax1.csv")
    print("file name:" + file_path)
    descending_order_sorted_df = pd.read_csv(file_path)

    sum_price_value = descending_order_sorted_df["calc_price"].sum()
    print(sum_price_value)

    sum_price_value = descending_order_sorted_df["calc_price"].sum()
    added_sum_price_value = f"合計{sum_price_value}円"

    send_datas = []
    descending_order_sorted_df_length = len(descending_order_sorted_df)
    print(descending_order_sorted_df_length)
    for i in range(1, descending_order_sorted_df_length):
        descending_order_sorted_df_row = descending_order_sorted_df.iloc[i]

        send_data_date = descending_order_sorted_df_row["日付"].replace("月", "")
        send_data_content = descending_order_sorted_df_row["内容"]
        send_data_price = descending_order_sorted_df_row["金額"]

        raw_send_message_content = f"\n\n{send_data_date}\n{send_data_content}\n{send_data_price}"

        send_datas.append(raw_send_message_content)

    send_datas.append(f"\n{added_sum_price_value}\nポイント  {point_value}P")

    connected_send_datas = connect_string(*send_datas)
    print(connected_send_datas)

    send_line_notify_message(connected_send_datas)


def main():
    driver = selenium_driver_settings()
    # 最大の読み込み時間を設定
    driver.implicitly_wait(5)
    driver.set_window_size(1200, 1000)

    login_url = "https://app.getmoneytree.com/app/trends/net-worth"
    driver.get(login_url)

    MSC_USERNAME = os.environ['MSC_USERNAME']
    MSC_PASSWORD = os.environ['MSC_PASSWORD']

    # n月1日のときだけ実行
    now_month = datetime.date.today().month
    now_day = datetime.date.today().day
    # now_day = 1

    # select_month = 2
    # select_month = page_date_month
    select_month = now_month-1
    if select_month == 0:
        select_month = 12

    if now_day != 1:
        print(f"now_day{now_day}")
        print(f"select_month{select_month}")
        print("例外_now_day=1ではない")
    elif now_day == 15 or now_day == 30:
        send_gmail(subject="三井住友カードチェックBOT 定期検査", bodyText=f"{now_month}/{now_day}:三井住友カードチェックBOTは正常に動作中です")
    elif now_day == 1:
        print(f"now_day:{now_day}")
        print(f"select_month:{select_month}")
        send_gmail(subject="三井住友カードチェックBOT 定期実行", bodyText=f"{now_month}/{now_day}:三井住友カードチェックBOTは正常に動作中です")
        execute_task(driver, select_month, MSC_USERNAME, MSC_PASSWORD)
