```console
py -m venv env
.\env\Scripts\activate
pip install -r requirements.txt
```
Copy `vi_VN.aff` và `vi_VN.dic` vào `.\env\Lib\site-packages\enchant\data\mingw64\share\enchant\hunspell`
```console
flask --app main run
```