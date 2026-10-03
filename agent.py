class AIAgent:

    def process_request(self, user_request):

        request = user_request.lower()


        # Export customer data
        if (
            ("customer" in request or "client" in request)
            and
            ("export" in request or "download" in request or "extract" in request)
        ):
            return "EXPORT_CUSTOMER_DATA"



        # Delete files
        elif (
            "delete" in request
            or "remove file" in request
            or "erase file" in request
            or "remove document" in request
        ):
            return "DELETE_FILE"



        # Employee records
        elif (
            "employee" in request
            or "staff record" in request
            or "employee information" in request
            or "staff details" in request
        ):
            return "READ_EMPLOYEE_RECORDS"



        # Database access
        elif (
            "database" in request
            or "customer database" in request
            or "system database" in request
        ):
            return "READ_DATABASE"



        # Financial reports
        elif (
            "financial" in request
            or "finance report" in request
            or "money report" in request
            or "account report" in request
        ):
            return "ACCESS_FINANCIAL_REPORT"



        # Password reset
        elif (
            "password" in request
            or "reset password" in request
            or "change password" in request
            or "forgot password" in request
        ):
            return "RESET_USER_PASSWORD"



        # Support ticket
        elif (
            "support ticket" in request
            or "support case" in request
            or "create ticket" in request
            or "open ticket" in request
            or "open a case" in request
            or "customer complaint" in request
            or "customer issue" in request
            or "customer problem" in request
            or "problem report" in request
            or "log an issue" in request
        ):
            return "CREATE_SUPPORT_TICKET"



        # Security logs
        elif (
            "security log" in request
            or "audit log" in request
            or "access log" in request
        ):
            return "VIEW_SECURITY_LOGS"



        else:
            return "UNKNOWN_ACTION"