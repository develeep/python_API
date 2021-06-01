from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 keyword, 검색 기간 입력
keyword = 'izone'
period = 'now 7-d'

# 구글 트렌드 접속
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword],timeframe=period)

print(trend_obj)
# 지역별 검색 트렌드 비
trend_df = trend_obj.interest_by_region().sort_values(by= 'izone', ascending=False)
print(trend_df.head)

# 그래프 출력
plt.style.use('ggplot')
plt.figure(figsize=(14,10))
trend_df.plot(kind='bar')            
plt.title('Google trends by Region',Size=15)
plt.legend(labels=[keyword],loc='upper right')

# 그래프 파일 저장
cwd = os.getcwd()
output_filepath = os.path.join(cwd,'output','google_trend_by_region_%s.png'%keyword)
plt.savefig(output_filepath,dpi=300)
plt.show()