import json

def load_budget (filename= "budget.json"):
    default_data = {"limit": 0,"transactions": []}
    try:
        with open(filename ,"r", encoding = "utf-8") as file:
            data = json.load(file)
            if not isintantance(data, dict):
                return default_data
            data.setdefault("limit",0)
            data.setdefault("transactions",[])
            return data
    except FileNotError:
        print(f"файл f'{filename}' не найден . Создан пустой бюджет")
        save_budger(default_data, filename)
        return default_data
    except json.JSONDecodeError:
        print(f"Ошибка чтения '{filename}' Загружен пустой бюджет.")
        return default_data

def save_budget(data, filename="budget.json"):

     with open (filename,"w",encoding ="utf-8") as file:
        json.dump (data,file,ensure_ascii = False, indent=2)