#!/usr/bin/env python
import os

root_path = os.getcwd()

folders = [
    '1RdReportBl',
    '1RdReportRpr',
    '1RdReportRvr',
    '1RdReportTm',
    'ArrivalNotification',
    'IncomeAdmReport',
    'LmDailyReport',
    'LmHcReport',
    'LmPatentStatsReport',
    'LmSeaReport',
    'LmWpHsStatsReport',
    'Rp1blReport',
    'Rp1prAvtReport',
    'Rp1prReport',
    'RpIpjReport',
    'RpLpjReport',
    'RpTijReport',
    'RpZpReport',
    'adb',
    'application',
    'asRussianPassport',
    'asao',
    'aspassport',
    'aspassport1p',
    'case',
    'casun',
    'cbduig',
    'chargeReport',
    'edaps',
    'egrn',
    'fsb',
    'fssp',
    'giac',
    'hotel',
    'interchange',
    'izberkom',
    'labormigration',
    'parus',
    'riurReport',
    'rosstat',
    'statistics'
]

for folder in folders:
    os.mkdir(os.path.join(root_path, folder))
