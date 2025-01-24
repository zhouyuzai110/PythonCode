import json

import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
}

BASEURL = 'https://www.jisilu.cn/data/etf/etf_list/'
excel_file = '集思录ETF基金.xlsx'


def get_origin():
    """
    获取基金数据并整理成数据框
    """
    # 发起HTTP请求，返回类型为requests.models.Response
    r: requests.models.Response = requests.get(BASEURL, headers=headers)
    # 解析HTML响应，返回BeautifulSoup对象
    soup: BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    # 提取基金数据并转换为列表
    etf_fund: List[Dict[str, Any]] = [x['cell'] for x in json.loads(str(soup))['rows']]
    # 将列表数据展开为列，并转化为pandas.DataFrame对象
    etf_fund_dataframe: pd.DataFrame = pd.json_normalize(etf_fund)
    # 选择需要的列并复制，得到一个新的DataFrame
    etf_fund_dataframe_cut: pd.DataFrame = etf_fund_dataframe[[
        'fund_id', 'fund_nm', 'price', 'volume', 'index_nm', 'unit_total', 'issuer_nm'
    ]].copy()
    # 将价格和基金规模列转换为数值类型
    etf_fund_dataframe_cut[["price", "unit_total"]] = etf_fund_dataframe_cut[["price", "unit_total"]].apply(pd.to_numeric)

    # 读取中国指数列表Excel文件，返回一个pandas.DataFrame对象
    china_index_list: pd.DataFrame = pd.read_excel('中国指数列表.xlsx', sheet_name='Sheet1', header=0)[['指数代码', '指数代码_clean', '指数简称']]

    # 按照指数名称分组并计算基金规模总和，返回一个pandas.DataFrame对象
    index_sum: pd.DataFrame = etf_fund_dataframe_cut.groupby(['index_nm']).agg({'unit_total': 'sum'})

    # 按照指数名称分组并计算基金个数，返回一个pandas.DataFrame对象
    index_count: pd.DataFrame = pd.DataFrame(etf_fund_dataframe.groupby('index_nm')['fund_id'].count())

    # 合并基金个数和基金规模数据，并按照基金规模降序排列，返回一个排序后的pandas.DataFrame对象
    df_result: pd.DataFrame = pd.merge(
        index_count, index_sum, on='index_nm').sort_values(
            'unit_total', ascending=False).reset_index()

    # 将中国指数列表与df_result合并，返回一个合并后的pandas.DataFrame对象
    df_result_china_index_list: pd.DataFrame = pd.merge(
        df_result, china_index_list, how='left', left_on='index_nm', right_on='指数简称').iloc[:, :-1]

    # 设置列名
    df_result_china_index_list.columns = ['跟踪指数', '基金个数', '基金规模', '指数代码', '指数代码缩写']

    # 将指数代码和指数代码缩写列转换为字符串类型
    df_result_china_index_list[['指数代码', '指数代码缩写']] = df_result_china_index_list[['指数代码', '指数代码缩写']].astype(str)

    # 创建Excel写入器
    with pd.ExcelWriter(excel_file) as result_excel:
        # 将原始基金列表按照基金规模降序排列并写入Excel
        etf_fund_dataframe_cut.sort_values(
            'unit_total', ascending=False, ignore_index=True).to_excel(
                excel_writer=result_excel, sheet_name='工作基金列表')

        # 将基金规模数据写入Excel
        df_result_china_index_list.to_excel(excel_writer=result_excel, sheet_name='基金规模')


def main():
    get_origin()


if __name__ == '__main__':
    main()
