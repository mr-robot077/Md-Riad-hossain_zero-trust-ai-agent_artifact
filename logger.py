from datetime import datetime


class SecurityLogger:

    def log_event(self, user, action, risk_score, decision):

        timestamp = datetime.now()

        message = (
            f"{timestamp} | "
            f"User: {user} | "
            f"Action: {action} | "
            f"Risk: {risk_score} | "
            f"Decision: {decision}\n"
        )

        with open("logs/security.log", "a") as file:
            file.write(message)