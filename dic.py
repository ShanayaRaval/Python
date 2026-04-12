student_data = {
    'id1' : {'Name' : 'Sara', 'Grade' : 'VI', 'subject_integration' : 'English, Math, Science'},
    'id2' : {'Name' : 'David', 'Grade' : 'VI', 'subject_integration' : 'English, Math, Science'},
    'id3' : {'Name' : 'Sara', 'Grade' : 'VI', 'subject_integration' : 'English, Math, Science'},
    'id4' : {'Name' : 'Surya', 'Grade' : 'VI', 'subject_integration' : 'English, Math, Science'},
}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    uni_key = (details['Name'], details['Grade'], details['subject_integration'])

    if uni_key not in seen_keys:
        seen_keys.append(uni_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ':', v)