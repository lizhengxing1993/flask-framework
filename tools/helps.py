# 将model的结果转为字典格式 filters是要过滤掉不返回的字段
def model_to_dict(result, filters=None):
    from collections import Iterable
    # 转换完成后，删除  '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result if res]
            for t in tmp:
                t.pop('_sa_instance_state')
                if filters:
                    [t.pop(key) for key in filters]
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
            if filters:
                for key in filters:
                    tmp.pop(key)
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')
