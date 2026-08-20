from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Place:
    id: int
    name: str
    parent_id: Optional[int] = None

@dataclass
class Permission:
    permission_id: str
    place_id: int
    timestamp: int
    is_granted: bool

class GoogleAdWord:
    def __init__(self) -> None:
        self._places: Dict[int, Place] = {}
        self._permissions: Dict[str, Permission] = {}
        self._timestamp: int = 0
    
    def _generate_permission_id(self, advertiser_id: str, place_id: int) -> str:
        return f"{advertiser_id}_{place_id}"
    
    def _increment_timestamp(self) -> int:
        self._timestamp += 1
        return self._timestamp

    def add_place(self, name: str) -> int:
        new_id = len(self._places)
        self._places[new_id] = Place(id=new_id, name=name)
        return new_id

    def set_place_parent(self, place_id: int, parent_id: int) -> None:
        if place_id not in self._places or parent_id not in self._places:
            raise ValueError("Invalid place or parent ID")
        
        place = self._places[place_id]
        self._places[place_id] = Place(
            id=place.id,
            name=place.name,
            parent_id=parent_id
        )

    def get_place_hierarchy(self, place_id: int) -> List[int]:
        hierarchy = []
        current_id = place_id

        while current_id is not None:
            hierarchy.append(current_id)
            place = self._places.get(current_id)
            if not place:
                break
            current_id = place.parent_id

        return hierarchy

    def grant_access(self, advertiser_id: str, place_id: int) -> None:
        if place_id not in self._places:
            raise ValueError("Invalid place ID")

        timestamp = self._increment_timestamp()
        permission = Permission(
            permission_id=advertiser_id,
            place_id=place_id,
            timestamp=timestamp,
            is_granted=True
        )
        self._permissions[self._generate_permission_id(advertiser_id, place_id)] = permission

    def revoke_access(self, advertiser_id: str, place_id: int) -> None:
        if place_id not in self._places:
            raise ValueError("Invalid place ID")

        timestamp = self._increment_timestamp()
        permission = Permission(
            permission_id=advertiser_id,
            place_id=place_id,
            timestamp=timestamp,
            is_granted=False
        )
        self._permissions[self._generate_permission_id(advertiser_id, place_id)] = permission

    def check_access(self, advertiser_id: str, place_id: int) -> bool:
        if place_id not in self._places:
            return False

        hierarchy = self.get_place_hierarchy(place_id)
        
        latest_permission = None
        for place_id in hierarchy:
            key = self._generate_permission_id(advertiser_id, place_id)
            permission = self._permissions.get(key)
            
            if permission and (latest_permission is None or 
                             permission.timestamp > latest_permission.timestamp):
                latest_permission = permission

        return latest_permission.is_granted if latest_permission else False


# Example usage
if __name__ == "__main__":
    # Create an instance
    ad_word = GoogleAdWord()

    # Create place hierarchy
    europe_id = ad_word.add_place("Europe")
    france_id = ad_word.add_place("France")
    paris_id = ad_word.add_place("Paris")

    # Set up hierarchy
    ad_word.set_place_parent(france_id, europe_id)
    ad_word.set_place_parent(paris_id, france_id)

    # Test permissions
    advertiser = "advertiser1"
    
    # Grant access to Europe
    ad_word.grant_access(advertiser, europe_id)
    ad_word.grant_access(advertiser, france_id)
    print(f"Access to Europe: {ad_word.check_access(advertiser, europe_id)}")  # True
    print(f"Access to France: {ad_word.check_access(advertiser, france_id)}")  # True
    print(f"Access to Paris: {ad_word.check_access(advertiser, paris_id)}")    # True

    # Revoke access from France
    ad_word.revoke_access(advertiser, europe_id)
    print("\nAfter revoking access from France:")
    print(f"Access to Europe: {ad_word.check_access(advertiser, europe_id)}")  # True
    print(f"Access to France: {ad_word.check_access(advertiser, france_id)}")  # False
    print(f"Access to Paris: {ad_word.check_access(advertiser, paris_id)}")    # False