REM npx prettier part1.md --write
pandoc part1.md -t typst -f markdown -o part1.typ
cat ilm-header.typ > mlmw_part1.typ
cat part1.typ >> mlmw_part1.typ
typst compile mlmw_part1.typ