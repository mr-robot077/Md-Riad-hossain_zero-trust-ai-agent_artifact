class PolicyEngine:

    def evaluate(self, user, action, risk_score):

        # Admin policy
        if user == "admin":

            # Admin can perform high-risk actions
            # but extremely dangerous actions still need control
            if risk_score <= 90:
                return "ALLOW"

            else:
                return "REQUIRE_APPROVAL"


        # Employee policy

        elif user == "employee":

            allowed_actions = [
                "CREATE_SUPPORT_TICKET",
                "READ_INVENTORY",
                "READ_EMPLOYEE_RECORDS"
            ]

            if action in allowed_actions:

                if risk_score <= 50:
                    return "ALLOW"

                else:
                    return "REQUIRE_APPROVAL"


            else:
                return "DENY"


        # Unknown users

        else:
            return "DENY"