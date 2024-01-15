from flask import Blueprint, make_response
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment, AssignmentStateEnum

from .schema import AssignmentSchema, AssignmentGradeSchema
teacher_assignments_resources = Blueprint('teacher_assignments_resources', __name__)

@teacher_assignments_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_assignments(p):
    teachers_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    teachers_assignments_dump = AssignmentSchema().dump(teachers_assignments, many=True)
    return APIResponse.respond(data=teachers_assignments_dump)

@teacher_assignments_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def grade_assignment(p,incoming_payload):
    grade_assignment_payload = AssignmentGradeSchema().load(incoming_payload)

    assignment = Assignment.get_by_id(grade_assignment_payload.id)

    if not assignment:
        error_message = "FyleError"
        response_data = {"error": error_message}
        status_code = 404
    elif assignment.state != AssignmentStateEnum.DRAFT:
        error_message = "FyleError"
        response_data = {"error": error_message}
        status_code = 400
    elif not assignment.content.strip():
        error_message = "FyleError"
        response_data = {"error": error_message}
        status_code = 400
    elif assignment.teacher_id != p.teacher_id:
        error_message = "FyleError"
        response_data = {"error": error_message, "message": "Unauthorized to grade this assignment"}
        status_code = 400
    else:
        graded_assignment = Assignment.mark_grade(
            _id=grade_assignment_payload.id,
            grade=grade_assignment_payload.grade,
            auth_principal=p
        )
        db.session.commit()
        graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
        response_data = {"data": graded_assignment_dump}
        status_code = 200
    response = make_response(response_data, status_code)
    return response

