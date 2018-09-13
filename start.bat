@echo off

REM --------------------修改start------------------------------
set python_env=D:\test\mechine_learning\venv\Scripts
set pyMd2Doc_path=D:\workspace\pyMarkdown-master\app
REM --------------------修改end------------------------------

%python_env%\pip install -r requirements.txt
cd %pyMd2Doc_path%
%python_env%\python main.py

pause
