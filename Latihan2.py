data_list = [1, 2, 3, 4, 5, 5, 6]
data_set = {7, 8, 9, 10}
data_tuple = (11, 12, 13, 13, 14)

print("Data List sebelum konversi: ", data_list)
konversi_set = set(data_list)
print("Data Set setelah konversi dari List: ", konversi_set)

print("\nData Set sebelum konversi: ", data_set)
konversi_list = list(data_set)
print("Data List setelah konversi dari Set: ", konversi_list)

print("\nData Tuple sebelum konversi: ", data_tuple)
konversi_set_from_tuple = set(data_tuple)
print("Data Set setelah konversi dari Tuple: ", konversi_set_from_tuple)

print("\nData Set sebelum konversi: ", data_set)
konversi_tuple = tuple(data_set)
print("Data Tuple setelah konversi dari Set: ", konversi_tuple)