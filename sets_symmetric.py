morning_session = ['Java', 'C', 'Ruby', 'Lisp', 'C#']
afternoon_session = ['Python', 'C#', 'Java', 'C', 'Ruby', 'Lisp']
possible_courses = set(morning_session).symmetric_difference(afternoon_session)
print(possible_courses)