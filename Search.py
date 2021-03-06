from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os

# 검색 키워드, 검색 기간
keyword = 'Galaxy s20'
period = 'today 3-m'    # 검색기간 최근 3개월


# 구글 트렌드 접속
trend_obj = TrendReq()
trend_obj.build_payload(kw_list=[keyword],timeframe=period)

# 시간에 따른 트렌드 변화
trend_df = trend_obj.interest_over_time()
print(trend_df.head())

# 그래프 출력
plt.style.use('ggplot')
plt.figure(figsize=(14,5))
trend_df['Galaxy s20'].plot()
plt.title('Google Trends over time', size = 15)
plt.legend(labels=['Galaxy s20'],loc='upper right')

# 그래프 파일 저장
cwd = os.getcwd()
print(cwd)
output_filepath = os.path.join(cwd,'output','google_trend_%s.png' %keyword)
print(output_filepath)
plt.savefig(output_filepath,dpi=300)
plt.show()
