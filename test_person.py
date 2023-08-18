import unittest
import person   
from fields import PersonPhoneNumbers, PersonAddress, PersonBirthday, PersonEmailAddress, PersonName, PersonNote, PersonStatus, PersonFormatterInfo
from my_exception import ExceptionIncorrectFormat

class TestPerson(unittest.TestCase):
    def test_phone_add(self):
        self.assertEqual(person.Person.phone_add(p, PersonPhoneNumbers("0951232323")), "Phone додано")

if __name__ == "__main__":
    p = person.Person(PersonName("name"), PersonPhoneNumbers(""), PersonEmailAddress(""), PersonBirthday(""), PersonStatus(""), PersonAddress("", "", ""), PersonNote(""))
    unittest.main()
    list_car = [str(car) for car in range(0,100)]