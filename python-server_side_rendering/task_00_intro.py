def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template must be a string")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict)
                                                  for a in attendees):
        print("Error: attendees must be a list of dictionaries")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    index = 1

    for attendee in attendees:
        invitation_text = template
        
        value = attendee.get('name') or "N/A"
        invitation_text = invitation_text.replace("{name}", value)

        value = attendee.get('event_title') or "N/A"
        invitation_text = invitation_text.replace("{event_title}", value)

        value = attendee.get('event_date') or "N/A"
        invitation_text = invitation_text.replace("{event_date}", value)

        value = attendee.get('event_location') or "N/A"
        invitation_text = invitation_text.replace("{event_location}", value)

        with open(f"output_{index}.txt", "w") as f:
            f.write(invitation_text)
        index += 1
