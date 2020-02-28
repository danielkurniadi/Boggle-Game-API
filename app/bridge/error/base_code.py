"""
ABSTRACTION OF ERROR CODE
"""


class BaseCode:

    def get_result_bool(self):
        raise NotImplementedError

    def get_result_msg(self):
        raise NotImplementedError

    def to_dict(self, *args, **kwargs):
        return {
            'result': self.get_result_bool(),
            'message': self.get_result_msg(),
            'error_code': self.error_code,
        }
