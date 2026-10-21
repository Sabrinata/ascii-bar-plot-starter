from rich.console import Console
from rich.bar import Bar

values = [
    ("A", 2.16),
    ("B", 4.33),
    ("C", 6.57),
    ("D", 8.71),
]

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values):
    console = Console()

    maximum = max(value for name, value in values)

    for name, value in values:
        length = scale_bar(value, maximum)

        bar = Bar(
            size=40,
            begin=0,
            end=length,
            color="green"
        )

        console.print(name, bar)

render_bar_chart(values)