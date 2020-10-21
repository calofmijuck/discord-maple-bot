def print_all_commands(commands, prefix):
    help_text_list = []
    for cmd in commands:
        if cmd.hidden:
            continue
        
        cmd_help = prefix + cmd.name
        if cmd.usage != None:
            cmd_help += " " + cmd.usage
        
        cmd_help += "\n"
        if cmd.brief != None:
            cmd_help += cmd.brief + "\n"
        
        help_text_list.append(cmd_help)
    
    full_text = '\n'.join(help_text_list) + '\n'
    full_text += prefix + "도움말 [명령어] 로 명령어에 대한 자세한 설명을 볼 수 있습니다."
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
                return "추가 예정"
        return "해당 명령어가 존재하지 않습니다."
