"""Exceptions raised by the Route53 service."""
from moto.core.exceptions import RESTError


class Route53ClientError(RESTError):
    """Base class for Route53 errors."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("template", "wrapped_single_error")
        super().__init__(*args, **kwargs)


class InvalidInput(Route53ClientError):
    """Malformed ARN for the CloudWatch log group."""

    code = 400

    def __init__(self, message: str):
        super().__init__("InvalidInput", message)


class InvalidCloudWatchArn(InvalidInput):
    def __init__(
        self,
    ):
        message = "The ARN for the CloudWatch Logs log group is invalid"
        super().__init__(message)


class InvalidActionValue(InvalidInput):
    def __init__(self, value: str):
        message = (
            f"Invalid XML ; cvc-enumeration-valid: Value '{value}' is not facet-valid"
            " with respect to enumeration '[CREATE, DELETE, UPSERT]'. It must be a value from the enumeration."
        )
        super().__init__(message)


class InvalidPaginationToken(Route53ClientError):
    """Bad NextToken specified when listing query logging configs."""

    code = 400

    def __init__(self):
        message = (
            "Route 53 can't get the next page of query logging configurations "
            "because the specified value for NextToken is invalid."
        )
        super().__init__("InvalidPaginationToken", message)


class InvalidVPCId(Route53ClientError):
    """Missing/Invalid VPC ID"""

    code = 400

    def __init__(self):
        message = "Invalid or missing VPC Id."
        super().__init__("InvalidVPCId", message)
        self.content_type = "text/xml"


class NoSuchCloudWatchLogsLogGroup(Route53ClientError):
    """CloudWatch LogGroup has a permissions policy, but does not exist."""

    code = 404

    def __init__(self):
        message = "The specified CloudWatch Logs log group doesn't exist."
        super().__init__("NoSuchCloudWatchLogsLogGroup", message)


class NoSuchHostedZone(Route53ClientError):
    """HostedZone does not exist."""

    code = 404

    def __init__(self, host_zone_id):
        message = f"No hosted zone found with ID: {host_zone_id}"
        super().__init__("NoSuchHostedZone", message)
        self.content_type = "text/xml"


class NoSuchHealthCheck(Route53ClientError):
    """HealthCheck does not exist."""

    code = 404

    def __init__(self, health_check_id):
        message = f"A health check with id {health_check_id} does not exist."
        super().__init__("NoSuchHealthCheck", message)
        self.content_type = "text/xml"


class HostedZoneNotEmpty(Route53ClientError):
    """HostedZone does not exist."""

    code = 400

    def __init__(self):
        message = (
            "The hosted zone contains resource records that are not SOA or NS records."
        )
        super().__init__("HostedZoneNotEmpty", message)
        self.content_type = "text/xml"


class PublicZoneVPCAssociation(Route53ClientError):
    """Public hosted zone can't be associated."""

    code = 400

    def __init__(self):
        message = "You're trying to associate a VPC with a public hosted zone. Amazon Route 53 doesn't support associating a VPC with a public hosted zone."
        super().__init__("PublicZoneVPCAssociation", message)
        self.content_type = "text/xml"


class LastVPCAssociation(Route53ClientError):
    """Last VPC can't be disassociate."""

    code = 400

    def __init__(self):
        message = "The VPC that you're trying to disassociate from the private hosted zone is the last VPC that is associated with the hosted zone. Amazon Route 53 doesn't support disassociating the last VPC from a hosted zone."
        super().__init__("LastVPCAssociation", message)
        self.content_type = "text/xml"


class NoSuchQueryLoggingConfig(Route53ClientError):
    """Query log config does not exist."""

    code = 404

    def __init__(self):
        message = "The query logging configuration does not exist"
        super().__init__("NoSuchQueryLoggingConfig", message)


class QueryLoggingConfigAlreadyExists(Route53ClientError):
    """Query log config exists for the hosted zone."""

    code = 409

    def __init__(self):
        message = "A query logging configuration already exists for this hosted zone"
        super().__init__("QueryLoggingConfigAlreadyExists", message)


class InvalidChangeBatch(Route53ClientError):

    code = 400

    def __init__(self):
        message = "Number of records limit of 1000 exceeded."
        super().__init__("InvalidChangeBatch", message)


class NoSuchDelegationSet(Route53ClientError):
    code = 400

    def __init__(self, delegation_set_id):
        super().__init__("NoSuchDelegationSet", delegation_set_id)
        self.content_type = "text/xml"


class DnsNameInvalidForZone(Route53ClientError):
    code = 400

    def __init__(self, name, zone_name):
        error_msg = (
            f"""RRSet with DNS name {name} is not permitted in zone {zone_name}"""
        )
        super().__init__("InvalidChangeBatch", error_msg)


class ChangeSetAlreadyExists(Route53ClientError):
    code = 400

    def __init__(self, action: str, name: str, _type: str):
        super().__init__(
            "InvalidChangeBatch",
            f"Tried to {action.lower()} resource record set [name='{name}', type='{_type}'] but it already exists",
        )
