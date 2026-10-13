"""05 - re, datetime, zoneinfo, json, logging."""
import json, logging, re
from datetime import datetime, date, timedelta, timezone
from zoneinfo import ZoneInfo

# --- Regular expressions ---
text = "Contact: ada@example.com, bo@test.org"
print(re.findall(r"[\w.]+@[\w.]+\.\w+", text))
m = re.search(r"(?P<user>\w+)@(?P<host>[\w.]+)", text)
print(m.group("user"), m.groupdict())
print(re.sub(r"\d+", "#", "a1b22c333"))
pattern = re.compile(r"^\d{3}-\d{4}$")
print(bool(pattern.match("555-1234")))

# --- datetime ---
now = datetime(2026, 3, 15, 9, 30)
print(now.strftime("%Y-%m-%d %H:%M"), now.isoformat())
print(datetime.strptime("2026-01-31", "%Y-%m-%d").date())
print(date(2026, 12, 25) - date(2026, 1, 1), now + timedelta(hours=5))
utc = datetime(2026, 6, 1, 12, tzinfo=timezone.utc)
print(utc.astimezone(ZoneInfo("Asia/Kolkata")))

# --- JSON with custom encoder ---
class Enc(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)): return o.isoformat()
        return super().default(o)
print(json.dumps({"when": now, "ok": True}, cls=Enc, sort_keys=True))

# --- logging (prefer over print in real apps) ---
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s")
log = logging.getLogger("study")
log.info("started"); log.warning("careful"); log.debug("hidden at INFO level")
