#!/usr/bin/env python3
"""
Parser for all sections of advent.dat
"""

def parse_advent_dat(filename='adventure/advent.dat'):
    """Parse all sections of advent.dat into dictionaries"""
    sections = {}
    current_section = None
    current_data = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # Check for section markers
            if line.isdigit():
                # Save previous section if exists
                if current_section is not None:
                    sections[current_section] = current_data

                current_section = int(line)
                current_data = []
                print(f"Found section {current_section} at line {line_num}")
                continue

            # Skip empty lines and -1 end markers
            if not line or line == '-1':
                continue

            # Add line to current section
            current_data.append(line)

    # Save final section
    if current_section is not None:
        sections[current_section] = current_data

    return sections

def parse_section_data(section_num, data):
    """Parse specific section data into appropriate structure"""
    if section_num == 1:  # Room descriptions
        rooms = {}
        current_room_id = None
        current_description = []

        for line in data:
            if '\t' in line:
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    try:
                        room_id = int(parts[0])
                        description_part = parts[1]

                        # If this is a new room, save the previous one
                        if current_room_id is not None and room_id != current_room_id:
                            rooms[current_room_id] = ' '.join(current_description)

                        # Start accumulating this room's description
                        if room_id != current_room_id:
                            current_room_id = room_id
                            current_description = [description_part]
                        else:
                            # Continue accumulating for the same room
                            current_description.append(description_part)

                    except ValueError:
                        continue

        # Save the last room
        if current_room_id is not None:
            rooms[current_room_id] = ' '.join(current_description)

        return rooms

    elif section_num == 2:  # Short room descriptions
        short_rooms = {}
        for line in data:
            if '\t' in line:
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    try:
                        room_id = int(parts[0])
                        short_rooms[room_id] = parts[1]
                    except ValueError:
                        continue
        return short_rooms

    elif section_num == 3:  # Travel table
        # This is complex, just return raw lines for now
        return data

    elif section_num == 4:  # Vocabulary
        vocab = {}
        for line in data:
            if '\t' in line:
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    try:
                        word_id = int(parts[0])
                        vocab[word_id] = parts[1]
                    except ValueError:
                        continue
        return vocab

    elif section_num == 5:  # Messages
        messages = {}
        for line in data:
            if '\t' in line:
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    try:
                        msg_id = int(parts[0])
                        messages[msg_id] = parts[1]
                    except ValueError:
                        continue
        return messages

    else:
        # Return raw data for other sections
        return data

if __name__ == "__main__":
    sections = parse_advent_dat()

    print(f"\nFound {len(sections)} sections:")
    for section_num in sorted(sections.keys()):
        print(f"Section {section_num}: {len(sections[section_num])} lines")

    # Parse section 1 (rooms)
    if 1 in sections:
        rooms = parse_section_data(1, sections[1])
        rooms_dict = {room_id: description for room_id, description in rooms.items()}
        print(f"\nSection 1 - Rooms: {len(rooms)} rooms")

    # validate map
    print("Validating map...")
    if 3 in sections:
        map = parse_section_data(3, sections[3])
        for location in map:
            map_structure = location.split('\t')
            print(map_structure)
            source_room_int = int(map_structure[0])
            destination_room_int = int(map_structure[1])
            source = rooms_dict[source_room_int]
            if destination_room_int < 131 and destination_room_int > 0:
                #print(destination_room_int)
                destination = rooms_dict[destination_room_int]
            verbs = map_structure[2:]
            #print(f"{source} -> {destination} ({verbs})")

    # Parse section 4 (vocabulary)
    if 4 in sections:
        vocab = parse_section_data(4, sections[4])
        print(f"\nSection 4 - Vocabulary: {len(vocab)} words")

    # find orphaned rooms.  rooms in the source that are not in the destination for any direction
    print("Finding orphaned rooms...")
    rooms = [room_id for room_id,_ in parse_section_data(1, sections[1]).items()]
    map = parse_section_data(3, sections[3])
    source_rooms = []
    destination_rooms = []
    for location in map:
        map_structure = location.split('\t')
        source_rooms.append(int(map_structure[0]))
        destination_rooms.append(int(map_structure[1]))
    orphaned_rooms = set(rooms) - set(destination_rooms)
    # sort
    orphaned_rooms = sorted(orphaned_rooms)
    print(orphaned_rooms)
    