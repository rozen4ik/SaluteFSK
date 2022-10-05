from re import search


class DataSourceInfoCard:

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message

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
