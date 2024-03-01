import subprocess

def execute_command(command):
    try:
        if '|' in command:
            commands = command.split('|')
            prev_output = None
            for cmd in commands:
                cmd_parts = cmd.strip().split()
                input_source = subprocess.PIPE if prev_output else None
                proc = subprocess.run(cmd_parts, input=prev_output, capture_output=True, text=True)
                prev_output = proc.stdout
            print(prev_output)
            return
        
        commands = command.split()
        if '>' in commands:
            index = commands.index('>')
            output_file = commands[index + 1]
            output = subprocess.run(commands[:index], capture_output=True, text=True)
            with open(output_file, 'w') as file:
                file.write(output.stdout)
        elif '<' in commands:
            index = commands.index('<')
            input_file = commands[index + 1]
            with open(input_file, 'r') as file:
                output = subprocess.run(commands[:index], input=file.read(), capture_output=True, text=True)
                print(output.stdout)
        else:
            output = subprocess.run(commands, capture_output=True, text=True)
            print(output.stdout)
            
    except FileNotFoundError:
        print("Command not found")
        
    except Exception as e:
        print(f"An error has occurred: {e}")
        


def main():
    while True:
        command = input("shell> ")
        if command.lower() in ['exit', 'quit']:
            print("Exiting shell...")
            break
        execute_command(command)
        
if __name__ == "__main__":
    main()
                
