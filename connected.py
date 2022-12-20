import subprocess

class ConnectedWIFI:


    def __init__(self):
        self.get_passwords()


    def get_passwords(self):
        self.wifi_name = ""
        self.wifi_password = ""
        self.list_of_profiles = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        for i in self.list_of_profiles:

            if "All User Profile" in i:
                self.current_profile = i.split("All User Profile     : ", 1)[1].strip()
                self.get_network = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', self.current_profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                for j in self.get_network:

                    self.network_info = j.strip()
                    if "SSID name              : " in self.network_info:
                        self.wifi_name = j.split("SSID name              : ", 1)[1].strip()

                    if "Key Content            : " in self.network_info:
                        self.wifi_password = j.split("Key Content            : ", 1)[1].strip()
                        self.wifi_name = self.wifi_name.replace('"', '')
                        print(f"{self.wifi_name} : {self.wifi_password}")



ConnectedWIFI()