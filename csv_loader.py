import os
import re
import folder_paths
from abc import ABC, abstractmethod

ARCHITECTS = "Architects"
ARTISTS = "Artists"
COLORS = "Colors"
DESIGNERS = "Designers"
LIGHTS = "Lights"
MATERIALS = "Materials"
ARTMOVEMENTS = "Artmovements"
CHARACTERS = "Characters"
COMPOSITION = "Composition"
LIGHTING = "Lighting"
SETTINGS = "Settings"
STYLES = "Styles"
POSITIVE = "Positive"
NEGATIVE = "Negative"


class CSVLoader(ABC):
    """
    Base abstract class for load csv items.
    """

    @staticmethod
    def load_csv(path: str):
        """Loads csv file with items. It has only one column.
        Ignore the first row (header).
        positive_prompt are strings separated by comma. Each string is a prompt.
        negative_prompt are strings separated by comma. Each string is a prompt.

        Returns:
            list: List of items. Each style is a dict with keys: style_name and value: [positive_prompt, negative_prompt]
        """

        items = {
            "Error loading items.csv, check the console": ["", ""]}
        if not os.path.exists(path):
            print(f"""Error. No items.csv found. Put your items.csv in the custom_nodes/ComfyUI_Loader/CSV directory of ComfyUI. Then press "Refresh".
                  Your current root directory is: {folder_paths.base_path}
            """)
            return items
        try:
            with open(path, "r", encoding="utf-8") as f:
                items = [[x.replace('"', '').replace('\n', '') for x in
                          re.split(',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)]
                         for
                         line in f.readlines()[1:]]
                items = {x[0]: [x[1], x[2]] for x in items}
        except Exception as e:
            print(f"""Error loading items.csv. Make sure it is in the custom_nodes/ComfyUI_Loader/CSV directory of ComfyUI. Then press "Refresh".
                    Your current root directory is: {folder_paths.base_path}
                    Error: {e}
            """)
        return items

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive prompt", "negative prompt")
    FUNCTION = "execute"
    CATEGORY = "CSV Loaders"

    @classmethod
    def INPUT_TYPES(cls, item_name):
        cls.items_csv = cls.load_csv(
            os.path.join(folder_paths.base_path,
                         "custom_nodes", "ComfyUI-CSV-Loader", "CSV", f"{item_name}.csv"))
        return {
            "required": {
                f"{item_name}": (list(cls.items_csv.keys()),),
            },
        }

    @abstractmethod
    def execute(self, class_name):
        pass


# ARCHITECTS
class ArchitectsCSVLoader(CSVLoader):
    """
    Loads csv file with characters. For migration purposes from automatic11111 webui.
    """
    item_name = ARCHITECTS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, architects):
        return (
            self.items_csv[architects][0], self.items_csv[architects][1])


# ARTISTS
class ArtistsCSVLoader(CSVLoader):
    """
    Loads csv file with artists.
    """
    item_name = ARTISTS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, artists):
        return self.items_csv[artists][0], self.items_csv[artists][1]


# COLORS
class ColorsCSVLoader(CSVLoader):
    """
    Loads csv file with colors.
    """
    item_name = COLORS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, colors):
        return self.items_csv[colors][0], self.items_csv[colors][1]


# DESIGNERS
class DesignersCSVLoader(CSVLoader):
    """
    Loads csv file with designers.
    """
    item_name = DESIGNERS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, designers):
        return self.items_csv[designers][0], self.items_csv[designers][1]


# LIGHTS
class LightsCSVLoader(CSVLoader):
    """
    Loads csv file with lights.
    """
    item_name = LIGHTS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, lights):
        return self.items_csv[lights][0], self.items_csv[lights][1]


# MATERIALS
class MaterialsCSVLoader(CSVLoader):
    """
    Loads csv file with lights.
    """
    item_name = MATERIALS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, materials):
        return self.items_csv[materials][0], self.items_csv[materials][1]


# ARTMOVEMENTS
class ArtmovementsCSVLoader(CSVLoader):
    """
    Loads csv file with artmovements.
    """
    item_name = ARTMOVEMENTS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, artmovements):
        return self.items_csv[artmovements][0], self.items_csv[artmovements][1]


