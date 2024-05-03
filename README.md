# HaMonitorSentry
## 配置环境
```bash
git clone https://github.com/mumuyeye/HaMonitorSentry.git
cd HaMonitorSentry
conda env create -f environment.yml
```
## 字体安装
```bash
mkdir -p ~/.local/share/fonts  # 创建字体目录如果它还不存在
cp /root/sentry/HaMonitorSentry/MSYH.TTF ~/.local/share/fonts/
fc-cache -fv
fc-list | grep "MSYH"
```