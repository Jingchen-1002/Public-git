# 随笔：
### 主要框架结构：
        利用数据库 存储 -》 case以及config
        每一条数据即是一条testcase
        主要是如何将每一条testcase--》运行出来--》并send report
        围绕这个进行框架设计：
                设计一个通用的类，即是--》requests_util  ：
                            主要功能就是进行：requests应用，进行一些请求方法以及url的封装
                再者，开始真正的设计：
                    设计一个 ApiTestCase类：
                            主要功能便是进行用例的读取、加载、运行、以及对结果的报告发送
                        类中需要设计方法，从而实现以上的功能：
                            1. 读取加载所有的测试用例方法--》loadAllCaseByApp
                                    主要功能是读取所有的测试用例--依据app查找 类似于某一个业务
                                      简单来说就是对数据库的”查“的操作，依据 app 查出来所有的语句
                                        单独查询，读取每一个
                            2. 利用id读取所有测试用例--》findCaseById
                                既然已经加载出来了所有的测试用例，接下来对每一条用例的查找，当然这个是利用
                                id去查找出来，就是对数据库的”查“操作，通过id的查出来
                            3. 加载配置--》loadConfigByAppAndKey
                                这就是读取配置项，所谓的配置项，也就是  url 以及 sendEmail 的信息
                                无非就是对数据库的操作，通过 app 查出来 字典的key、value值，但是这个查询就是
                                单独查询，读取每一个。
                            4. 通过id进行更新响应内容以及测试内容--》updateResultByCaseId
                                这就是对数据库响应内容的更新。中规中矩的  修改数据库信息，通过断言内容
                                    is_pass = True or False, 从而判断是否修改哪一个sql语句
                            5. 开始运行测试用例  -- 》  all（所有）
                                 所有测试用例的运行   --》 获取域名  --》 读取所有测试用例 --》
                                