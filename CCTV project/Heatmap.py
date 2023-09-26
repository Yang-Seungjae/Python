import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import gaussian_filter
import cx_Oracle

# Oracle 데이터베이스에 연결하기 위한 정보
dsn = cx_Oracle.makedsn(host='localhost', port=1521, service_name='xe')
user = 'hr'
password = 'hr'

# 데이터베이스 연결
connection = cx_Oracle.connect(user=user, password=password, dsn=dsn)

# 커서 생성
cursor = connection.cursor()

# SQL 쿼리 실행하여 컬럼 값 가져오기

count_date = input("날짜를 입력해주세요(yy/mm/dd hh:mm): ")
sql = "SELECT section1, section2 FROM count_num WHERE count_date = :my_date"
cursor.execute(sql, {'my_date': count_date})
row = cursor.fetchone()
print(row)
cursor.close()
connection.close()

# if row:
section1_value = float(row[0])
section2_value = float(row[1])

#     # section1 값 변환
# if section1_value >= 0 and section1_value < 1:
#     converted_section1 = 0.1
# elif section1_value >= 1 and section1_value < 2:
#     converted_section1 = 0.2
# elif section1_value >= 2 and section1_value < 3:
#     converted_section1 = 0.3
# elif section1_value >= 3 and section1_value < 4:
#     converted_section1 = 0.4
# elif section1_value >= 4 and section1_value < 5:
#     converted_section1 = 0.5
# elif section1_value >= 5 and section1_value < 6:
#     converted_section1 = 0.6
# elif section1_value >= 6 and section1_value < 7:
#     converted_section1 = 0.7
# elif section1_value >= 7 and section1_value < 8:
#     converted_section1 = 0.8
# elif section1_value >= 8 and section1_value < 9:
#     converted_section1 = 0.9
# elif section1_value >= 9:
#     converted_section1 = 1

# # section2 값 변환
# if section2_value >= 0 and section2_value < 1:
#     converted_section2 = 0.1
# elif section2_value >= 1 and section2_value < 2:
#     converted_section2 = 0.2
# elif section2_value >= 2 and section2_value < 3:
#     converted_section2 = 0.3
# elif section2_value >= 3 and section2_value < 4:
#     converted_section2 = 0.4
# elif section2_value >= 4 and section2_value < 5:
#     converted_section2 = 0.5
# elif section2_value >= 5 and section2_value < 6:
#     converted_section2 = 0.6
# elif section2_value >= 6 and section2_value < 7:
#     converted_section2 = 0.7
# elif section2_value >= 7 and section2_value < 8:
#     converted_section2 = 0.8
# elif section2_value >= 8 and section2_value < 9:
#     converted_section2 = 0.9
# elif section2_value >= 9:
#     converted_section2 = 1

print("변환된 section1 값:", section1_value)
print("변환된 section2 값:", section2_value)
# else:
#     print("데이터가 존재하지 않습니다.")


# Original Image
cover_img = plt.imread('image.jpg')

print("Cover Reference Image")
plt.figure(figsize=(8, 8))
plt.imshow(cover_img)
plt.axis('off')

# Image Dimensions
height, width = cover_img.shape[:2]

# Number of regions
num_regions = 2  # Set to 2 for splitting the screen in half

# Define data for each region
region_width = width // num_regions
region_height = height

# Set the desired values for each region
region_values = np.array([section1_value, section2_value])  # Replace these values with your desired values

# Create the heatmap data
heatmap_data = np.zeros((height, width))
for i in range(num_regions):
    region_value = region_values[i]
    region_x_start = i * region_width
    region_x_end = (i + 1) * region_width
    region_y_start = 0
    region_y_end = height
    heatmap_data[region_y_start:region_y_end, region_x_start:region_x_end] = region_value

# Apply Gaussian blur to the heatmap data
heatmap_detail = 0.05  # Controls the level of blur
filter_h = int(heatmap_detail * height)
filter_w = int(heatmap_detail * width)
heatmap = gaussian_filter(heatmap_data, sigma=(filter_w, filter_h), order=0)

# Display the Cover image with heatmap overlay
plt.figure(figsize=(20, 20))
plt.imshow(cover_img)
plt.imshow(heatmap, cmap='jet', alpha=0.5)
plt.axis('off')
plt.show()