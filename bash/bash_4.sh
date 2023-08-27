# Contoh Bash
echo "Starting at: $(date)"
echo

echo "UPTIME"
uptime
echo

echo "FREE"
free
echo

echo "WHO"
who
echo

echo "Finishing at: $(date)"

# atau bisa juga dengan penulisan seperti ini

echo "Starting at: $(date)"; echo

echo "UPTIME"; uptime; echo

echo "FREE"; free; echo

echo "WHO"; who; echo

echo "Finishing at: $(date)"


# variabel

line = "------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)" $line