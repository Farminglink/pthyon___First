import json
CONTACTS_FILE = "contacts.json"

MENU = {
    1:"查询联系人资料",
    2:"插入新的联系人",
    3:"删除已有联系人",
    4:"退出通讯录程序",
}
def show_menu(title):
    print(f"|--- {title} ---|")
    for num,text in MENU.items():
        print(f"|--- {num}:{text} ---|")
        
def load_contacts():
    try:
        with open(CONTACTS_FILE,"r",encoding="UTF-8") as f:
            data = json.load(f)
            
            if isinstance(data,dict):
                return data
            print("通讯录文件格式不正确，将使用空通讯录。")
            return {}
        
    except FileNotFoundError:
        return {}
    
    except json.JSONDecodeError:
        print("通讯录文件损毁，将使用空通讯录!")
        return {}

def save_contacts(contacts):
    try:
        with open(CONTACTS_FILE,"w",encoding="UTF-8") as f:
            json.dump(contacts,f,ensure_ascii=False,indent=2)
        return True
    except OSError as e:
        print(f"保存失败：{e}")
        return False

def get_name() -> str:
    while True:
        name = input("请输入联系人姓名：").strip()
        if name:
            return name
        print("姓名不能为空！")

def get_phone_number() -> str:
    while True:
        phone_number = input("请输入用户联系电话：").strip()
        if not phone_number:
            print("电话号码不能为空！")
            continue
        has_error = False
        for ch in phone_number:
            if not (ch.isdigit() or ch in "+ -"):
                has_error = True
                break
        if has_error:
            print("电话号码只能包含数字、+、- 和空格，请重新输入!")
            continue
        return phone_number
        
def get_int():
    while True:
        try:
            n = int(input("请输入相关指令代码："))
            if n in MENU:
                return n
            else:
                show_menu("请正确使用本程序")
        except ValueError:
            show_menu("请正确使用本程序")
def ask_yes_no(prompt):
    yes = ("yes","y","1","是")
    no = ("no","n","0","否","不是")
    while True:
        answer = input(prompt).strip().lower()
        if answer in yes:
            return True
        elif answer in no:
            return False
        else:
            print("请输入正常指令！")

def delete_contact(contacts, name):
    new_contacts = contacts.copy()
    del new_contacts[name]

    if save_contacts(new_contacts):
        print(f"{name}已成功删除!")
        return new_contacts
    else:
        print("保存失败，本次操作没有生效!")
        return contacts

def set_contact(contacts, name, phone_number):
    new_contacts = contacts.copy()
    new_contacts[name] = phone_number

    if save_contacts(new_contacts):
        print(f"已成功保存{name}用户号码！")
        return new_contacts
    else:
        print("保存失败，本次操作没有生效!")
        return contacts

def do_query(contacts):
    print("|--- 您正在使用查询功能 ---|")
    name = get_name()
    if name in contacts:
        print(name+' '+contacts[name])
    else:
        if ask_yes_no("未查找到该联系人，是否录入？(Yes/No)"):
            phone_number = get_phone_number()
            contacts = set_contact(contacts,name,phone_number)
        else:
            print("已取消录入！")
    print()
    return contacts

def do_add(contacts):
    print("|--- 您正在使用插入功能 ---|")
        
    name = get_name()
    if name in contacts:
        print("您输入的姓名在通讯录中已存在 -->>"+contacts[name])
        if ask_yes_no("是否修改用户联系电话(Yes/No)："):
            phone_number = get_phone_number()
            contacts = set_contact(contacts,name,phone_number)
    else:
        phone_number = get_phone_number()
        contacts = set_contact(contacts,name,phone_number)

    print()
    return contacts

def do_delete(contacts):
    print("|--- 您正在使用删除功能 ---|")
    
    name = get_name()
    if name in contacts:
        if ask_yes_no(f"确定要删除联系人{name}吗？(Yes/No)"):
            contacts = delete_contact(contacts,name)
        else:
            print(f"已取消本次删除,{name}还在您的通讯录当中！")
    else:
        print("联系人不存在")

    print()
    return contacts

def do_exit():
    print("|--- 感谢使用本通讯录程序 ---|")

def main():
    contacts = load_contacts()
    show_menu("欢迎进入通讯录程序")
    print()

    handlers = {
        1:do_query,
        2:do_add,
        3:do_delete,
    }
    while True:
        order = get_int()
        if order == 4:
            do_exit()
            break
        contacts = handlers[order](contacts)
if __name__ == "__main__":
    main()
