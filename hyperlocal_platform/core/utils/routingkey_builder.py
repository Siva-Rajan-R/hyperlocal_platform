from ..enums.routingkey_enum import RoutingkeyActions,RoutingkeyState,RoutingkeyVersions

def generate_routingkey(domain:str,work_for:str,action:RoutingkeyActions,state:RoutingkeyState,version:RoutingkeyVersions):
    """
    The domain is the current service name, work-for is a service name of who triggered,

    """
    return f"{domain.lower()}.{work_for.lower()}.{action.value.lower()}.{state.value.lower()}.{version.value.lower()}"