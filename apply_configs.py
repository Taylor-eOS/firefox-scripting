import os

def update_firefox_prefs(profile_path, prefs_to_update):
    prefs_file_path = os.path.join(profile_path, "prefs.js")
    if not os.path.exists(prefs_file_path):
        print("prefs.js not found in the specified directory. You have to launch the profile once for it to be created.")
        return
    with open(prefs_file_path, 'r') as file:
        lines = file.readlines()
    updated_lines = []
    found_prefs = set()
    for line in lines:
        updated_line = line
        for pref, (value, is_string) in prefs_to_update.items():
            pref_string = f'user_pref("{pref}",'
            if line.startswith(pref_string):
                #Format the value based on whether it's a string
                if is_string:
                    updated_line = f'user_pref("{pref}", "{value}");\n'
                else:
                    updated_line = f'user_pref("{pref}", {value});\n'
                found_prefs.add(pref)
        updated_lines.append(updated_line)
    #Add missing preferences
    for pref, (value, is_string) in prefs_to_update.items():
        if pref not in found_prefs:
            if is_string:
                updated_lines.append(f'user_pref("{pref}", "{value}");\n')
            else:
                updated_lines.append(f'user_pref("{pref}", {value});\n')
    #Write the updated content back to prefs.js
    with open(prefs_file_path, 'w') as file:
        file.writelines(updated_lines)
    print("prefs.js updated successfully.")

if __name__ == "__main__":
    profile_path = input("Path to Firefox profile directory (first line in about:profiles, likely in ~/.mozilla/firefox/): ")
    prefs_to_update = {
        #Format: "preference_name": ("value", is_string). You have to check in your prefs.js whether values are saved with strings. Some numbers are saved as strings.
        "browser.tabs.closeWindowWithLastTab": ("false", False),
        "extensions.pocket.enabled": ("false", False),
        "browser.translations.automaticallyPopup": ("false", False),
        "widget.non-native-theme.scrollbar.size.override": (15, False),
        #"widget.non-native-theme.enabled": (true, False),
        "toolkit.zoomManager.zoomValues": (".98,.99,1,1.01,1.02,1.03,1.04,1.05,1.06,1.07,1.08,1.09,1.1", True),
        "browser.urlbar.trimURLs": ("false", False),
        "browser.urlbar.maxRichResults": ("6", False),
        "browser.bookmarks.max_backups": ("4", False)}
    update_firefox_prefs(profile_path, prefs_to_update)

