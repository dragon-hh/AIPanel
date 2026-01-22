import subprocess
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
# 拆分参数为列表（避免空格解析错误，subprocess 推荐列表形式）
cmd_args = [
chrome_path,
    "--remote-debugging-port=9222",
    r"--user-data-dir=C:\sel_chrome_profile"
]
process = subprocess.Popen(
    cmd_args,
    stdout=subprocess.PIPE,  # 屏蔽控制台输出（可选）
    stderr=subprocess.PIPE,
    creationflags=subprocess.CREATE_NEW_PROCESS_GROUP  # Windows 下独立进程组
)
print(f"Chrome 已启动，进程ID：{process.pid}")
print(f"调试端口：9222，用户数据目录：C:\\sel_chrome_profile")