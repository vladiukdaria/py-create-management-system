import dataclasses
from datetime import datetime
from typing import List
import pickle


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


def write_groups_information(groups: List[Group]) -> int:
    """Сохраняет группы в 'groups.pickle', возвращает макс. число студентов"""
    with open("groups.pickle", "wb") as f:
        pickle.dump(groups, f)
    return max(len(g.students) for g in groups) if groups else 0


def write_students_information(students: List[Student]) -> int:
    """Сохраняет студентов в 'students.pickle', возвращает количество"""
    with open("students.pickle", "wb") as f:
        pickle.dump(students, f)
    return len(students)


def read_groups_information() -> List[str]:
    """Читает группы из 'groups.pickle', возвращает уникальные названия специальностей"""
    with open("groups.pickle", "rb") as f:
        groups: List[Group] = pickle.load(f)
    return list({g.specialty.name for g in groups})


def read_students_information() -> List[Student]:
    """Читает студентов из 'students.pickle'"""
    with open("students.pickle", "rb") as f:
        students: List[Student] = pickle.load(f)
    return students
