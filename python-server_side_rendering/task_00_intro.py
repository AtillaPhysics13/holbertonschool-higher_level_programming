import os


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Invalid input: template must be a string, got {}".format(type(template).__name__))
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries, got {}".format(type(attendees).__name__))
        return

    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            content = content.replace("{" + key + "}", value)

        output_file = "output_{}.txt".format(index)
        try:
            with open(output_file, 'w') as f:
                f.write(content)
        except Exception as e:
            print("Error writing file {}: {}".format(output_file, e))
