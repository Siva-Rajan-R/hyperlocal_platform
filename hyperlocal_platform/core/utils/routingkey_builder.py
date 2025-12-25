from ..enums.routingkey_enum import RoutingkeyActions,RoutingkeyState,RoutingkeyVersions

def generate_routingkey(domain:str,action:RoutingkeyActions,state:RoutingkeyState,version:RoutingkeyVersions):
    return f"{domain}.{action.value}.{state.value}.{version.value}"