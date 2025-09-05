from typing import Dict, List
from .modifier import Modifier
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
        """
        Add a resource by providing a name, base_value, and additional args.
        """
        resource = Resource(name, base, current, **kwargs)
        self.add_resource(resource)

    def add_resource(self, resource: Resource):
        """
        Add a resource.
        """
        key = self._normalize_name(resource.name)
        self._resources[key] = resource

    def get_resource(self, name: str) -> Resource:
        """
        Get a resource by name.
        """
        key = self._normalize_name(name)
        return self._resources[key]

    def contains_resource(self, name: str) -> bool:
        """
        Check if a resource is in resources.
        """
        key = self._normalize_name(name)
        return key in self._resources

    # --- Tick ---
    def tick(self) -> Dict[str, List[Modifier]]:
        """
        Tick all resources, returning a dict mapping resource names
        to lists of expired modifiers.
        """
        expired_modifiers: Dict[str, List[Modifier]] = {}
        for key, res in self._resources.items():
            expired = res.tick()
            if expired:
                expired_modifiers[key] = expired
        return expired_modifiers

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

    # --- Overrides ---
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
