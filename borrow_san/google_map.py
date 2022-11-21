# google maps 좌표 찍기
import pandas as pd
import folium


def maker():
    tiles = 'http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}'
    attr = 'Google'
    kor_map = folium.Map(location=[37.570333, 126.984829], zoom_start=100, tiles=tiles, attr=attr)
    df_cities = pd.DataFrame(
        {'위도': [37.570333, 37.570446], '경도': [126.984829, 126.985237]},
        index=['종각역 8번 출구', '종각 YMCA 1층'])

    for i in range(len(df_cities)):
        folium.Marker([df_cities.iloc[i][0], df_cities.iloc[i][1]], popup=df_cities.index[i]).add_to(kor_map)

    kor_map.save('./save/umb_maker.html')
    print('저장 완료')


if __name__ == '__main__':
    maker()