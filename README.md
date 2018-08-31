# ai-writing

这是AI辅助项目的后端2018-7

## Getting start

首先确认您使用 Python3 并已经安装了 conda 或者 virtualenv

```bash
git clone https://github.com/MasterFishfish/ai-writing.git
cd ai-writing/mysite
virtualenv venv # 假设您使用 virtualenv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
