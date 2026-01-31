filename="file.txt"

IFS=$'\n'
for word in $(cat "$filename")
do
  echo "$word"
done