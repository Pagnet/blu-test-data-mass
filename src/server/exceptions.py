from flask import jsonify

class Exceptions_errors():
    def make_error(self, status_code, message, obj):
        response = jsonify({
            'status_code': status_code,
            'message': message,
            'payload': obj
        })
        response.status_code = status_code
        return response