import os
import datetime

filepath = input("Enter the file path:")
filename = input("Enter the file name:")
temp = os.path.dirname(filepath)
#temp = os.path.dirname(__file__)
srt_file_path = os.path.join(temp, filename)


def read_srt_file_gen():
    with open(srt_file_path, "r") as fs:
        for data in fs.readlines():
            yield data


def read_srt_file():
    with open(srt_file_path, "r") as fs:
        data = fs.read()
    return data


def start():
    new_data_str = read_srt_file()
    for item in read_srt_file_gen():
        if "--> " in item:
            time_arr = item.split('--> ')
            start_time = time_arr[0].replace(" ", "")
            end_time = time_arr[1].replace("\n", "")
            _new_start_time = datetime.datetime.strptime(start_time + "0", "%H:%M:%S,%f") - datetime.timedelta(
                seconds=1)
            _new_end_time = datetime.datetime.strptime(end_time + "0", "%H:%M:%S,%f") - datetime.timedelta(
                seconds=1)
            new_start_time = datetime.datetime.strftime(
                _new_start_time, "%H:%M:%S,%f")[:-3]
            new_end_time = datetime.datetime.strftime(
                _new_end_time, "%H:%M:%S,%f")[:-3]
            new_data_str = new_data_str.replace(
                start_time, new_start_time).replace(end_time, new_end_time)
    return new_data_str


if __name__ == '__main__':
    print(start())
