DOC_URL = "https://github.com"

def print_all_commands(commands, prefix):
    help_text_list = [
        "[지원하는 명령어 목록]",
        prefix + "도움말 [명령어] 로 명령어에 대한 자세한 설명을 볼 수 있습니다.",
        "전체 매뉴얼: " + DOC_URL,
        ""
    ]
    for cmd in commands:
        if cmd.hidden:
            continue

        cmd_help = prefix + cmd.name
        if cmd.usage != None:
            cmd_help += " " + cmd.usage

        help_text_list.append(cmd_help)

    full_text = '\n'.join(help_text_list) + '\n'
    return "```" + full_text + "```"


def get_help_command(bot, *args):
    arg_len = len(args)
    commands = bot.commands
    prefix = bot.command_prefix

    if arg_len == 0:
        return print_all_commands(commands, prefix)
    else:
        for cmd in commands:
            if cmd.name == args[0]:
                return print_command_help(cmd, prefix)
        return "해당 명령어가 존재하지 않습니다."


def print_command_help(command, prefix):
    help = prefix + command.name
    if command.usage != None:
        help += " " + command.usage

    help += "\n"
    help += command.description

    return "```" + help + "```"
