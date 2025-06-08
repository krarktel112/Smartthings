        if not event.is_directory:
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
            config = read_config_json(config_file_path)
            x = event.src_path
            #print(f"File opened: {event.src_path} {timestamp_str} {config}")
            if x == config_file_path2:
                file_path = 'Emma.txt'
                with open(file_path, 'a') as file:
                    file.write(f"Korra: {timestamp_str} {config}\n")
                with open(file_path, "r") as file:
                    lines = file.readlines()
                    last_line = lines[-1]
                    if "online" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "idle" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "dnd" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "offline" in last_line:
                        if y == "offline":
                            y == "offline"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley3'])
                            except:
                                print("Error")
                            y == "offline"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "gaming" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "listening" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
                    if "playing" in last_line:
                        if y == "online":
                            y == "online"
                        else:
                            try:
                                ST.execute_scene(ST.scenes['Home']['Ashley2'])
                            except:
                                print("Error")
                            y == "online"
                            print(f"Korra: {timestamp_str} {config}\n")
