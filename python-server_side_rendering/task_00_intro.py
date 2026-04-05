def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input type")
        return

    if not isinstance(attendees, list):
        print("Invalid input type")
        return

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Invalid input type")
            return
    
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for i, attendee in enumerate(attendees, start=1):
        file_name = f"output_{i}.txt"

        with open(file_name, "w") as file:
            line = template

            name = attendee.get("name") or "N/A"
            event_title = attendee.get("event_title") or "N/A"
            event_date = attendee.get("event_date") or "N/A"
            event_location = attendee.get("event_location") or "N/A"

            line = line.replace("{name}", name)
            line = line.replace("{event_title}", event_title)
            line = line.replace("{event_date}", event_date)
            line = line.replace("{event_location}", event_location)

            file.write(line)
