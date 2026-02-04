import dataclasses
from datetime import datetime
from typing import List
import pickle


# ----------------- Dataclasses -----------------
@dataclasses.dataclass
class Specialty:
    name: str
    number: int


@dataclasses.dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclasses.dataclass
class Group:
    specialty: Specialty
    course: int
    students: List[Student]


# ----------------- Functions with pickle -----------------
def write_groups_information(groups: List[Group]) -> int:
    """Write groups to 'groups.pickle' and return max number of students in a group"""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    # Максимальное количество студентов в группе
    return max(len(group.students) for group in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    """Write all students to 'students.pickle' and return total number of students"""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    """Read groups from 'groups.pickle' and return unique specialty names"""
    with open("groups.pickle", "rb") as f:
        groups: List[Group] = pickle.load(f)
    # Собираем уникальные названия специальностей
    return list({group.specialty.name for group in groups})


def read_students_information() -> List[Student]:
    """Read students from 'students.pickle' and return list of Student objects"""
    with open("students.pickle", "rb") as f:
        students: List[Student] = pickle.load(f)
    return students
