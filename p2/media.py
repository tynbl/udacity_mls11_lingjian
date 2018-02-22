# -*- coding: utf-8 -*-

"""
    作者:     凌剑
    版本:     1.0
    日期:     2018/01
    项目名称：Udacity机器学习（入门）P2项目-创建电影网站

    在项目提供的模板文件基础上修改完成。

"""

import webbrowser


class Movie():
    # 此类的功能是存储影片的相关信息

    def __init__(self,
                 movie_title, movie_storyline, movie_poster_image,
                 movie_trailer, movie_director, movie_starring,
                 movie_release_date
                 ):
        # 初始化Movie类的实例
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_url = movie_trailer
        self.director = movie_director
        self.starring = movie_starring
        self.release_date = movie_release_date

    def show_trailer(self):
        # 用浏览器打开影片预告片地址
        webbrowser.open(self.trailer_url)
