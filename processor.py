import json
from pathlib import Path
from collections import defaultdict
from typing import Dict, Union

MEMORY_FILE = Path("memory.json")

# --- Load or initialize memory ---
if not MEMORY_FILE.exists():
    MEMORY_FILE.write_text("{}")

try:
    memory: Dict[str, Dict] = json.loads(MEMORY_FILE.read_text())
except json.JSONDecodeError:
    memory = {}

def _parse_recipe(s: str) -> Dict[tuple[str, int], Dict[str, int]]:
    left, right = s.strip().split(":")
    k_count, k_item = left.split("*")
    key = (k_item.strip(), int(k_count))

    outputs = {item.strip(): int(count.strip())
               for count, item in (o.split("*") for o in right.split(","))}

    return {key: outputs}

def add_recipe(recipe:str):
    recipe = _parse_recipe(recipe)
    Gitem = ""
# --- Add to memory ---
    for (item, qty), outputs in recipe.items():
        Gitem = item
        if item not in memory:
            memory[item] = {
                "integration": {k: v / qty for k, v in outputs.items()}
            }

    # --- Save memory ---
    print(f"recipe: {Gitem}\nintegration: {({k: v / qty for k, v in outputs.items()})}")
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))


# --- Recursive expander ---
def expand_recipe(item: str, count: float = 1) -> Dict[str, float]:
    """Recursively expand recipe to basic ingredients."""
    if item not in memory:
        return {item: count}

    result = defaultdict(float)
    for sub_item, sub_count in memory[item]["integration"].items():
        for k, v in expand_recipe(sub_item, count * sub_count).items():
            result[k] += v
    return dict(result)

