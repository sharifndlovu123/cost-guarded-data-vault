"""Remediation ladder: decide what to do with one resource. Pure function, so it is easy to test."""


def decide(resource: dict) -> str:
    tags = resource.get("tags", {})
    if "keep" in tags:
        return "skip"
    if "owner" in tags:
        return "notify_owner"
    return "snapshot_and_stop"
