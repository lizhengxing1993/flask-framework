# coding=utf-8
import math

from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
# 配置中文字体
plt.rcParams['font.sans-serif']=['SimHei']

y_1 = [0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
y_2 = [0,0,0,0,0,0,0,0,0,0,0,8,0,0,0,0,0,0,0,0,0,0,0,0]
y_3 = [i*1000 for i in [14,51,71,25,33,82,17,73,12,44,32,11,15,12,2,3,4,6,7,86,6,5,45,7]]

list_all = y_1 + y_2 + y_3
end_num = 101
if max(list_all) / 1000 > end_num:
    end_num = math.ceil(max(list_all) / 1000 / 25) * 25 + 1
x = range(0,24)
y = [i * 1000 for i in range(0, end_num, 25)]
# 设置图形大小
plt.figure(figsize=(20,8),dpi=80)
# 设置标题
plt.title('数据全流程监控',loc='left',fontsize=20, fontweight='bold')


plt.plot(x,y_1,label="数据接入速率",color="green", marker='o')
plt.plot(x,y_2,label="数据处理速率",color="blue", marker='o')
plt.plot(x,y_3,label="ES入库速率",color="purple", marker='o')

#设置x轴刻度
_xtick_labels = ["{}".format(i) for i in x]
_ytick_labels = ["{}k".format(math.ceil(i/1000)) for i in y]
plt.xticks(x,_xtick_labels)
plt.yticks(y,_ytick_labels)

#绘制网格
plt.grid(alpha=0.7,linestyle=':')

#添加图例
plt.legend(loc="upper left")

#保存
plt.savefig("./t1.jpg")
#展示
plt.show()

class MappingImage(object):

    # 数据全流程监控折线图
    @classmethod
    def the_whole_process_of_data(cls,file_name, Access_list, handle_list, ES_Warehousing_list,
                                  figsize=(20,8), dpi=80, title_size=20):
        """

        :param file_name: 文件名 str
        :param Access_list: 数据接入速率 list
        :param handle_list: 数据处理速率 list
        :param ES_Warehousing_list:  ES入库速率 list
        :param figsize: 绘图尺寸 非必填
        :param dpi: 像素 非必填
        :param title_size: 标题字体大小 非必填
        :return:
        """
        y_1 = Access_list
        y_2 = handle_list
        y_3 = ES_Warehousing_list

        list_all = y_1 + y_2 + y_3
        end_num = 101
        if max(list_all) / 1000 > end_num:
            end_num = math.ceil(max(list_all) / 1000 + 1)

        x = range(0, 24)
        y = [i * 1000 for i in range(0, end_num, 25)]
        # 设置图形大小
        plt.figure(figsize=figsize, dpi=dpi)
        # 设置标题
        plt.title('数据全流程监控(EPS)', loc='left', fontsize=title_size, fontweight='bold')

        # 画图
        plt.plot(x, y_1, label="数据接入速率", color="green", marker='o')
        plt.plot(x, y_2, label="数据处理速率", color="blue", marker='o')
        plt.plot(x, y_3, label="ES入库速率", color="purple", marker='o')

        # 设置x轴刻度
        _xtick_labels = ["{}".format(i) for i in x]
        _ytick_labels = ["{}k".format(math.ceil(i / 1000)) for i in y]
        plt.xticks(x, _xtick_labels)
        plt.yticks(y, _ytick_labels)

        """
        import matplotlib.ticker as mticker  
        x = [i * 2872155 for i in range(1, 11)]
        y = [0.219, 0.402,  0.543,  0.646,0.765,  0.880,1.169, 1.358,1.492,1.611]
        
        plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%.1f s'))
        plt.plot(x, y)
        
        """
        # 绘制网格
        plt.grid(alpha=0.7, linestyle=':')

        # 添加图例
        plt.legend(loc="upper left")

        # 保存
        plt.savefig('images/'+file_name)
        # 展示
        plt.show()

    # 数据全流程监控折线图
    @classmethod
    def data_monitor(cls,file_name, loophole_list, patch_list, host_loophole_list,
                        essats_list, model_list,
                                  figsize=(20,8), dpi=80, title_size=20):
        y_1 = loophole_list
        y_2 = patch_list
        y_3 = host_loophole_list
        y_4 = essats_list
        y_5 = model_list

        list_all = y_1 + y_2 + y_3 + y_4 + y_5
        end_num = 101
        if max(list_all) / 1000 > end_num:
            end_num = math.ceil(max(list_all) / 1000 / 25) * 25 + 1

        x = range(0, 24)
        y = [i * 1000 for i in range(0, end_num, 25)]
        # 设置图形大小
        plt.figure(figsize=figsize, dpi=dpi)
        # 设置标题
        plt.title('数据源监控(EPS)', loc='left', fontsize=title_size, fontweight='bold')

        plt.plot(x, y_1, label="漏洞运维服务", color="blue", marker='o')
        plt.plot(x, y_2, label="补丁数据资源子系统", color="green", marker='o')
        plt.plot(x, y_3, label="主机漏洞辅助验证与研判系统", color="red", marker='o')
        plt.plot(x, y_4, label="资产子系统", color="yellow", marker='o')
        plt.plot(x, y_5, label="恶意样本数据资源子系统", color="purple", marker='o')

        # 设置x轴刻度
        _xtick_labels = ["{}".format(i) for i in x]
        _ytick_labels = ["{}k".format(math.ceil(i / 1000)) for i in y]
        plt.xticks(x, _xtick_labels)
        plt.yticks(y, _ytick_labels)

        # 绘制网格
        plt.grid(alpha=0.7, linestyle=':')

        # 添加图例
        plt.legend(loc="upper left")

        # 保存
        plt.savefig('images/'+file_name)
        # 展示
        plt.show()


    # 数据流量趋势
    @classmethod
    def trend_of_data_volume(cls,file_name, loophole_list, patch_list, host_loophole_list,
                        essats_list, model_list,
                                  figsize=(20,8), dpi=80, title_size=20):
        y_1 = loophole_list
        y_2 = patch_list
        y_3 = host_loophole_list
        y_4 = essats_list
        y_5 = model_list

        x = range(0, 24)
        y = range(0, 101, 25)
        # 设置图形大小
        plt.figure(figsize=figsize, dpi=dpi)
        # 设置标题
        plt.title('数据源监控(EPS)', loc='left', fontsize=title_size, fontweight='bold')

        plt.plot(x, y_1, label="漏洞运维服务", color="blue", marker='o')
        plt.plot(x, y_2, label="补丁数据资源子系统", color="green", marker='o')
        plt.plot(x, y_3, label="主机漏洞辅助验证与研判系统", color="red", marker='o')
        plt.plot(x, y_4, label="资产子系统", color="yellow", marker='o')
        plt.plot(x, y_5, label="恶意样本数据资源子系统", color="purple", marker='o')

        # 设置x轴刻度
        _xtick_labels = ["{}点".format(i) for i in x]
        _ytick_labels = ["{}k".format(i) for i in y]
        plt.xticks(x, _xtick_labels)
        plt.yticks(y, _ytick_labels)

        # 绘制网格
        plt.grid(alpha=0.7, linestyle=':')

        # 添加图例
        plt.legend(loc="upper left")

        # 保存
        plt.savefig('images/'+file_name)
        # 展示
        plt.show()

MappingImage.the_whole_process_of_data('test3', y_1, y_2, y_3)
y_4 = [i*1000 for i in [0,29,0,0,9,0,0,0,0,0,0,8,70,0,0,0,0,40,0,0,0,0,22,0]]
y_5 = [i*1000 for i in [0,5,0,0,66,0,0,23,0,0,0,8,0,8,0,0,0,0,30,0,4,62,0,0] ]
MappingImage.data_monitor('test2', y_1, y_2, y_3, y_4, y_5)


