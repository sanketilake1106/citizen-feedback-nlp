topic_to_improvement = {
    "driver": "Consider driver soft skills training or regular customer service workshops.",
    "delay": "Review route timings and real-time GPS monitoring for delay mitigation.",
    "cleanliness": "Increase the frequency of vehicle cleaning and on-board cleanliness checks.",
    "crowded": "Add more buses during peak hours or reallocate resources.",
    "ticket": "Improve ticketing system usability or add more ticket counters/machines.",
    "safety": "Conduct safety audits and ensure security staff presence.",
    "rude": "Reinforce professional conduct via training and monitoring.",
    "noise": "Enforce noise control policies and maintain quiet zones.",
    "air conditioning": "Regularly service HVAC systems for better comfort.",
    "wifi": "Ensure stable and free WiFi or improve connectivity onboard.",
    "information": "Provide clear real-time updates via displays or announcements.",
    "fare": "Review fare structure or add flexible ticket pricing options.",
    "clean": "Ensure regular vehicle sanitization and inspection protocols.",
    "late": "Implement real-time tracking to reduce wait times.",
    "comfort": "Upgrade seating and reduce overcrowding for better comfort.",
    "staff": "Provide customer etiquette training for all staff.",
    "schedule": "Optimize schedules based on demand and traffic patterns.",
    "accessibility": "Ensure ramps, handrails, and priority seating are well maintained.",
    "maintenance": "Regular safety and performance checks on vehicles.",
    "delay_notification": "Send proactive delay alerts for passengers via app/SMS.",
}

def suggest_improvement(topics):
    suggestions = set()
    for topic in topics:
        for key in topic_to_improvement:
            if key in topic:
                suggestions.add(topic_to_improvement[key])
    return list(suggestions)
