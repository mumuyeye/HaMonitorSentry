# HaMonitorSentry 高层智能监测系统

> “HaMonitorSentry”是专为高层建筑和人群密集区设计的高级智能安防系统。该系统结合高分辨率、高帧率摄像技术和双角度监测策略，适用于智慧安防、智慧社区和智能建筑等行业，致力于与物业、企业、政府合作，以保障公民的生命和财产安全。

![系统概览](img/new_start.jpg)

## 系统运行环境

- **操作系统**: Ubuntu 20.04.3 LTS (Focal Fossa)

## 配置环境包

```bash
git clone https://github.com/mumuyeye/HaMonitorSentry.git
cd HaMonitorSentry
conda env create -f environment.yml
conda activate sentry
```

## 系统显示字体安装

```bash
# 创建字体目录（如果尚未存在）
mkdir -p ~/.local/share/fonts
# 复制字体文件
cp /root/sentry/HaMonitorSentry/MSYH.TTF ~/.local/share/fonts/
# 更新字体缓存
fc-cache -fv
# 验证字体是否安装成功
fc-list | grep "MSYH"
```

## 运行系统

```bash
python demo.py
```

---

驭科技以守护，持创新以护航，“HaMonitorSentry-高层智能监测系统”定会成为“智能安防，平安中国”之船的重要组成部分，载着人民共同渡往安全幸福的彼方。