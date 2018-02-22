# -*- coding: utf-8 -*-

"""
    作者:     凌剑
    版本:     1.0
    日期:     2018/01
    项目名称：Udacity机器学习（入门）P2项目-创建电影网站

    在项目提供的模板文件基础上修改完成。

"""

import media
import fresh_tomatoes
import xlrd


def main():
    """
        主函数
    """
    # 打开影片信息文件(为使用方便，影片信息存放在 movies.xlsx文件中)
    workbook = xlrd.open_workbook(r'movies.xlsx')

    # 根据sheet索引获取第一个sheet内容(影片信息放在第一个sheet)
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始

    # 定义一个空影片列表，用于存放从文件提取的影片信息
    movies = []

    # 提取影片信息，实例化Movie类，并添加到movies列表中
    for i in range(1, sheet1.nrows):  # 按行循环，movies.xlsx文件中第一行是标题行，所以从第二行开始
        movie = media.Movie(sheet1.row(i)[0].value,  # 影片名称
                            sheet1.row(i)[1].value,  # 影片简介
                            sheet1.row(i)[2].value,  # 影片海报地址
                            sheet1.row(i)[3].value,  # 影片预告片地址
                            sheet1.row(i)[4].value,  # 影片导演
                            sheet1.row(i)[5].value,  # 影片主演
                            sheet1.row(i)[6].value  # 影片上映时间
                            )  # 实例化Movie类
        movies.append(movie)  # 添加到movies列表中

    # 把含有实例化 Movie类的 movies列表传递给函数，生成网页，并用浏览器打开
    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
