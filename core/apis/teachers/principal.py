from flask import Blueprint, make_response
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher
from core.models.principals import Principal
from core.models.students import Student

principal_teacher_resources = Blueprint('principal_teacher_resources', __name__)

@principal_teacher_resources.route('/teacher', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teacher():
    """List all teachers in the system."""
    