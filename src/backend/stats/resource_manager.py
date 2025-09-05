from typing import Dict
from .resource import Resource


class ResourceManager:
    """
    Container for multiple resources with convenient access methods.
    """
    def __init__(self):
        self._resources: Dict[str, Resource] = {}

    # --- Helper ---
    def _normalize_name(self, name: str) -> str:
        return name.lower()

    # --- Accessors/Mutators ---
    def add(self, name: str, base: float, current: float, **kwargs):
        resource = Resource(name, base, current, **kwargs)
        self.add_resource(resource)

    def add_resource(self, resource: Resource):
        key = self._normalize_name(resource.name)
        self._resources[key] = resource

    def get_resource(self, name: str) -> Resource:
        key = self._normalize_name(name)
        return self._resources[key]

    def contains_resource(self, name: str) -> bool:
        key = self._normalize_name(name)
        return key in self._resources

    # --- Convenience ---
    def __getitem__(self, name: str):
        """Dict-like access"""
        key = self._normalize_name(name)
        if key in self._resources:
            return self._resources[key]
        raise KeyError(f"'{name}' not found in stats")

    def __contains__(self, name: str) -> bool:
        key = self._normalize_name(name)
        return key in self._resources

    def __repr__(self):
        stats = ", ".join(f"{k}={v.value}" for k, v in self._resources.items())
        return f"<Stats stats=[{stats}]>"

    # --- Serialization ---
    def serialize(self) -> dict:
        return {
            name: res.serialize()
            for name, res in self._resources.items()
        }

    @classmethod
    def deserialize(cls, data: dict) -> "ResourceManager":
        mgr = cls()
        for res_data in data.values():
            res = Resource.deserialize(res_data)
            mgr.add_resource(res)
        return mgr
