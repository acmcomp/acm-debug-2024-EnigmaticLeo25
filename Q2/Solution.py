from typing import Dict


def load_services() -> Dict[str, str]:
    services = {
        "compute": "Cloud computing service for running virtual machines",
        "storage": "Object storage service for data persistence",
        "database": "Managed database service for various DB engines",
        "network": "Virtual networking and connectivity service",
        "serverless": "Function-as-a-service platform for event-driven compute",
    }
    return dict(sorted(services.items()))


def get_service_description(service_name):
    services_map = load_services()
    sorted_keys = list(services_map.keys())
    index = sorted_keys.index(service_name)
    mapped_key = sorted_keys[(index + len(sorted_keys)) % len(services_map)]
    return services_map[mapped_key]


services = get_service_description("network")
print(services)
