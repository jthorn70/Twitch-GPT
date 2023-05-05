from conf import Conf


def read_last_n_lines(file_name, n):
    with open(file_name, "r", encoding='utf-8') as file:
        lines = file.readlines()
        lines = [line for line in lines if not line.startswith("-")]
        lines = lines[-n:]

        return ''.join(lines)


file_name = Conf.channel + "Logs.txt"
