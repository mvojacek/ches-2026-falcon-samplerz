#!/usr/bin/env python3

import argparse
import os
import tempfile
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

LOGIN_ORIGIN = "https://login.amd.com"
FIREFOX_BINARY = "/snap/firefox/current/usr/lib/firefox/firefox"
GECKODRIVER_BINARY = "/snap/bin/geckodriver"


def save_amd_login(
    driver: webdriver.Firefox,
    username: str,
    password: str,
) -> None:
    script = """
        const [origin, username, password, done] = arguments;
        const login = Components.classes[
            "@mozilla.org/login-manager/loginInfo;1"
        ].createInstance(Components.interfaces.nsILoginInfo);
        login.init(origin, "", null, username, password, "", "");
        Services.logins.addLoginAsync(login).then(
            () => done(null),
            error => done(String(error))
        );
    """

    with driver.context(driver.CONTEXT_CHROME):
        error = driver.execute_async_script(
            script,
            LOGIN_ORIGIN,
            username,
            password,
        )

    if error is not None:
        raise RuntimeError(f"Firefox could not save the AMD login: {error}")


def wait_for_installer(download_dir: Path) -> Path:
    previous: tuple[Path, int] | None = None
    stable_samples = 0

    while True:
        installers = sorted(
            download_dir.glob("*.bin"),
            key=lambda path: path.stat().st_mtime_ns,
            reverse=True,
        )

        if installers and not any(download_dir.glob("*.part")):
            installer = installers[0]
            current = (installer, installer.stat().st_size)
            if current == previous:
                stable_samples += 1
                if stable_samples >= 5:
                    return installer
            else:
                stable_samples = 0
                previous = current

        time.sleep(1)


def download_amd_installer(
    url: str,
    target_dir: Path,
    username: str,
    password: str,
) -> Path:
    target_dir = target_dir.expanduser().resolve()
    target_dir.mkdir(parents=True, exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="amd-firefox-") as temporary_dir:
        temporary = Path(temporary_dir)
        profile_dir = temporary / "profile"
        download_dir = target_dir
        profile_dir.mkdir()

        options = Options()
        options.binary_location = FIREFOX_BINARY
        options.profile = str(profile_dir)
        options.set_preference("signon.rememberSignons", True)
        options.set_preference("signon.autofillForms", True)
        options.set_preference("signon.autofillForms.autocompleteOff", True)
        options.set_preference("signon.autofillForms.http", False)
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.dir", str(download_dir))
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference(
            "browser.helperApps.neverAsk.saveToDisk",
            "application/octet-stream",
        )

        driver: webdriver.Firefox | None = None
        try:
            service = Service(
                executable_path=GECKODRIVER_BINARY,
                service_args=["--allow-system-access"],
            )
            driver = webdriver.Firefox(options=options, service=service)
            save_amd_login(driver, username, password)
            driver.get(url)

            print("Firefox is open with the AMD login ready for autofill.", flush=True)
            print("Complete the download form in the VM browser and start the .bin download.", flush=True)
            print("Provisioning will wait without a timeout until the installer is ready.", flush=True)
            installer = wait_for_installer(download_dir)
        finally:
            if driver is not None:
                driver.quit()

        return installer


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Interactively download the Vivado installer with Firefox."
    )
    parser.add_argument("url")
    parser.add_argument("target_dir", type=Path)
    args = parser.parse_args()

    username = os.environ.get("XILINX_USERNAME")
    password = os.environ.get("XILINX_PASSWORD")
    if not username:
        parser.error("XILINX_USERNAME is not set")
    if not password:
        parser.error("XILINX_PASSWORD is not set")

    installer = download_amd_installer(
        args.url,
        args.target_dir,
        username,
        password,
    )
    print(f"Installer ready: {installer}", flush=True)


if __name__ == "__main__":
    main()
