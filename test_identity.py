from zero_trust.identity import IdentityVerifier


identity = IdentityVerifier()


print(identity.verify("employee"))

print(identity.get_user_role("employee"))

print(identity.check_permission(
    "employee",
    "EXPORT_CUSTOMER_DATA"
))


print(identity.check_permission(
    "employee",
    "CREATE_SUPPORT_TICKET"
))