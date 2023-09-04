import time
import winsound

def focus_timer(work_minutes, break_minutes):
    while True:
        print("开始工作 {} 分钟".format(work_minutes))
        time.sleep(work_minutes * 60)
        winsound.Beep(1000, 1000)  # 发出声音提醒工作时间结束
        print("休息 {} 分钟".format(break_minutes))
        time.sleep(break_minutes * 60)
        winsound.Beep(1000, 1000)  # 发出声音提醒休息时间结束

if __name__ == "__main__":
    work_minutes = 25  # 设置工作时间为 25 分钟
    break_minutes = 5  # 设置休息时间为 5 分钟
    focus_timer(work_minutes, break_minutes)
