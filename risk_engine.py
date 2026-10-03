class RiskEngine:

    def calculate_risk(self, action):

        if action == "CREATE_SUPPORT_TICKET":
            return 10


        elif action == "READ_INVENTORY":
            return 20


        elif action == "READ_EMPLOYEE_RECORDS":
            return 50


        elif action == "VIEW_SECURITY_LOGS":
            return 60


        elif action == "RESET_USER_PASSWORD":
            return 70


        elif action == "ACCESS_FINANCIAL_REPORT":
            return 80


        elif action == "EXPORT_CUSTOMER_DATA":
            return 90


        elif action == "DELETE_FILE":
            return 100


        else:
            return 80