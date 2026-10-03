class IdentityVerifier:

    def __init__(self):

        self.users = {

            "admin": {
                "role": "administrator",
                "permissions": [
                    "CREATE_SUPPORT_TICKET",
                    "READ_EMPLOYEE_RECORDS",
                    "VIEW_SECURITY_LOGS",
                    "ACCESS_FINANCIAL_REPORT",
                    "EXPORT_CUSTOMER_DATA",
                    "DELETE_FILE",
                    "RESET_USER_PASSWORD"
                ]
            },


            "employee": {
                "role": "support_employee",
                "permissions": [
                    "CREATE_SUPPORT_TICKET",
                    "READ_EMPLOYEE_RECORDS"
                ]
            },


            "data_manager": {
                "role": "data_manager",
                "permissions": [
                    "READ_EMPLOYEE_RECORDS",
                    "ACCESS_FINANCIAL_REPORT",
                    "EXPORT_CUSTOMER_DATA"
                ]
            }

        }


    def verify(self, user):

        if user in self.users:
            return True

        return False


    def get_user_role(self, user):

        if user in self.users:
            return self.users[user]["role"]

        return None


    def check_permission(self, user, action):

        if user in self.users:

            permissions = self.users[user]["permissions"]

            if action in permissions:
                return True

        return False