import os

def update_firefox_prefs(profile_path, prefs_to_update):
    prefs_file_path = os.path.join(profile_path, "prefs.js")
    if not os.path.exists(prefs_file_path):
        print("prefs.js not found in the specified profile directory.")
        return
    with open(prefs_file_path, 'r') as file:
        lines = file.readlines()
    updated_lines = []
    found_prefs = set()
    for line in lines:
        updated_line = line
        for pref, value in prefs_to_update.items():
            pref_string = f'user_pref("{pref}",'
            if line.startswith(pref_string):
                updated_line = f'user_pref("{pref}", {value});\n'
                found_prefs.add(pref)
        updated_lines.append(updated_line)
    for pref, value in prefs_to_update.items():
        if pref not in found_prefs:
            updated_lines.append(f'user_pref("{pref}", {value});\n')
    with open(prefs_file_path, 'w') as file:
        file.writelines(updated_lines)
    print("prefs.js updated successfully.")

if __name__ == "__main__":
    profile_path = input("Enter the path to your Firefox profile directory: ")

    prefs_to_update = {
        "browser.tabs.closeWindowWithLastTab": "false",
        "extensions.pocket.enabled": "false",
        "browser.translations.automaticallyPopup": "false",
        #"layout.css.devPixelsPerPx": "1.1",
        #"security.dialog_enable_delay": "10",
        "browser.urlbar.trimURLs": "false"
    }

    update_firefox_prefs(profile_path, prefs_to_update)

