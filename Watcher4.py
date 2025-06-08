            if x == config_file_path2:
                file_path = 'Asterea.txt'
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
