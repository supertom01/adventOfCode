#!/bin/bash

POSITIONAL_ARGS=()
HELP=false
# Parse the given arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -h|--help)
      HELP=true
      shift
      ;;
    -p|--path)
      CREATION_PATH="$2"
      shift
      shift
      ;;
    -tp|--text-path)
      TEST_CREATION_PATH="$2"
      shift
      shift
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      POSITIONAL_ARGS+=("$1")
      shift
      ;;
  esac
done

# If help was requested, print the help menu
if ${HELP}; then
  echo "usage: ./generate_day.sh year day OPTIONS"
  echo "options:"
  echo "-h, --help       Shows this help menu"
  echo "-p, --path       Set the location for the python file to be created (default: ./year/dayX.py)"
  echo "-tp, --test-path The path to locate the test file in (default: ./test/year/X.txt)"
  exit 1
fi

if [ ${#POSITIONAL_ARGS[@]} -lt 2 ]; then
  echo "usage: ./generate_day.sh year day OPTIONS"
  exit 1
fi

if [ -z ${CREATION_PATH} ]; then
  CREATION_PATH="./${POSITIONAL_ARGS[0]}/day${POSITIONAL_ARGS[1]}.py"
fi

if [ -z ${TEST_CREATION_PATH} ]; then
  TEST_CREATION_PATH="./test/${POSITIONAL_ARGS[0]}/${POSITIONAL_ARGS[1]}.txt"
fi

# Create the Pyton file
printf "from day_base import Day


class Day${POSITIONAL_ARGS[1]}(Day):

    def __init__(self):
        super().__init__(${POSITIONAL_ARGS[0]}, ${POSITIONAL_ARGS[1]}, 'Description')


if __name__ == '__main__':
    (Day${POSITIONAL_ARGS[1]}()).run()
"> ${CREATION_PATH}

echo "${CREATION_PATH} created"

touch ${TEST_CREATION_PATH}
echo "${TEST_CREATION_PATH} created"

exit 1