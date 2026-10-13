#!/usr/bin/env bash
# Run every study script and report failures.  Usage: ./run_all.sh
set -u
fail=0
for f in 0[1-5]_*/*.py; do
  if python3 "$f" >/dev/null 2>&1; then echo "ok    $f"; else echo "FAIL  $f"; fail=1; fi
done
exit $fail
