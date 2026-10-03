from zero_trust.identity import IdentityVerifier
from zero_trust.risk_engine import RiskEngine
from zero_trust.policy_engine import PolicyEngine
from zero_trust.logger import SecurityLogger


class ZeroTrustDecision:

    def __init__(self):

        self.identity = IdentityVerifier()
        self.risk_engine = RiskEngine()
        self.policy_engine = PolicyEngine()
        self.logger = SecurityLogger()


    def check_request(self, user, action):

        # Step 1: Verify identity
        identity_result = self.identity.verify(user)


        if not identity_result:

            self.logger.log_event(
                user,
                action,
                100,
                "DENY"
            )

            return {
                "User": user,
                "Action": action,
                "Risk Score": 100,
                "Decision": "DENY - Unknown User"
            }



        # Step 2: Check user permission
        permission_result = self.identity.check_permission(
            user,
            action
        )


        if not permission_result:

            self.logger.log_event(
                user,
                action,
                90,
                "DENY - Permission Failed"
            )

            return {
                "User": user,
                "Action": action,
                "Risk Score": 90,
                "Decision": "DENY - Permission Failed"
            }



        # Step 3: Calculate risk
        risk_score = self.risk_engine.calculate_risk(
            action
        )



        # Step 4: Policy decision
        decision = self.policy_engine.evaluate(
            user,
            action,
            risk_score
        )



        # Step 5: Security logging
        self.logger.log_event(
            user,
            action,
            risk_score,
            decision
        )



        return {
            "User": user,
            "Action": action,
            "Risk Score": risk_score,
            "Decision": decision
        }