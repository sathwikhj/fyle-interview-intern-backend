from marshmallow import Schema, EXCLUDE, fields, post_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow_enum import EnumField
from core.models.teachers import Teacher
from core.models.principals import Principal
from core.models.students import Student
from core.libs.helpers import GeneralObject


class PrincipalSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Principal
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    # Include other fields specific to Principal if needed
    name = auto_field()
    email = auto_field()
    # Add other fields as necessary

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Principal(**data_dict)
    
class TeacherSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Teacher
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    # Include other fields specific to Principal if needed
    name = auto_field()
    email = auto_field()
    # Add other fields as necessary

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Principal(**data_dict)

class StudentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Student
        unknown = EXCLUDE

    id = auto_field(required=False, allow_none=True)
    # Include other fields specific to Principal if needed
    name = auto_field()
    email = auto_field()
    # Add other fields as necessary

    @post_load
    def initiate_class(self, data_dict, many, partial):
        # pylint: disable=unused-argument,no-self-use
        return Principal(**data_dict)