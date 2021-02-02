# -*- coding: utf-8 -*-
import numpy as np
import talib

'''
策略名称: KDJ指标策略
关键词: 随机指标、中短期
方法:
1. 通过特定周期内的最高价、最低价、收盘价以及移动平均线法计算KDJ值.
2. 用KDJ判断超买/超卖线, 超买则卖出, 超卖则买入.
'''
