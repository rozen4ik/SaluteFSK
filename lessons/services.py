class KonturMessage:
    @staticmethod
    def message_info_card(number_card):
        message = f"<?xml version=\"1.0\" encoding=\"windows1251\" ?>" \
                  "<spd-xml-api>" \
                  "<request version=\"1.0\" ruid=\"739F9F2B-AEDD-4D94-93FF-EB59A9A1FCF5\">" \
                  f"<client identifier=\"{number_card}\">" \
                  "<attributes />" \
                  "<identifiers />" \
                  "</client>" \
                  "</request>" \
                  "</spd-xml-api>"
        return message

    @staticmethod
    def message_block_device(device_id):
        message = "<?xml version=\"1.0\" encoding=\"Windows-1251\"?> " \
                  "<script session=\"85D323F3-8EBD-48E6-A085-4E652468B8D6\"> " \
                  f"<command name=\"cLockDevice\" device=\"{device_id}\" guid=\"95D454F3-8EBD-50E6-A085-4E644468B8D6\"> " \
                  "<param name=\"cpLocker\">Карта Тройка</param> " \
                  "<param name=\"cpDuration\">30000</param> " \
                  "<param name=\"cpSession\">85D323F3-8EBD-48E6-A085-4E652468B8D6</param> " \
                  "</command> " \
                  "</script>"
        return message

    @staticmethod
    def message_passage_card(device_id, number_card):
        message = "<?xml version=\"1.0\" encoding=\"Windows-1251\"?> " \
                  "<script session=\"85D323F3-8EBD-48E6-A085-4E652468B8D6\"> " \
                  f"<command name=\"cRequest\" device=\"{device_id}\" guid=\"44871464-8EBD-56E6-A085-4E654768B8D6\"> " \
                  f"<param name=\"cpCard\">{number_card}</param> " \
                  "<param name=\"cpCardType\">1</param> " \
                  "<param name=\"cpDirection\">1</param> " \
                  "<param name=\"cpText\">Запрос по карте</param> " \
                  "</command> " \
                  "</script>"
        return message

    @staticmethod
    def message_unblock_device(device_id):
        message = "<?xml version=\"1.0\" encoding=\"Windows-1251\"?> " \
                  "<script session=\"85D323F3-8EBD-48E6-A085-4E652468B8D6\"> " \
                  f"<command name=\"cUnlockDevice\" device=\"{device_id}\" guid=\"98545167-8EBD-6578-A085-4E633368B8D6\"> " \
                  "<param name=\"cpLocker\">Карта Тройка</param> " \
                  "<param name=\"cpDuration\">30000</param> " \
                  "<param name=\"cpSession\">85D323F3-8EBD-48E6-A085-4E652468B8D6</param> " \
                  "</command> " \
                  "</script>"
        return message

    @staticmethod
    def answer_device(device_id):
        message = "<?xml version=\"1.0\" encoding=\"Windows-1251\"?> " \
                  "<script session=\"85D323F3-8EBD-48E6-A085-4E652468B8D6\"> " \
                  f"<wait delay=\"20000\" device=\"{device_id}\"/> " \
                  "</script>"
        return message
