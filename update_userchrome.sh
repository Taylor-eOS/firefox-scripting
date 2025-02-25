#!/bin/bash
BASE_DIR="/home/l/.local/share/ice/firefox"
CSS_CONTENT='
#navigator-toolbox {
  border-bottom: none !important;
}
#nav-bar,
#identity-box,
#tabbrowser-tabs,
#TabsToolbar,
#nav-bar * {
  visibility: collapse !important;
}'

find "$BASE_DIR" -mindepth 1 -maxdepth 1 -type d | while read -r web_app_dir; do
  css_file="${web_app_dir}/chrome/userChrome.css"
  # Only proceed if file exists
  if [ -f "$css_file" ]; then
    # Check for existing content
    if ! grep -qF "$CSS_CONTENT" "$css_file"; then
      echo "$CSS_CONTENT" >> "$css_file"
      echo "Updated: ${css_file}"
    else
      echo "Already configured: ${css_file}"
    fi
  else
    echo "File not found: ${css_file} (skipping)"
  fi
done
