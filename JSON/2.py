import os
import stat

filepath = 'D:\Тест прогсы\py.test1\py.test1-1\JSON\population_data.json'

mode = os.stat(filepath).st_mode