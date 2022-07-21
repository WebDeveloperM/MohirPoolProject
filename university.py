import uuid
from pprint import pprint
import json
import os

FILENAME = 'UniversitySystem.json'


class University:
    def add(self):
        print(
            "You are adding student !!! Choose level student, if Undergraduate = U, if Postgraduate = P"
        )
        choice = input("Choose: ")

        if is_file_empty(FILENAME):
            data = {
                "undergraduate": [],
                "postgraduate": []
            }
            # Serializing json
            json_object = json.dumps(data)

            with open(FILENAME, "w") as outfile:
                outfile.write(json_object)

        if choice == "U":
            id = input("Id: ")
            full_name = input("Fullname as, John Doe Dodge: ")
            nationality = input("Nationality: ")
            gender = input("Gender: ")
            faculty = input("Faculty: ")
            admission_year = input("Admission year: ")
            residential_hall = input("Residential hall: ")

            new_student = {
                "id": id,
                "full_name": full_name,
                "nationality": nationality,
                "gender": gender,
                "faculty": faculty,
                "admission_year": admission_year,
                "residential_hall": residential_hall,
            }

            writing_in_json_file(FILENAME, 'undergraduate', new_student)

        if choice == "P":
            id=input("Id: ")
            full_name = input("Fullname as, John Doe Dodge: ")
            nationality = input("Nationality: ")
            gender = input("Gender: ")
            faculty = input("Faculty: ")
            admission_year = input("Admission year: ")
            supervisor_name = input("Supervisor name: ")
            research_topic = input("Research topic: ")

            new_student = {
                "id": id,
                "full_name": full_name,
                "nationality": nationality,
                "gender": gender,
                "faculty": faculty,
                "admission_year": admission_year,
                "supervisor_name": supervisor_name,
                "research_topic": research_topic,
            }

            writing_in_json_file(FILENAME, 'postgraduate', new_student)

    def remove(self):
        if is_file_empty(FILENAME):
            print('File is empty or doesn\'t not exist')
            return

        with open(FILENAME, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if len(data) == 0:
            print('Not added any students yet!')
            return

        student_id = input("Which student do you want remove !!! Write student id:  ")

        under = data['undergraduate']
        post = data['postgraduate']

        all = under + post
        i = 0
        while i < len(all):
            if all[i]['id'] == student_id and i < len(under):
                under.pop(i)
                break
            elif all[i]['id'] == student_id and i >= len(under):
                post.pop(i - len(under))
                break
            else:
                print('Student not found !!!')
            i += 1

        new_data = {
            "undergraduate": under,
            "postgraduate": post,
        }

        with open(FILENAME, 'w') as f:
            json.dump(new_data, f)

    def find(self):
        if is_file_empty(FILENAME):
            print('File is empty or doesn\'t not exist')
            return

        with open(FILENAME, 'r', encoding='utf-8') as file:
            data = json.load(file)
            all_students = data["undergraduate"] + data["postgraduate"]

        if len(all_students) == 0:
            print('Not added any students yet!')
            return

        student_id = input("Which student you want find ? Write student id:  ")

        for student in all_students:
            print(student['id'])
            if student['id'] == student_id:
                print(f'Urraaa we found student: {student}')
                pprint(student)
                break
        else:
            print('Student not found !!! ')

    def display_all(self):
        if is_file_empty(FILENAME):
            print('File is empty or doesn\'t not exist')
            return

        with open(FILENAME, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if len(data) == 0:
            print('Not added any students yet!')
            return

        print(f'Students count is {len(data["undergraduate"] + data["postgraduate"])}')
        pprint(data)


def randomIdentifier():
    return str(uuid.uuid1())


def is_file_empty(filename):
    return os.path.isfile(filename) and os.path.getsize(filename) == 0 or not os.path.exists(filename)


def writing_in_json_file(filename, level, data):
    with open(filename, "r", encoding='utf-8') as file:
        list_data = json.load(file)
    list_data[level].append(data)
    list_data.update(list_data)
    with open(filename, 'w') as file:
        json.dump(list_data, file)
    print('Successfully written to the JSON file')
