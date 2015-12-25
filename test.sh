#!/usr/bin/env bash
file_string=$(ls -a)
file_names=(${file_string//\\n/})
exit_code=0
for i in "${!file_names[@]}"
do
  if [ -d "${file_names[i]}" ]; then
    if [ "${file_names[i]}" == ".." ]; then
      continue
    fi
    sub_file_string=$(ls -a "${file_names[i]}")
    sub_file_names=(${sub_file_string//\\n/})
    for j in "${!sub_file_names[@]}"
    do
      extension="${sub_file_names[j]##*.}"
      if [ "$extension" == "py" ]; then
        echo "${file_names[i]}/${sub_file_names[j]}"
        python "${file_names[i]}/${sub_file_names[j]}"
        if [ "$?" -ne 0 ]; then
          exit_code=1
        fi
        echo ""
      fi
    done
  fi
done
exit $exit_code
