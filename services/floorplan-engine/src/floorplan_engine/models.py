from dataclasses import dataclass, field

@dataclass
class Component:

    id: int

    area: int

    left: int

    top: int

    width: int

    height: int

    aspect_ratio: float

    fill_ratio: float

    cls: str = "UNKNOWN"

    contour: any = None