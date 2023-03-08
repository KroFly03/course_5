import json
import random
from typing import Optional
import marshmallow_dataclass
from dataclasses import dataclass


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float


@dataclass
class Weapon:
    id: int
    name: str
    max_damage: float
    min_damage: float
    stamina_per_hit: float

    def damage(self) -> float:
        return round(random.uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    weapons: list[Weapon]
    armors: list[Armor]


class Equipment:
    def __init__(self):
        self.equipment: EquipmentData = self._get_data()

    @staticmethod
    def _get_data() -> EquipmentData:
        with open('data/equipment.json', encoding='utf-8') as file:
            data = json.load(file)
            equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
            return equipment_schema().load(data)

    def get_weapon(self, name: str) -> Optional[Weapon]:
        for weapon in self.equipment.weapons:
            if weapon.name == name:
                return weapon

        return None

    def get_armor(self, name: str) -> Optional[Armor]:
        for armor in self.equipment.armors:
            if armor.name == name:
                return armor

        return None

    def get_weapon_names(self) -> list[str]:
        return [weapon.name for weapon in self.equipment.weapons]
    
    def get_armor_names(self) -> list[str]:
        return [armor.name for armor in self.equipment.armors]
