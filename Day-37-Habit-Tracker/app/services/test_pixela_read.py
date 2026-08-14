from app.services.pixela_service import PixelaService


pixela = PixelaService()

GRAPH_ID = "u4-coding-world"


print("\n--- TODAY PIXEL ---")

today = pixela.get_today_pixel(
    graph_id=GRAPH_ID
)

print(today)


print("\n--- LATEST PIXEL ---")

latest = pixela.get_latest_pixel(
    graph_id=GRAPH_ID
)

print(latest)


print("\n--- SPECIFIC PIXEL ---")

specific = pixela.get_pixel(
    graph_id=GRAPH_ID,
    record_date="20260813"
)

print(specific)


print("\n--- ALL PIXELS ---")

pixels = pixela.get_pixels(
    graph_id=GRAPH_ID
)

print(pixels)