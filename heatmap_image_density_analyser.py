import cv2
import os
import numpy as np

def heatmap_percentage(image_path, lower_threshold, upper_threshold):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)
    heatmap_pixels = np.count_nonzero(mask)

    total_pixels = image.shape[0] * image.shape[1]
    percentage = (heatmap_pixels / total_pixels) * 100

    return percentage

def max_heatmap_coordinates(image_path, lower_threshold, upper_threshold):
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv_image, lower_threshold, upper_threshold)
    max_intensity = np.max(mask)
    max_coordinates = np.argwhere(mask == max_intensity)

    return max_coordinates

root_directory = './Results'

red_lower_threshold = np.array([0, 70, 150])
red_upper_threshold = np.array([10, 255, 255])

yellow_lower_threshold = np.array([20, 100, 150])
yellow_upper_threshold = np.array([35, 255, 255])

green_lower_threshold = np.array([60, 90, 120])
green_upper_threshold = np.array([80, 255, 255])

for directory, _, files in os.walk(root_directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)

            red_percentage = heatmap_percentage(image_path, red_lower_threshold, red_upper_threshold)
            yellow_percentage = heatmap_percentage(image_path, yellow_lower_threshold, yellow_upper_threshold)
            green_percentage = heatmap_percentage(image_path, green_lower_threshold, green_upper_threshold)

            print(f"Percentage of heatmap coverage in {directory}/{filename}:")
            print(f"  Red: {red_percentage:.2f}%")
            print(f"  Yellow: {yellow_percentage:.2f}%")
            print(f"  Green: {green_percentage:.2f}%")

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)

            red_coordinates = max_heatmap_coordinates(image_path, red_lower_threshold, red_upper_threshold)
            yellow_coordinates = max_heatmap_coordinates(image_path, yellow_lower_threshold, yellow_upper_threshold)
            green_coordinates = max_heatmap_coordinates(image_path, green_lower_threshold, green_upper_threshold)

            print(f"Coordinates of most intense heatmap colors in {directory}/{filename}:")
            print(f"  Red: {red_coordinates}")
            print(f"  Yellow: {yellow_coordinates}")
            print(f"  Green: {green_coordinates}")