# CHARACTERS
class CharactersCSVLoader(CSVLoader):
    """
    Loads csv file with characters.
    """
    item_name = CHARACTERS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, characters):
        return self.items_csv[characters][0], self.items_csv[characters][1]


# COMPOSITION
class CompositionCSVLoader(CSVLoader):
    """
    Loads csv file with composition.
    """
    item_name = COMPOSITION.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, composition):
        return self.items_csv[composition][0], self.items_csv[composition][1]


# LIGHTING
class LightingCSVLoader(CSVLoader):
    """
    Loads csv file with lighting.
    """
    item_name = LIGHTING.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, lighting):
        return self.items_csv[lighting][0], self.items_csv[lighting][1]


# SETTING
class SettingsCSVLoader(CSVLoader):
    """
    Loads csv file with settings.
    """
    item_name = SETTINGS.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, setting):
        return self.items_csv[setting][0], self.items_csv[setting][1]


# STYLE
class StylesCSVLoader(CSVLoader):
    """
    Loads csv file with styles. For migration purposes from automatic11111 webui.
    """
    item_name = STYLES.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, style):
        return self.items_csv[style][0], self.items_csv[style][1]


# POSITIVE
class PositiveCSVLoader(CSVLoader):
    """
    Loads csv file with positive. For migration purposes from automatic11111 webui.
    """
    item_name = POSITIVE.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, positive):
        return self.items_csv[positive][0], self.items_csv[positive][1]


# NEGATIVE
class NegativeCSVLoader(CSVLoader):
    """
    Loads csv file with negative. For migration purposes from automatic11111 webui.
    """
    item_name = NEGATIVE.lower()

    @classmethod
    def INPUT_TYPES(cls):
        return super().INPUT_TYPES(cls.item_name)

    def execute(self, negative):
        return self.items_csv[negative][0], self.items_csv[negative][1]


# NODE NAMING

NODE_CLASS_MAPPINGS = {
    f"Load {ARCHITECTS} CSV": ArchitectsCSVLoader,
    f"Load {ARTISTS} CSV": ArtistsCSVLoader,
    f"Load {COLORS} CSV": ColorsCSVLoader,
    f"Load {DESIGNERS} CSV": DesignersCSVLoader,
    f"Load {LIGHTS} CSV": LightsCSVLoader,
    f"Load {MATERIALS} CSV": MaterialsCSVLoader,
    f"Load {ARTMOVEMENTS} CSV": ArtmovementsCSVLoader,
    f"Load {CHARACTERS} CSV": CharactersCSVLoader,
    f"Load {COMPOSITION} CSV": CompositionCSVLoader,
    f"Load {LIGHTING} CSV": LightingCSVLoader,
    f"Load {SETTINGS} CSV": SettingsCSVLoader,
    f"Load {STYLES} CSV": StylesCSVLoader,
    f"Load {POSITIVE} CSV": PositiveCSVLoader,
    f"Load {NEGATIVE} CSV": NegativeCSVLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    f"{ARCHITECTS}CSVLoader": f"Load {ARCHITECTS} CSV Node",
    f"{ARTISTS}CSVLoader": f"Load {ARTISTS} CSV Node",
    f"{COLORS}CSVLoader": f"Load {COLORS} CSV Node",
    f"{DESIGNERS}CSVLoader": f"Load {DESIGNERS} CSV Node",
    f"{LIGHTS}CSVLoader": f"Load {LIGHTS} CSV Node",
    f"{MATERIALS}CSVLoader": f"Load {MATERIALS} CSV Node",
    f"{ARTMOVEMENTS}CSVLoader": f"Load {ARTMOVEMENTS} CSV Node",
    f"{CHARACTERS}CSVLoader": f"Load {CHARACTERS} CSV Node",
    f"{COMPOSITION}CSVLoader": f"Load {COMPOSITION} CSV Node",
    f"{LIGHTING}CSVLoader": f"Load {LIGHTING} CSV Node",
    f"{SETTINGS}CSVLoader": f"Load {SETTINGS} CSV Node",
    f"{STYLES}CSVLoader": f"Load {STYLES} CSV Node",
    f"{POSITIVE}CSVLoader": f"Load {POSITIVE} CSV Node",
    f"{NEGATIVE}CSVLoader": f"Load {NEGATIVE} CSV Node"
}
