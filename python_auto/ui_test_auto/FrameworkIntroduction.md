# ui_test_auto介绍
## GitHub项目地址：
## 框架介绍：
      本人基于python + selenium + unittest + PO + ddt + HTMLTestRunner进行框架搭建。
## 框架整体结构：

- ui_test_auto
    - base_page:项目的基础文件
        - base_page.py: 基类封装，主要是对关键字的封装
    - common： 项目公共文件
        - readconfig.py: 读取配置文件
    - config：配置文件
        - chrome_option.py:针对于谷歌浏览器进行option配置
        - config.py: 路径的配置文件
        - url_path.ini: 提取公共的url部分
    - data：yaml文件，主要是一些针对于ddt数据驱动时所需的文件
    - page_object:主要是对于po模式下，对于各个页面进行封装
    - report:各种报告
        - html：存放基于HTMLTestRunner生成的html报告
        - img：针对于error截图存放的路径
        - log： 存放执行日志
    - test_case: 测试用例，基于unittest框架
    - util: 工具
    - run： 执行
        - run_all:执行所有的测试用例
    

