from re import search


class DataSourceInfoCard:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

    def get_list_package(self):
        msg = self.message.partition('<package')[2]
        msg = f"<package {msg}"
        list_package = msg.partition('</identifier>')[0]

        list_rule_use = []
        list_use_count = []
        list_used_count = []

        for i in list_package.split('" '):
            msg = i.partition('description="')[2]
            list_rule_use.append(msg)
            msg = i.partition('use_count="')[2]
            list_use_count.append(msg)
            msg = i.partition('used_count="')[2]
            list_used_count.append(msg)

        list_rule_use = [e for e in list_rule_use if e]
        list_use_count = [e for e in list_use_count if e]
        list_used_count = [e for e in list_used_count if e]

        size_package = len(list_used_count)
        packages = []
        b = 0

        while b < size_package:
            packages.append(f"Услуга: {list_rule_use[b]}, Всего занятий: {list_use_count[b]}, Посещено занятий: {list_used_count[b]}")
            b += 1

        return packages

    def get_full_name(self):
        f_name = self.message.partition('<attribute name="fname"  comment="Имя"  value="')[2]
        f_name = f_name.partition('"')[0]
        l_name = self.message.partition('<attribute name="lname"  comment="Фамилия"  value="')[2]
        l_name = l_name.partition('"')[0]
        m_name = self.message.partition('<attribute name="mname"  comment="Отчество"  value="')[2]
        m_name = m_name.partition('"')[0]
        full_name = f"{l_name} {f_name} {m_name}"
        return full_name

    def get_msg(self):
        msg = self.message.partition('<Message>')[2]
        msg = msg.partition('</Message>')[0]
        msg = f"<?xml version=\"1.0\" encoding=\"Windows-1251\"?>" \
              f"<script session=\"85D323F3-8EBD-48E6-A085-4E652468B8D6\">" \
              f"<Message>{msg}</Message>" \
              f"</script>"
        msg = msg.replace("rPrior", "rFinal")
        return msg

    def get_balance_card(self):
        if '<currency name="RUB"  comment="Российский рубль"  value="' in self.message:
            msg = self.message.partition('<currency name="RUB"  comment="Российский рубль"  value="')[2]
            msg = msg.partition('"')[0]
            msg = msg[:-1]
            return f"{msg} руб."
        else:
            return "Баланса нет"

    def get_balance_package(self):
        msg = self.message.partition(',Остаток=')[2]
        msg = msg.partition(',')[0]
        return f"Осталось {msg} занятий"
