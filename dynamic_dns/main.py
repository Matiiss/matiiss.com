import os
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path

import httpx


class BigDooDooTime(Exception): ...


def get_env_var(name: str) -> str:
    env_var = os.getenv(name)
    if env_var is None:
        raise BigDooDooTime(f"Environment variable {name} not set")

    return env_var


IP_PATH = Path("/app/data/ip.txt")
IP_PATH.parent.mkdir(parents=True, exist_ok=True)
IP_PATH.touch(exist_ok=True)

CLOUDFLARE_API_URL = "https://api.cloudflare.com/client/v4"

CLOUDFLARE_API_TOKEN = get_env_var("CLOUDFLARE_API_TOKEN")
CLOUDFLARE_ZONE_ID = get_env_var("CLOUDFLARE_ZONE_ID")
CLOUDFLARE_DNS_RECORD_IDS = get_env_var("CLOUDFLARE_DNS_RECORD_IDS").split(",")


def get_wan_ip():
    output = subprocess.check_output(["upnpc", "-s"], text=True)

    for line in output.splitlines():
        line = line.strip()

        if not line.startswith("ExternalIPAddress"):
            continue

        return line.split("=")[1].strip()

    raise BigDooDooTime


def update_dns_records(ip: str) -> None:
    with httpx.Client(
        headers={"Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}"}
    ) as client:
        for record_id in CLOUDFLARE_DNS_RECORD_IDS:
            record_api_url = f"{CLOUDFLARE_API_URL}/zones/{CLOUDFLARE_ZONE_ID}/dns_records/{record_id}"

            response = client.get(record_api_url).json()
            name = response["result"]["name"]
            ttl = response["result"]["ttl"]
            record_type = response["result"]["type"]

            client.patch(
                record_api_url,
                json={
                    "name": name,
                    "ttl": ttl,
                    "type": record_type,
                    "content": ip,
                },
            )


def now() -> str:
    return datetime.now(timezone.utc).isoformat(sep=" ", timespec="seconds")


def main():
    while True:
        previous_ip = IP_PATH.read_text().strip()
        current_ip = get_wan_ip()

        if previous_ip != current_ip:
            print(f"[{now()}] Previous IP: {previous_ip}", flush=True)
            print(f"[{now()}] Current IP: {current_ip}", flush=True)

            update_dns_records(current_ip)
            IP_PATH.write_text(current_ip)

            print(f"[{now()}] Updated DNS records", flush=True)

        time.sleep(60)  # sleep for a minute (literally)


if __name__ == "__main__":
    main()
